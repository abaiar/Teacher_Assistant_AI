import os
import sys
import asyncio
import dotenv
from typing import Literal

# MCP 相关库
from fastmcp import FastMCP

# LangChain/LangGraph 相关库
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.tools import create_retriever_tool
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

# 加载环境变量
dotenv.load_dotenv()

# 【重要修复】定义安全日志函数
# MCP Stdio模式下，标准输出(stdout)只能用于协议通信
# 所有的日志必须打印到标准错误(stderr)
def log(message: str):
    sys.stderr.write(f"[RAG_SERVER] {message}\n")
    sys.stderr.flush()

# --- 1. 全局配置与初始化 (启动 Server 时执行) ---

log("正在初始化 RAG 知识库，请稍候...")  # 使用 log 替代 print

# 从环境变量读取API配置
api_key = os.getenv("DASHSCOPE_API_KEY")
ali_model_name = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not api_key:
    log("❌ 严重警告: 环境变量 DASHSCOPE_API_KEY 未找到！请检查 .env 文件")
    # 即使没有Key，也不要直接抛出异常退出，先让 Server 跑起来，
    # 否则 Client 会报 Connection closed
else:
    log(f"✅ 检测到 API Key (长度: {len(api_key)})")

# B. 加载并处理文档 (全局变量)
# 为了演示速度，这里只保留一个核心链接
urls = ["https://docs.langchain.com/oss/python/langchain/overview"]
try:
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=50 # 稍微调大chunk
    )
    doc_splits = text_splitter.split_documents(docs_list)

    # C. 初始化 Embedding 和 向量数据库
    embeddings = DashScopeEmbeddings(model="text-embedding-v2", dashscope_api_key=api_key)
    vectorstore = InMemoryVectorStore.from_documents(
        documents=doc_splits, embedding=embeddings
    )
    retriever = vectorstore.as_retriever()

    # D. 创建检索工具
    retriever_tool = create_retriever_tool(
        retriever,
        "retrieve_langchain_docs",
        "根据提供的Langchain官方文档，搜索并返回有关Langchain的信息",
    )
    
    log("向量库构建完成")

except Exception as e:
    log(f"初始化知识库失败: {str(e)}")
    # 即使失败也继续，避免 Server 直接崩溃，但在调用时会报错
    retriever_tool = None 

# E. 初始化 LLM 模型
response_model = ChatTongyi(model=ali_model_name, temperature=0, api_key=api_key)
grader_model = ChatTongyi(model=ali_model_name, temperature=0, api_key=api_key)

log("开始构建图逻辑...")

# --- 2. 定义 Graph 的节点逻辑 ---

class GradeDocuments(BaseModel):
    binary_score: str = Field(
        description="Relevance score: 'yes' if relevant, or 'no' if not relevant"
    )

GRADE_PROMPT = (
    "你是一个评估检索到的文档与用户问题相关度的评估器。 \n "
    "这里是检索到的文档: \n\n {context} \n\n"
    "这里是用户问题: {question} \n"
    "如果文档包含与用户问题相关的关键词或语义含义，将其评为相关。 \n"
    "请仅输出'yes'或'no'来表示文档是否与问题相关。"
)

REWRITE_PROMPT = (
    "请根据输入的问题，尝试推理出潜在的语义意图/含义。\n"
    "这里是初始问题:"
    "\n ------- \n"
    "{question}"
    "\n ------- \n"
    "请重新-formulate一个改进的问题:"
)

GENERATE_PROMPT = (
    "您是一个回答问题的助手。 "
    "使用以下检索到的上下文来回答问题。 "
    "如果您不知道答案，只是说您不知道。 "
    "使用最多三句话，保持答案简洁。\n"
    "问题: {question} \n"
    "上下文: {context}"
)

# 节点函数定义
def generate_query_or_respond(state: MessagesState):
    if retriever_tool is None:
        return {"messages": [{"role": "assistant", "content": "知识库初始化失败，无法检索。"}]}
        
    response = (
        response_model
        .bind_tools([retriever_tool]).invoke(state["messages"])
    )
    return {"messages": [response]}

def grade_documents(state: MessagesState) -> Literal["generate_answer", "rewrite_question"]:
    question = state["messages"][0].content
    context = state["messages"][-1].content
    
    # 简单的防御性检查
    if not context:
        return "rewrite_question"
 
    prompt = GRADE_PROMPT.format(question=question, context=context)
    
    try:
        response = (
            grader_model
            .with_structured_output(GradeDocuments).invoke(
                [{"role": "user", "content": prompt}]
            )
        )
    except Exception as e:
        log(f"⚠️ 评分模型调用异常: {e}")
        response = None

    # --- 核心修复开始 ---
    # 如果模型没返回结构化数据（None），我们默认认为文档“不相关”，或者“相关”
    # 这里为了保险，如果评分失败，通常选择重写问题或者直接尝试回答（看你偏好）
    if response is None:
        log("⚠️ 评分模型返回 None (解析失败)，默认执行: rewrite_question")
        return "rewrite_question" 
    # --- 核心修复结束 ---

    score = response.binary_score
    if score == "yes":
        return "generate_answer"
    else:
        log("文档相关性不足，触发重写...")
        return "rewrite_question"

def rewrite_question(state: MessagesState):
    messages = state["messages"]
    question = messages[0].content
    prompt = REWRITE_PROMPT.format(question=question)
    response = response_model.invoke([{"role": "user", "content": prompt}])
    return {"messages": [{"role": "user", "content": response.content}]}

def generate_answer(state: MessagesState):
    question = state["messages"][0].content
    context = state["messages"][-1].content 
    prompt = GENERATE_PROMPT.format(question=question, context=context)
    response = response_model.invoke([{"role": "user", "content": prompt}])
    return {"messages": [response]}

# --- 3. 构建并编译 Graph ---

workflow = StateGraph(MessagesState)

workflow.add_node("generate_query_or_respond", generate_query_or_respond)
workflow.add_node("retrieve", ToolNode([retriever_tool] if retriever_tool else []))
workflow.add_node("rewrite_question", rewrite_question)
workflow.add_node("generate_answer", generate_answer)

workflow.add_edge(START, "generate_query_or_respond")

workflow.add_conditional_edges(
    "generate_query_or_respond",
    tools_condition,
    {
        "tools": "retrieve",
        END: END,
    },
)

workflow.add_conditional_edges(
    "retrieve",
    grade_documents,
)
workflow.add_edge("generate_answer", END)
workflow.add_edge("rewrite_question", "generate_query_or_respond")

rag_graph = workflow.compile()
log("Graph 编译完成，准备启动 MCP Server。")

# --- 4. 定义 MCP Server ---

mcp = FastMCP("RAGTools")

@mcp.tool()
async def query_langchain_docs(query: str) -> str:
    """
    通过 RAG (检索增强生成) 查询 LangChain 的官方文档。
    包含文档检索、相关性评分和问题重写机制。
    
    Args:
        query: 用户关于 LangChain 的问题
    """
    log(f"收到查询请求: {query}")
    inputs = {"messages": [{"role": "user", "content": query}]}
    result = await rag_graph.ainvoke(inputs)
    final_response = result["messages"][-1].content
    log("查询完成")
    return final_response

# --- 5. 运行入口 ---
if __name__ == "__main__":
    # 使用 stdio 传输层
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        log(f"Server 运行错误: {e}")