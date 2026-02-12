import os
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 加载环境变量
dotenv.load_dotenv()

# ================= 1. 初始化 Flask 应用 =================
app = Flask(__name__)
# 允许跨域，方便前端（Vue等）调用
CORS(app, resources={r"/*": {"origins": "*"}})

# ================= 2. 配置大模型 (通义千问) =================
# 从环境变量读取API配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
ALI_MODEL_NAME = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not DASHSCOPE_API_KEY:
    raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")

# 初始化模型
chatLLM = ChatTongyi(
    dashscope_api_key=DASHSCOPE_API_KEY,
    model=ALI_MODEL_NAME,
    temperature=0,  # 低温度保证代码生成的准确性
    streaming=False   # 简单起见，暂不使用流式输出
)

# ================= 3. 定义提示词模板 (Prompt) =================
# 定义 System Prompt：设定 AI 为高级代码审查专家
system_template = """你是一位拥有10年经验的高级软件架构师和代码审查专家。
你的任务是根据用户提供的【代码内容】和【具体问题】，提供专业的代码审查、修复和解释。

请严格按照以下 Markdown 格式输出回复，不要输出其他无关的开场白：

## 🧐 问题分析
简要分析用户代码存在的问题、错误原因或逻辑漏洞。

## 🛠️ 代码修正
```python
(在这里提供完整的、修复后的代码，如果是其他语言请修改语言标签)
💡 关键修改说明
修正点 1: 解释为什么这样改...

修正点 2: 解释为什么这样改...

🚀 优化建议
提供 1-2 条关于性能、安全性或代码规范的额外建议。 """

code_review_prompt = ChatPromptTemplate.from_messages([ ("system", system_template), ("human", """ 【用户问题】：{user_question}

【用户代码】：
{code_content}
""")
])

# 使用 LCEL (LangChain Expression Language) 构建处理链
# 数据流向：Prompt -> LLM -> String Output
review_chain = code_review_prompt | chatLLM | StrOutputParser()

# ================= 4. 辅助函数 =================
def read_file_content(file_obj): 
    """读取上传的文件内容，自动处理 UTF-8 和 GBK 编码""" 
    content = file_obj.read() 
    try: 
        return content.decode('utf-8') 
    except UnicodeDecodeError: 
        try: 
            return content.decode('gbk') 
        except UnicodeDecodeError: 
            return None

# ================= 5. API 路由定义 =================
@app.route('/review_code', methods=['POST'])
def review_code():
    try:
        # 1. 获取用户问题
        user_question = request.form.get('question', '')
        
        # 2. 获取代码内容
        code_content = ""
        # 检查是否有文件上传
        if 'file' in request.files and request.files['file'].filename != '':
            uploaded_file = request.files['file']
            file_content = read_file_content(uploaded_file)
            
            if file_content is None:
                return jsonify({"status": "error", "message": "文件编码无法识别，请上传 UTF-8 格式文件"}), 400
            
            code_content = file_content
            
        # 如果没有文件，检查 code 字段
        elif 'code' in request.form and request.form['code'].strip() != '':
            code_content = request.form['code']
            
        else:
            return jsonify({"status": "error", "message": "请上传代码文件或粘贴代码内容"}), 400

        # 如果用户没写问题，设置默认问题
        if not user_question:
            user_question = "请帮我找出这段代码的错误并进行优化。"

        result = review_chain.invoke({
            "user_question": user_question,
            "code_content": code_content
        })

        # 4. 返回结果
        return jsonify({
            "status": "success",
            "data": result 
        })

    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"status": "error", "message": f"服务处理异常: {str(e)}"}), 500
@app.route('/health', methods=['GET']) 
def health_check(): 
    return jsonify({"status": "ok", "message": "Code Review API is running..."})

if __name__ == '__main__': 
    print("启动代码批改服务: http://0.0.0.0:5004") 
    app.run(host='0.0.0.0', port=5004, debug=True)