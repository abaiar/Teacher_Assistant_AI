import os
import json
import dotenv
from typing import Optional, AsyncIterator, List, Dict, Any
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

dotenv.load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
ALI_MODEL_NAME = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not DASHSCOPE_API_KEY:
    raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")


class AICodingMentor:
    """AI 编程思维导师 - 采用苏格拉底式教学法"""
    
    def __init__(self):
        self.chat_llm = ChatTongyi(
            dashscope_api_key=DASHSCOPE_API_KEY,
            model=ALI_MODEL_NAME,
            temperature=0.7,
            streaming=True
        )
        
        self.non_stream_llm = ChatTongyi(
            dashscope_api_key=DASHSCOPE_API_KEY,
            model=ALI_MODEL_NAME,
            temperature=0.7,
            streaming=False
        )
        
        self.conversation_history: Dict[str, List] = {}
        self.help_counts: Dict[str, int] = {}
        
        self._setup_prompts()
    
    def _setup_prompts(self):
        """设置各种场景的 Prompt 模板"""
        
        self.socratic_system_prompt = """你是一个针对 10-15 岁学生的编程启蒙老师。你的名字叫'小助老师'。

【核心原则】
当学生代码出错时，绝对禁止直接给出正确代码！你需要：
1. 分析代码逻辑，找到 Bug
2. 用生动、幽默的比喻解释这个错误（例如：'变量就像一个小盒子，你是不是忘了往里面放东西？'）
3. 提出一个引导性问题，让学生自己思考如何修改

【求助次数规则】
- 第1次求助：只给比喻和引导问题
- 第2次求助：给出更具体的提示，但仍不给完整代码
- 第3次及以上求助：可以给出代码片段提示，但要用注释标注关键修改点

【回复格式要求】
请用以下格式回复：
🤔 **小助老师发现了一个问题**
[用生动的比喻描述问题]

💡 **小提示**
[引导性问题或提示]

🎯 **下一步**
[告诉学生应该思考什么]

【语言风格】
- 使用鼓励性的语言
- 可以使用表情符号让对话更有趣
- 避免使用过于专业的术语
- 如果学生答对了，要给予热情的表扬"""

        self.explain_flow_prompt = ChatPromptTemplate.from_messages([
            ("system", """你是一个面向中小学生的代码讲解老师。你的任务是将代码执行过程翻译成"慢动作解说"。

【要求】
1. 逐行解释代码，跟踪变量变化
2. 使用生动的比喻和生活化的例子
3. 把代码执行想象成一个故事
4. 输出必须是严格的 JSON 数组格式

【输出格式】
请严格按照以下 JSON 格式输出，不要添加任何其他文字：
[
  {{"line": 1, "desc": "第一行代码的生动解说..."}},
  {{"line": 2, "desc": "第二行代码的生动解说..."}},
  ...
]

【解说风格示例】
- 变量赋值：'我们在内存里开辟了一个叫 i 的小盒子，把数字 0 放了进去'
- 循环：'现在开始一个神奇的循环旅程，就像操场跑圈一样'
- 条件判断：'这里有个岔路口，我们需要看看条件是否满足才能决定走哪条路'
- 函数调用：'我们召唤了一个叫 xxx 的小助手来帮我们完成任务'"""),
            ("human", """请用故事化的方式讲解以下 {language} 代码的执行过程：

```
{code}
```

请输出 JSON 格式的逐行解说。""")
        ])
        
        self.prompt_eval_system = """你是一个 Prompt 工程教学助手，专门教中小学生如何写好 AI 提示词。

【评价维度】
1. 清晰度 (0-100分)：任务描述是否清楚明白
2. 约束条件 (0-100分)：是否有明确的限制和要求
3. 逻辑性 (0-100分)：需求描述是否有逻辑顺序

【回复格式】
请用以下格式回复：

📊 **Prompt 评分报告**

| 维度 | 得分 | 评价 |
|------|------|------|
| 清晰度 | XX/100 | ... |
| 约束条件 | XX/100 | ... |
| 逻辑性 | XX/100 | ... |
| **总分** | **XX/100** | |

💡 **优点**
- ...

🔧 **改进建议**
- ...

✨ **优化后的 Prompt 示例**
```
[给出一个优化后的 Prompt 示例]
```

【语言风格】
- 使用鼓励性的语言
- 对小朋友友好的表达方式
- 具体指出哪里写得好，哪里需要改进"""

    def _get_session_key(self, session_id: str) -> str:
        """获取会话键"""
        return session_id or "default"
    
    async def guide_debug(
        self,
        student_code: str,
        error_message: str,
        language: str,
        session_id: str,
        user_message: str = ""
    ) -> AsyncIterator[str]:
        """苏格拉底式纠错 - 流式输出"""
        key = self._get_session_key(session_id)
        
        if key not in self.conversation_history:
            self.conversation_history[key] = []
            self.help_counts[key] = 0
        
        help_count = self.help_counts.get(key, 0)
        
        context = f"""【学生代码】({language})
```
{student_code}
```

【错误信息】
{error_message if error_message else '代码没有报错，但可能存在逻辑问题'}

【求助次数】
这是学生第 {help_count + 1} 次求助

【学生最新消息】
{user_message if user_message else '学生请求帮助'}"""

        messages = [
            SystemMessage(content=self.socratic_system_prompt),
        ]
        
        for msg in self.conversation_history[key][-6:]:
            messages.append(msg)
        
        messages.append(HumanMessage(content=context))
        
        self.help_counts[key] = help_count + 1
        
        full_response = ""
        async for chunk in self.chat_llm.astream(messages):
            content = chunk.content
            full_response += content
            yield content
        
        self.conversation_history[key].append(HumanMessage(content=context))
        self.conversation_history[key].append(AIMessage(content=full_response))
    
    async def explain_flow_visually(
        self,
        code: str,
        language: str
    ) -> List[Dict[str, Any]]:
        """代码故事化讲解 - 返回 JSON 格式"""
        chain = self.explain_flow_prompt | self.non_stream_llm | StrOutputParser()
        
        result = chain.invoke({
            "code": code,
            "language": language
        })
        
        try:
            json_match = result
            if "```json" in result:
                json_match = result.split("```json")[1].split("```")[0]
            elif "```" in result:
                json_match = result.split("```")[1].split("```")[0]
            
            parsed = json.loads(json_match.strip())
            return parsed
        except json.JSONDecodeError:
            lines = code.strip().split('\n')
            return [
                {"line": i + 1, "desc": f"第 {i + 1} 行代码执行中..."}
                for i in range(len(lines))
            ]
    
    async def evaluate_prompt_quality(
        self,
        user_prompt: str,
        target_task: str
    ) -> str:
        """提示词角斗场 - 评价学生 Prompt 质量"""
        messages = [
            SystemMessage(content=self.prompt_eval_system),
            HumanMessage(content=f"""请评价以下 Prompt 的质量：

【目标任务】
{target_task}

【学生写的 Prompt】
{user_prompt}

请给出详细的评分和改进建议。""")
        ]
        
        result = await self.non_stream_llm.ainvoke(messages)
        return result.content
    
    def reset_session(self, session_id: str):
        """重置会话"""
        key = self._get_session_key(session_id)
        if key in self.conversation_history:
            del self.conversation_history[key]
        if key in self.help_counts:
            del self.help_counts[key]


class ChatRequest(BaseModel):
    code: str
    error_message: str = ""
    language: str = "Python"
    session_id: str = "default"
    user_message: str = ""


class ExplainRequest(BaseModel):
    code: str
    language: str = "Python"


class PromptCheckRequest(BaseModel):
    user_prompt: str
    target_task: str = "让 AI 生成代码"


app = FastAPI(title="AI 编程思维导师服务")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mentor: Optional[AICodingMentor] = None


@app.on_event("startup")
async def startup_event():
    global mentor
    mentor = AICodingMentor()
    print("🚀 AI 编程思维导师服务已启动")


@app.post("/api/mentor/chat")
async def chat_with_mentor(request: ChatRequest):
    """苏格拉底式对话 - 流式响应"""
    if not mentor:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "服务未初始化"}
        )
    
    async def generate():
        async for chunk in mentor.guide_debug(
            student_code=request.code,
            error_message=request.error_message,
            language=request.language,
            session_id=request.session_id,
            user_message=request.user_message
        ):
            yield chunk
    
    return StreamingResponse(
        generate(),
        media_type="text/plain; charset=utf-8"
    )


@app.post("/api/mentor/explain")
async def explain_code(request: ExplainRequest):
    """代码故事化讲解"""
    if not mentor:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "服务未初始化"}
        )
    
    try:
        result = await mentor.explain_flow_visually(
            code=request.code,
            language=request.language
        )
        return JSONResponse(
            content={"status": "success", "data": result}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )


@app.post("/api/mentor/prompt_check")
async def check_prompt(request: PromptCheckRequest):
    """提示词质量评价"""
    if not mentor:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "服务未初始化"}
        )
    
    try:
        result = await mentor.evaluate_prompt_quality(
            user_prompt=request.user_prompt,
            target_task=request.target_task
        )
        return JSONResponse(
            content={"status": "success", "data": result}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": str(e)}
        )


@app.post("/api/mentor/reset")
async def reset_session(request: Request):
    """重置会话"""
    if not mentor:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "服务未初始化"}
        )
    
    data = await request.json()
    session_id = data.get("session_id", "default")
    mentor.reset_session(session_id)
    return JSONResponse(
        content={"status": "success", "message": "会话已重置"}
    )


@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "AI 编程思维导师服务运行中..."}


@app.post("/review_code")
async def review_code_legacy(request: Request):
    """兼容旧版 API"""
    form = await request.form()
    
    code = form.get("code", "")
    question = form.get("question", "请帮我分析这段代码")
    
    if not code:
        return JSONResponse(
            status_code=400,
            content={"status": "error", "message": "请提供代码内容"}
        )
    
    if not mentor:
        return JSONResponse(
            status_code=500,
            content={"status": "error", "message": "服务未初始化"}
        )
    
    result = ""
    async for chunk in mentor.guide_debug(
        student_code=code,
        error_message="",
        language="Python",
        session_id="legacy",
        user_message=question
    ):
        result += chunk
    
    return JSONResponse(
        content={"status": "success", "data": result}
    )


if __name__ == "__main__":
    import uvicorn
    print("🚀 启动 AI 编程思维导师服务: http://0.0.0.0:5004")
    uvicorn.run(app, host="0.0.0.0", port=5004)
