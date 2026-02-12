import os
import sys
import asyncio
import traceback
import warnings
import dotenv
from typing import TypedDict, Annotated, List
from flask import Flask, request, jsonify
from flask_cors import CORS
import re
# --- LangChain/LangGraph 核心组件 ---
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, BaseMessage, SystemMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.prebuilt import ToolNode, tools_condition
import operator

# 加载环境变量
dotenv.load_dotenv()

# 创建Flask应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求

# 屏蔽无关警告
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ============= 全局配置 =============
RAG_SERVER_PATH = r"D:\Teacher_Assistant_AI\backend\Paper_composition\RAG_MCP.py"

# 从环境变量读取API配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
ALI_MODEL_NAME = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not DASHSCOPE_API_KEY:
    raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")

CLIENT = MultiServerMCPClient({
    # 1. 阿里云 WebSearch
    "WebSearch": {
        "transport": "sse",
        "url": "https://dashscope.aliyuncs.com/api/v1/mcps/WebSearch/sse",
        "headers": {"Authorization": f"Bearer {DASHSCOPE_API_KEY}"}
    },

    # 2. 文档解析 Agent
    "LLM_output_with_docxpdf_MCP_Agent_Challenge": {
        "transport": "streamable_http",
        "url": "https://mcp.api-inference.modelscope.net/b16a0cecccc149/mcp"
    },

    # 3. 本地 RAG 工具
    "LocalLangChainRAG": {
        "transport": "stdio",           # 本地通信模式
        "command": sys.executable,      # 自动使用当前环境的 python.exe
        "args": [RAG_SERVER_PATH],      # 使用修正后的绝对路径
    }
})

# ============= 定义工作流State =============
class QuizWorkflowState(TypedDict):
    query: str
    topic_content: str
    quiz_markdown: str
    pdf_url: str
    messages: Annotated[List[BaseMessage], operator.add]

# ============= 初始化模型 =============
# streaming=False 避免工具调用时的 Bug
_MODEL = ChatTongyi(model=ALI_MODEL_NAME, streaming=False, api_key=DASHSCOPE_API_KEY) 

# ============= 通用 Agent 构建函数 =============
def build_agent_graph(model, tools):
    """手动构建一个支持工具调用的 Agent 图"""
    model_with_tools = model.bind_tools(tools)

    def agent_node(state: MessagesState):
        return {"messages": [model_with_tools.invoke(state["messages"])]}

    workflow = StateGraph(MessagesState)
    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", ToolNode(tools))

    workflow.add_edge(START, "agent")
    workflow.add_conditional_edges("agent", tools_condition)
    workflow.add_edge("tools", "agent")

    return workflow.compile()

# ============= 第一步：通过MCP获取题目 =============
async def mcp_fetch_node(state: QuizWorkflowState) -> dict:
    """通过MCP服务获取资料（自动选择 联网搜索 或 本地RAG）"""
    query = state['query']
    print(f"\n[Step 1] 正在调用 MCP 工具检索关于 '{query}' 的信息...")
    
    try:
        # 1. 动态获取所有连接的工具 (包括 WebSearch 和 RAG)
        tools = await CLIENT.get_tools()
        # 打印一下工具名称，确认 RAG 是否加载成功
        tool_names = [t.name for t in tools]
        print(f"   >>> 已加载工具: {tool_names}")

        agent_app = build_agent_graph(_MODEL, tools)
        
        # 2. 优化提示词：允许模型自由选择工具
        # 如果用户问的是 LangChain 相关，模型应当选择本地 RAG；如果是高考题，选择 WebSearch
        system_content = (
            "你是一个智能教育资源助手。你拥有以下工具："
            "1. WebSearch: 用于搜索互联网上的最新信息、真题和时事。"
            "2. query_langchain_docs (或类似名称): 用于查询本地知识库中关于 LangChain 的技术文档。"
            "\n请根据用户的输入，智能选择最合适的工具。"
            "如果用户请求具体的试题，请尽量提供包含题干和答案的完整内容。"
        )

        inputs = {
            "messages": [
                SystemMessage(content=system_content),
                HumanMessage(content=f"请帮我查找关于以下主题的详细资料或试题：{query}")
            ]
        }

        # 3. 执行 Agent
        result = await asyncio.wait_for(agent_app.ainvoke(inputs), timeout=180)
        
        last_message = result["messages"][-1]
        content = last_message.content
        
        print(f"✓ Step 1 完成，获取到 {len(content)} 字符")
        return {"topic_content": content, "messages": result["messages"]}

    except Exception as e:
        print(f"\n✗ Step 1 严重异常: {type(e).__name__}")
        
        # 【核心调试代码】 尝试拆解 TaskGroup 异常
        # TaskGroup 会把子任务的错误包装成 ExceptionGroup，我们需要拆开看
        if hasattr(e, 'exceptions'):
            print("🔍 发现 ExceptionGroup，正在拆解子错误...")
            for i, sub_exc in enumerate(e.exceptions):
                print(f"\n--- 子错误 [{i+1}] ---")
                print(f"类型: {type(sub_exc).__name__}")
                print(f"内容: {str(sub_exc)}")
                # 如果是 Validation Error，通常意味着收到的不是 JSON
                if "validation error" in str(sub_exc).lower():
                    print("👉 分析: 主程序收到了无法解析的数据。可能是 Server 打印了非 JSON 内容。")
                traceback.print_exception(type(sub_exc), sub_exc, sub_exc.__traceback__)
        else:
            # 普通错误直接打印堆栈
            traceback.print_exception(type(e), e, e.__traceback__)
            
        return {"topic_content": f"检索失败: {str(e)}", "messages": []}
    # except Exception as e:
        
        # print(f"✗ Step 1 异常: {str(e)}")
        # if "index out of range" in str(e):
        #     print("提示: 请检查 ChatTongyi 是否设置了 streaming=False")
        # return {"topic_content": f"检索失败: {str(e)}", "messages": []}

# ============= 第二步：出卷生成试题 =============
async def quiz_generation_node(state: QuizWorkflowState) -> dict:
    print("\n[Step 2] 正在生成试题 Markdown...")
    
    topic_content = state.get("topic_content", "")
    if not topic_content or "失败" in topic_content[:10] or len(topic_content) < 10:
        print("! 跳过 Step 2 (资料获取不足)")
        return {"quiz_markdown": "无法生成试题：前置资料获取失败", "messages": []}

    system_prompt = """# Role: 试题排版与生成专家
## Profile
你擅长将杂乱的文本转化为结构严谨、排版美观的Markdown格式试题。

## Formatting Standards
1. **大题标题**：使用二级标题（`##`）（如：`## 一、选择题`）。
2. **小题结构**：`1. 题目内容`。
3. **答案结构**：答案必须**另起一行**，以“答：”开头。
4. **间距**：大题之间空一行，小题之间不空行。

请根据【资料内容】生成一份试题。"""
    
    try:
        response = await _MODEL.ainvoke([
            HumanMessage(content=system_prompt),
            HumanMessage(content=f"【资料内容】：\n{topic_content}")
        ])
        
        quiz_md = response.content
        print(f"✓ Step 2 完成，生成了 {len(quiz_md)} 字符的试题")
        return {"quiz_markdown": quiz_md, "messages": [response]}
        
    except Exception as e:
        print(f"✗ Step 2 异常: {str(e)}")
        return {"quiz_markdown": f"错误: {str(e)}", "messages": []}

# ============= 第三步：转PDF =============
async def markdown_to_pdf_node(state: QuizWorkflowState) -> dict:
    print("\n[Step 3] 正在转换为 PDF...")
    
    quiz_markdown = state.get("quiz_markdown", "")
    if not quiz_markdown or "错误" in quiz_markdown[:10] or len(quiz_markdown) < 20:
        return {"pdf_url": "", "messages": []} # 失败情况返回空

    try:
        tools = await CLIENT.get_tools()
        agent_app = build_agent_graph(_MODEL, tools)
        
        # 提示词保持不变
        system_prompt = (
            '你是一个文档助手。请调用 LLM_output_with_docxpdf_MCP_Agent_Challenge 工具，'
            '将用户提供的Markdown文本转换为 PDF 格式，并直接返回下载链接。'
        )
        
        inputs = {
            "messages": [
                SystemMessage(content=system_prompt),
                HumanMessage(content=f"请将以下内容转为PDF：\n\n{quiz_markdown[:5000]}") 
            ]
        }
        
        result = await asyncio.wait_for(agent_app.ainvoke(inputs), timeout=180)
        
        # 【核心修改开始】 ------------------------------------------------
        raw_content = result["messages"][-1].content
        print(f"原始模型返回: {raw_content}") # 调试用，看看模型到底说了啥

        # 使用正则表达式提取 URL
        # 匹配 http 或 https 开头，直到遇到空格、换行或右括号结束
        url_pattern = r"https?://[^\s\)]+"
        match = re.search(url_pattern, raw_content)

        if match:
            clean_url = match.group(0)
            print(f"✓ Step 3 完成，提取到链接: {clean_url}")
            return {"pdf_url": clean_url, "messages": result["messages"]}
        else:
            print("⚠️ 未能从模型回复中提取到有效链接")
            return {"pdf_url": "", "messages": result["messages"]}
        # 【核心修改结束】 ------------------------------------------------

    except Exception as e:
        print(f"✗ Step 3 异常: {str(e)}")
        return {"pdf_url": "", "messages": []}

# ============= 创建主工作流 =============
def create_quiz_workflow():
    graph = StateGraph(QuizWorkflowState)
    
    graph.add_node("mcp_fetch", mcp_fetch_node)
    graph.add_node("quiz_generation", quiz_generation_node)
    graph.add_node("pdf_conversion", markdown_to_pdf_node)
    
    graph.add_edge(START, "mcp_fetch")
    graph.add_edge("mcp_fetch", "quiz_generation")
    graph.add_edge("quiz_generation", "pdf_conversion")
    graph.add_edge("pdf_conversion", END)
    
    return graph.compile()

# ============= 异步生成函数 =============
async def generate_quiz_async(query):
    """异步生成试卷"""
    workflow = create_quiz_workflow()
    
    try:
        final_state = await workflow.ainvoke({
            "query": query,
            "topic_content": "",
            "quiz_markdown": "",
            "pdf_url": "",
            "messages": [],
        })
        
        return {
            "quiz_markdown": final_state.get('quiz_markdown', '无法生成试题'),
            "pdf_url": final_state.get('pdf_url', '')
        }
        
    except Exception as e:
        print(f"✗ 流程错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return {
            "quiz_markdown": f"生成失败: {str(e)}",
            "pdf_url": ""
        }

# ============= 智能组卷API接口 =============
@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    """生成试卷API接口"""
    try:
        # 获取请求数据
        data = request.get_json()
        if not data or 'query' not in data:
            return jsonify({'error': '缺少query参数'}), 400
        
        query = data['query']
        
        # 运行异步生成函数
        result = asyncio.run(generate_quiz_async(query))
        
        return jsonify(result), 200
        
    except Exception as e:
        print(f"API错误: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# ============= 主函数 =============
async def main():
    # 测试提示：
    # 1. 输入 "LangChain怎么安装" -> 应该调用 LocalLangChainRAG
    # 2. 输入 "2024高考数学导数真题" -> 应该调用 WebSearch
    query = input("请输入出题主题 (或技术查询): ")
    
    result = await generate_quiz_async(query)
    
    print("\n" + "="*50)
    print("✅ 工作流执行完成")
    print("="*50)
    
    print(f"\n[内容预览]:\n{result['quiz_markdown'][:500]}...\n")
    
    if "http" in str(result['pdf_url']):
        print(f"🎉 PDF 下载链接: {result['pdf_url']}")
    else:
        print(f"⚠️ PDF转换结果: {result['pdf_url']}")

# ============= 运行服务器 =============
if __name__ == "__main__":
    if len(sys.argv) == 1:
        # 添加 use_reloader=False 即使在 debug=True 时也禁止自动重启
        app.run(host='0.0.0.0', port=5002, debug=True, use_reloader=False)
    else:
        # 如果是通过命令行参数运行，执行测试
        asyncio.run(main())