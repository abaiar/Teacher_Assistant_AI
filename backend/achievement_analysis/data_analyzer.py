import os
import io
import base64
import json
import dotenv
import pandas as pd
import numpy as np
import matplotlib
# 设置非交互式后端，防止在Web服务中出错
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_core.messages import HumanMessage, SystemMessage

# --- 修改点 1: 引入 dashscope 和 LangChain 的通义千问适配器 ---
import dashscope
from langchain_community.chat_models import ChatTongyi

# 加载环境变量
dotenv.load_dotenv()

# 配置 DashScope API Key
dashscope.api_key = os.getenv("DASHSCOPE_API_KEY")

# 创建Flask应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求

class StudentDataAnalyzer:
    def __init__(self):
        """初始化分析器"""
        # --- 修改点 2: 使用 ChatTongyi 初始化阿里云模型 ---
        # 确保已在环境变量中设置 DASHSCOPE_API_KEY，或者在此处显式传入
        api_key = os.getenv("DASHSCOPE_API_KEY")
        model_name = os.getenv("ALI_MODEL_NAME", "qwen-plus") # 默认使用 qwen-plus
        
        if not api_key:
            raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")

        # 初始化阿里云千问模型
        self.chat_model = ChatTongyi(
            model=model_name,
            api_key=api_key,
            temperature=0.7
            # 如果需要启用搜索功能，可以添加: enable_search=True
        )
        # ----------------------------------------------------

        # 设置中文字体支持
        # 尝试多种常见中文字体，兼容不同系统
        plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'PingFang SC', 'WenQuanYi Micro Hei', 'sans-serif']
        plt.rcParams['axes.unicode_minus'] = False
        self.df = None
        self.students_data = {}
    
    def analyze_student_grades(self, df, student_name):
        """分析学生成绩"""
        student_data = df[df['姓名'] == student_name]
        
        # 计算成绩趋势
        subjects = [col for col in df.columns if col not in ['姓名', '考试类型', '兴趣爱好', '考试序号']]
        trends = {}
        current_scores = {}
        
        # 获取最新一次考试的成绩
        if len(student_data) > 0:
            latest_record = student_data.iloc[-1]
            for subject in subjects:
                if subject in student_data.columns and not pd.isna(latest_record[subject]):
                    current_scores[subject] = latest_record[subject]

        for subject in subjects:
            if subject in student_data.columns:
                scores = student_data[subject].dropna().tolist()
                if len(scores) >= 2:
                    change = scores[-1] - scores[0]
                    trend = "进步" if change > 0 else "退步" if change < 0 else "稳定"
                    trends[subject] = f"{trend} ({scores[0]} → {scores[-1]})"
        
        # 获取兴趣
        interests = '未记录'
        if '兴趣爱好' in student_data.columns and not student_data['兴趣爱好'].empty:
            interests = student_data['兴趣爱好'].iloc[0]
        
        # 准备分析消息
        # 注意：ChatTongyi 完美兼容 LangChain 的 Message 格式
        messages = [
            SystemMessage(content="你是一位专业的教育数据分析师，擅长分析学生成绩和提供学习建议"),
            HumanMessage(content=f"""
            请分析以下学生数据：

            学生姓名：{student_name}
            当前各科成绩：{current_scores}
            成绩变化趋势：{trends}
            兴趣爱好：{interests}

            请从以下方面进行分析：
            1. 优势科目和薄弱科目识别
            2. 学习进步情况评估
            3. 具体的学习改进建议
            4. 如何结合兴趣爱好提高学习效果

            用专业且鼓励的语气回复，字数在300字左右。
            """)
        ]
        
        response = self.chat_model.invoke(messages)
        return response.content
    
    def create_study_plan(self, student_name, analysis_result, time_frame):
        """创建学习计划"""
        messages = [
            SystemMessage(content="你是一位专业的学习规划师"),
            HumanMessage(content=f"""
            基于以下分析结果：
            {analysis_result}

            学生姓名：{student_name}
            计划类型：{time_frame}

            请制定具体可行的学习计划，包括：
            1. 明确的学习目标
            2. 详细的时间安排
            3. 有效的学习方法
            4. 预期的进步效果

            用鼓励和支持的语气，字数在250字左右。
            """)
        ]
        
        response = self.chat_model.invoke(messages)
        return response.content
    
    def provide_career_advice(self, student_name, scores, interests):
        """提供生涯规划建议"""
        messages = [
            SystemMessage(content="你是一位职业规划专家"),
            HumanMessage(content=f"""
            学生姓名：{student_name}
            各科成绩：{scores}
            兴趣爱好：{interests}

            请提供：
            1. 适合的大学专业方向
            2. 未来职业发展路径
            3. 需要培养的核心能力
            4. 具体的行动建议

            用启发性和鼓励性的语言，字数在250字左右。
            """)
        ]
        
        response = self.chat_model.invoke(messages)
        return response.content
    
    def encourage_student(self, student_name, achievements):
        """鼓励学生"""
        messages = [
            SystemMessage(content="你是一位充满热情的教育专家，擅长用温暖的语言鼓励学生"),
            HumanMessage(content=f"""
            请为学生{student_name}写一段鼓励的话。
            学生的特点：{achievements}

            要求：
            1. 真诚温暖，富有感染力
            2. 肯定学生的努力和进步
            3. 激发继续前进的动力
            4. 包含具体的赞美点

            字数在150字左右。
            """)
        ]
        
        response = self.chat_model.invoke(messages)
        return response.content

    def generate_charts_base64(self, df, student_name):
        """
        生成学生分析图表并返回Base64编码的图片列表
        """
        charts = {}
        try:
            student_data = df[df['姓名'] == student_name]
            if student_data.empty:
                return charts

            # 获取所有科目（排除非成绩列）
            exclude_columns = ['姓名', '考试类型', '兴趣爱好', '考试序号']
            subjects = [col for col in df.columns if col not in exclude_columns]
            
            # 1. 各科目成绩对比柱状图 (最新一次)
            img_bar = self._create_subject_bar_chart_base64(student_data, student_name, subjects)
            if img_bar:
                charts['bar_chart'] = img_bar
            
            # 2. 雷达图 (最新一次)
            img_radar = self._create_radar_chart_base64(student_data, student_name, subjects)
            if img_radar:
                charts['radar_chart'] = img_radar

            # 3. 趋势图 (如果有多次考试)
            if len(student_data) >= 2:
                img_trend = self._create_trend_line_chart_base64(student_data, student_name, subjects)
                if img_trend:
                    charts['trend_chart'] = img_trend
                
                img_progress = self._create_progress_chart_base64(student_data, student_name, subjects)
                if img_progress:
                    charts['progress_chart'] = img_progress

            return charts
            
        except Exception as e:
            print(f"❌ 生成图表时出错: {e}")
            return charts

    def _fig_to_base64(self):
        """辅助函数：将当前Matplotlib图表转换为Base64字符串"""
        buf = io.BytesIO()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        img_str = base64.b64encode(buf.read()).decode('utf-8')
        plt.close()
        return img_str

    def _create_subject_bar_chart_base64(self, student_data, student_name, subjects):
        latest_exam = student_data.iloc[-1]
        latest_scores = {}
        latest_subjects = []
        
        for subject in subjects:
            if subject in student_data.columns and not pd.isna(latest_exam[subject]):
                latest_scores[subject] = latest_exam[subject]
                latest_subjects.append(subject)
        
        if not latest_scores:
            return None
        
        plt.figure(figsize=(8, 5))
        colors = plt.cm.Set3(np.linspace(0, 1, len(latest_subjects)))
        bars = plt.bar(latest_subjects, [latest_scores[sub] for sub in latest_subjects], 
                      color=colors, edgecolor='black', linewidth=1.0)
        
        for bar, score in zip(bars, [latest_scores[sub] for sub in latest_subjects]):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(score)}', ha='center', va='bottom', fontsize=9)
        
        plt.title(f'{student_name} 最新成绩', fontsize=14, fontweight='bold')
        plt.ylabel('分数')
        plt.ylim(0, 110)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        return self._fig_to_base64()

    def _create_radar_chart_base64(self, student_data, student_name, subjects):
        valid_subjects = []
        latest_scores = []
        for subject in subjects:
            if subject in student_data.columns:
                score = student_data.iloc[-1][subject]
                if not pd.isna(score):
                    valid_subjects.append(subject)
                    latest_scores.append(score)
        
        if len(valid_subjects) < 3:
            return None
        
        angles = np.linspace(0, 2 * np.pi, len(valid_subjects), endpoint=False).tolist()
        angles += angles[:1]
        scores = latest_scores + latest_scores[:1]
        
        fig = plt.figure(figsize=(6, 6))
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, scores, 'o-', linewidth=2, color='#9370DB')
        ax.fill(angles, scores, alpha=0.25, color='#9370DB')
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(valid_subjects, fontsize=10)
        ax.set_ylim(0, 105)
        plt.title(f'{student_name} 能力雷达图', fontsize=14, fontweight='bold', pad=20)
        plt.tight_layout()
        return self._fig_to_base64()

    def _create_trend_line_chart_base64(self, student_data, student_name, subjects):
        plt.figure(figsize=(10, 5))
        if '考试序号' in student_data.columns:
            x_labels = [f"第{num}次" for num in student_data['考试序号']]
        else:
            x_labels = student_data['考试类型'].tolist()
        
        for subject in subjects:
            if subject in student_data.columns:
                scores = student_data[subject].tolist()
                if len(scores) >= 2:
                    plt.plot(range(len(scores)), scores, marker='o', label=subject)
        
        plt.title(f'{student_name} 成绩趋势', fontsize=14)
        plt.xticks(range(len(x_labels)), x_labels)
        plt.legend(loc='best')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        return self._fig_to_base64()

    def _create_progress_chart_base64(self, student_data, student_name, subjects):
        progress_data = []
        progress_labels = []
        for subject in subjects:
            if subject in student_data.columns:
                scores = student_data[subject].tolist()
                if len(scores) >= 2:
                    progress = scores[-1] - scores[0]
                    progress_data.append(progress)
                    progress_labels.append(subject)
        
        if not progress_data:
            return None
            
        plt.figure(figsize=(8, 5))
        colors = ['green' if x >= 0 else 'red' for x in progress_data]
        bars = plt.bar(progress_labels, progress_data, color=colors, alpha=0.7)
        for bar, change in zip(bars, progress_data):
            height = bar.get_height()
            va = 'bottom' if change >= 0 else 'top'
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{change:+d}', ha='center', va=va)
        plt.axhline(0, color='black', linewidth=0.8)
        plt.title(f'{student_name} 进步/退步情况', fontsize=14)
        plt.tight_layout()
        return self._fig_to_base64()

# 成绩分析API接口
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        analyzer = StudentDataAnalyzer()
        df = None
        
        # 检查请求类型
        if 'dataType' in request.form:
            data_type = request.form['dataType']
            
            if data_type == 'json':
                # 手动输入模式
                students_json = request.form.get('students')
                if not students_json:
                    return jsonify({'error': '缺少students数据'}), 400
                
                try:
                    raw_students = json.loads(students_json)
                    processed_data = []
                    for s in raw_students:
                        record = {
                            '姓名': s.get('name'),
                            '考试类型': s.get('examType'),
                            '兴趣爱好': s.get('interests', '未记录')
                        }
                        if 'scores' in s and isinstance(s['scores'], dict):
                            scores = {k: float(v) for k, v in s['scores'].items() if v is not None and v != ''}
                            record.update(scores)
                        processed_data.append(record)
                    
                    df = pd.DataFrame(processed_data)
                    
                except Exception as e:
                    return jsonify({'error': f'JSON数据解析失败: {str(e)}'}), 400
                
            elif data_type == 'csv':
                # CSV上传模式
                if 'file' not in request.files:
                    return jsonify({'error': '缺少CSV文件'}), 400
                
                file = request.files['file']
                if file.filename == '':
                    return jsonify({'error': '未选择文件'}), 400
                
                try:
                    df = pd.read_csv(file)
                except Exception as e:
                    return jsonify({'error': f'CSV读取失败: {str(e)}'}), 400
            else:
                return jsonify({'error': '无效的数据类型'}), 400
        else:
            return jsonify({'error': '缺少dataType参数'}), 400
        
        if df is None or df.empty:
            return jsonify({'error': '没有有效的数据'}), 400

        cols_to_ignore = ['姓名', '考试类型', '兴趣爱好', '考试序号']
        for col in df.columns:
            if col not in cols_to_ignore:
                df[col] = pd.to_numeric(df[col], errors='coerce')

        analysis_results = []
        students = df['姓名'].unique()
        
        for student in students:
            # 成绩分析
            analysis = analyzer.analyze_student_grades(df, student)
            
            # 学习计划
            short_plan = analyzer.create_study_plan(student, analysis, "短期(1-3个月)")
            long_plan = analyzer.create_study_plan(student, analysis, "长期(6-12个月)")
            
            # 生涯规划
            student_data = df[df['姓名'] == student].iloc[0]
            subjects = [col for col in df.columns if col not in cols_to_ignore]
            current_scores = {subject: student_data[subject] for subject in subjects if subject in student_data and not pd.isna(student_data[subject])}
            interests = str(student_data.get('兴趣爱好', '未记录'))
            career_advice = analyzer.provide_career_advice(student, current_scores, interests)
            
            # 鼓励话语
            encouragement = analyzer.encourage_student(student, f"各科成绩良好，对{interests}有浓厚兴趣")
            
            # 生成图表
            charts = analyzer.generate_charts_base64(df, student)
            
            analysis_results.append({
                'name': student,
                'analysis': analysis,
                'shortPlan': short_plan,
                'longPlan': long_plan,
                'careerAdvice': career_advice,
                'encouragement': encouragement,
                'charts': charts
            })
        
        return jsonify(analysis_results), 200
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': f'服务器内部错误: {str(e)}'}), 500

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': '成绩分析API正在运行 (模型: 阿里云 ChatTongyi)'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=False)