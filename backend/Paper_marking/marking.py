import base64
import os
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from docx import Document
import dashscope
from dashscope import MultiModalConversation

# 加载环境变量
dotenv.load_dotenv()

app = Flask(__name__)
# 允许所有跨域请求
CORS(app, resources={r"/*": {"origins": "*"}})

# 从环境变量读取API配置
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

if not dashscope.api_key:
    raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")

def extract_text_from_docx(file_stream):
    """
    直接从内存流中读取 Word 文档内容
    """
    try:
        document = Document(file_stream)
        text = [p.text for p in document.paragraphs if p.text.strip()]
        return '\n'.join(text)
    except Exception as e:
        print(f"Word解析失败: {str(e)}")
        return ""

def get_image_data_uri(file_storage):
    """
    将上传的图片文件流直接转换为 Base64 Data URI
    """
    # 读取文件字节流
    img_bytes = file_storage.read()
    
    # 转换为 Base64 字符串
    base64_str = base64.b64encode(img_bytes).decode('utf-8')
    
    # 获取文件扩展名 (默认 jpg)
    filename = file_storage.filename
    ext = filename.split('.')[-1].lower() if '.' in filename else 'jpeg'
    if ext == 'jpg': ext = 'jpeg'
    
    # 拼接标准的 Data URI 格式
    # 例如: data:image/jpeg;base64,......
    return f"data:image/{ext};base64,{base64_str}"

def call_qwen_vl_ocr(image_data_uri, standard_answer_text):
    """
    调用通义千问VL-OCR模型
    """
    # 优化后的 Prompt：专门增强了对选择题的识别能力
    prompt_text = f"""
    你是一位拥有 10 年经验的资深教育专家，阅卷无数。
    
    【⚠️ 安全检查】
    如果图片全黑或无法读取，返回 "Error: 图片异常"。

    【任务目标】
    结合【学生作答图片】与【标准答案】，输出 Markdown 格式批改报告。
    **注意：试卷中混合了“选择题”和“主观题”，请务必全部批改，不要遗漏选择题！**
    
    【标准答案】
    {standard_answer_text}
    
    【🔥 核心指令：如何精准识别答案】
    1. **针对选择题（关键步骤）**：
       - 请像鹰眼一样扫描**题号旁边**、**题干末尾的括号 ( )** 或 **下划线 __** 区域。
       - **寻找手写的单个英文字母（A、B、C、D）**。
       - 即使手写字母很小、连笔或被涂改，只要能辨认，就必须提取出来。
       - 如果学生没有写字母，而是**在选项上打钩 (√) 或画圈**，请推断其选择的选项字母。
       - **绝不要**直接返回“无”，除非该题区域一片空白。
       
    2. **针对主观题**：
       - 识别大段手写文字，提取核心语义与标准答案的采分点进行比对。

    【强制输出格式】
    # 📝 智能批改报告

    ## 📊 成绩看板
    | 维度 | 数据 | 备注 |
    | :--- | :--- | :--- |
    | **预估得分** | [得分] / [总分] | 请根据题目数量合理分配分值（如选择题每题3-5分） |
    | **正确题数** | [正确数] / [总题数] | 务必统计所有题目 |
    | **掌握程度** | [S/A/B/C/D] | - |

    ## 🔍 逐题精批
    *(请严格按题号顺序排列，必须包含第1题、第2题...)*

    ### 第 [x] 题
    - **状态**：[✅ / ❌ / ⚠️]
    - **学生作答**：[OCR识别出的字母(如"A") 或 文字内容]
    - **标准答案**：[正确答案]
    - **点评**：[简短评价。如果是选择题，请简述正确选项的含义；如果是错题，指出学生选错项的含义]

    ---

    ## 💡 深度学习建议
    1. **薄弱点**：[具体知识点]
    2. **策略**：[具体建议]
    """

    messages = [
        {
            "role": "user",
            "content": [
                {"image": image_data_uri},
                {"text": prompt_text}
            ]
        }
    ]

    try:
        print("DEBUG: 正在发送请求给 Qwen-VL (已优化选择题Prompt)...")
        response = dashscope.MultiModalConversation.call(
            model='qwen-vl-ocr-latest', 
            messages=messages,
        )
        
        if response.status_code == 200:
            if "choices" in response.output and len(response.output.choices) > 0:
                content = response.output.choices[0].message.content
                if isinstance(content, list):
                    return content[0]['text']
                return str(content)
            else:
                return "模型未返回有效结果。"
        else:
            print(f"API Error: {response.code} - {response.message}")
            return f"批改失败: 服务端错误 {response.message}"
            
    except Exception as e:
        print(f"Exception: {str(e)}")
        return f"系统内部错误: {str(e)}"
@app.route('/correct', methods=['POST'])
def correct():
    try:
        # 1. 验证文件
        if 'standard_answer' not in request.files or 'student_answer' not in request.files:
            return "缺少必要的文件", 400

        standard_file = request.files['standard_answer']
        student_file = request.files['student_answer']

        # 2. 内存读取 Word (不再保存临时文件)
        standard_text = extract_text_from_docx(standard_file)
        if not standard_text:
            return "无法读取标准答案内容，请检查Word文件。", 400

        # 3. 内存处理图片转 Base64 (彻底解决路径问题)
        try:
            image_uri = get_image_data_uri(student_file)
        except Exception as e:
            return f"图片处理失败: {str(e)}", 400

        # 4. 调用模型
        result = call_qwen_vl_ocr(image_uri, standard_text)

        return result

    except Exception as e:
        print(f"Critical Error: {str(e)}")
        return f"服务器处理异常: {str(e)}", 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "Service is running (Memory Mode)"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)