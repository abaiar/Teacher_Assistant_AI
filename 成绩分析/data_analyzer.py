import os
import dotenv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# 加载环境变量
dotenv.load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY1")
os.environ['OPENAI_BASE_URL'] = os.getenv("OPENAI_BASE_URL")

# 创建Flask应用
app = Flask(__name__)
CORS(app)  # 允许跨域请求

class StudentDataAnalyzer:
    def __init__(self):
        """初始化分析器"""
        self.chat_model = ChatOpenAI(model="gpt-4o-mini")
        # 设置中文字体支持（Windows系统）
        plt.rcParams['font.sans-serif'] = ['Microsoft YaHei', 'SimHei', 'DejaVu Sans']
        plt.rcParams['axes.unicode_minus'] = False
        self.df = None
        self.students_data = {}
    
    def get_student_names(self):
        """获取所有学生姓名"""
        if self.df is None:
            return []
        return self.df['姓名'].unique().tolist()
    
    def get_student_data(self, student_name):
        """获取单个学生的数据"""
        if self.df is None:
            return None
        student_data = self.df[self.df['姓名'] == student_name]
        if student_data.empty:
            return None
        return student_data.to_dict(orient='records')[0]
    
    def analyze_all_students(self):
        """分析所有学生成绩"""
        if self.df is None:
            return {}
        
        analysis_results = {}
        students = self.get_student_names()
        
        for student in students:
            # 分析单个学生成绩
            student_data = self.df[self.df['姓名'] == student]
            if len(student_data) < 2:
                analysis_results[student] = "需要至少两次考试数据来分析趋势"
                continue
            
            # 计算成绩趋势
            subjects = [col for col in self.df.columns if col not in ['姓名', '考试类型', '兴趣爱好', '考试序号']]
            trends = {}
            current_scores = {}
            
            for subject in subjects:
                if subject in student_data.columns:
                    scores = student_data[subject].tolist()
                    if len(scores) >= 2:
                        change = scores[-1] - scores[0]
                        trend = "进步" if change > 0 else "退步" if change < 0 else "稳定"
                        trends[subject] = f"{trend} ({scores[0]} → {scores[-1]})"
                        current_scores[subject] = scores[-1]
            
            # 获取兴趣
            interests = student_data['兴趣爱好'].iloc[0] if '兴趣爱好' in student_data.columns else '未记录'
            
            # 准备分析结果
            student_analysis = {
                "current_scores": current_scores,
                "trends": trends,
                "interests": interests
            }
            
            analysis_results[student] = student_analysis
        
        return analysis_results
    
    def input_student_data(self):
        """让用户输入学生数据"""
        print("\n📝 请输入学生数据")
        print("=" * 25," 分割线 ","=" * 25)
        
        students_data = []
        
        while True:
            print(f"\n--- 输入第 {len(students_data) + 1} 个学生的数据 ---")
            
            # 输入学生基本信息
            name = input("学生姓名: ").strip()
            if not name:
                print("❌ 姓名不能为空，请重新输入")
                continue
            
            exam_type = input("考试类型(如:期中/期末/月考): ").strip()
            if not exam_type:
                print("❌ 考试类型不能为空，请重新输入")
                continue
            
            # 输入各科成绩
            print("\n请输入各科成绩(直接回车跳过该科目):")
            scores = {}
            
            subjects = ['语文', '数学', '英语', '物理', '化学', '生物']
            for subject in subjects:
                score_input = input(f"{subject}成绩: ").strip()
                if score_input:
                    try:
                        scores[subject] = int(score_input)
                    except ValueError:
                        print(f"❌ {subject}成绩输入无效，跳过该科目")
            
            if not scores:
                print("❌ 至少需要输入一门科目的成绩")
                continue
            
            # 输入兴趣爱好
            interests = input("兴趣爱好: ").strip()
            
            # 创建学生数据记录
            student_record = {
                '姓名': name,
                '考试类型': exam_type,
                '兴趣爱好': interests if interests else '未填写'
            }
            student_record.update(scores)  # 将成绩添加到记录中
            
            students_data.append(student_record)
            
            # 询问是否继续输入
            continue_input = input("\n是否继续输入下一个学生? (y/n): ").strip().lower()
            if continue_input not in ['y', 'yes', '是']:
                break
        
        # 转换为DataFrame
        df = pd.DataFrame(students_data)
        print(f"\n✅ 成功输入 {len(df)} 条学生记录")
        return df
    
    def input_single_student_multiple_exams(self):
        """输入单个学生的多次考试数据"""
        print("\n📝 输入单个学生的多次考试数据（用于分析成绩趋势）")
        print("=" * 50)
        
        name = input("学生姓名: ").strip()
        if not name:
            print("❌ 姓名不能为空")
            return None
        
        exams_data = []
        exam_count = 1
        
        while True:
            print(f"\n--- 输入第 {exam_count} 次考试数据 ---")
            
            exam_type = input("考试类型(如:期中/期末/月考): ").strip()
            if not exam_type:
                print("❌ 考试类型不能为空")
                continue
            
            # 输入各科成绩
            print("\n请输入各科成绩(直接回车跳过该科目):")
            scores = {}
            
            subjects = ['语文', '数学', '英语', '物理', '化学', '生物']
            for subject in subjects:
                score_input = input(f"{subject}成绩: ").strip()
                if score_input:
                    try:
                        scores[subject] = int(score_input)
                    except ValueError:
                        print(f"❌ {subject}成绩输入无效，跳过该科目")
            
            if not scores:
                print("❌ 至少需要输入一门科目的成绩")
                continue
            
            # 创建考试记录
            exam_record = {
                '姓名': name,
                '考试类型': exam_type,
                '考试序号': exam_count
            }
            exam_record.update(scores)
            
            exams_data.append(exam_record)
            exam_count += 1
            
            # 询问是否继续输入
            continue_input = input("\n是否继续输入下一次考试? (y/n): ").strip().lower()
            if continue_input not in ['y', 'yes', '是']:
                break
        
        if len(exams_data) < 2:
            print("❌ 需要至少两次考试数据来分析趋势")
            return None
        
        # 输入兴趣爱好（只需要一次）
        interests = input("\n学生的兴趣爱好: ").strip()
        for record in exams_data:
            record['兴趣爱好'] = interests if interests else '未填写'
        
        df = pd.DataFrame(exams_data)
        print(f"\n✅ 成功输入 {name} 的 {len(df)} 次考试记录")
        return df
    
    def load_data_from_csv(self, file_path):
        """从CSV文件加载数据"""
        try:
            self.df = pd.read_csv(file_path)
            print(f"✅ 成功加载数据，共 {len(self.df)} 条记录")
            return True
        except FileNotFoundError:
            print(f"❌ 文件不存在: {file_path}")
            return False
        except Exception as e:
            print(f"❌ 读取文件失败: {e}")
            return False
    
    def analyze_student_grades(self, df, student_name):
        """分析学生成绩"""
        student_data = df[df['姓名'] == student_name]
        
        # 支持单条记录
        if len(student_data) < 2:
            # 只有一次考试数据，直接分析当前成绩
            pass
        
        # 计算成绩趋势
        subjects = [col for col in df.columns if col not in ['姓名', '考试类型', '兴趣爱好', '考试序号']]
        trends = {}
        current_scores = {}
        
        for subject in subjects:
            if subject in student_data.columns:
                scores = student_data[subject].tolist()
                if len(scores) >= 2:
                    change = scores[-1] - scores[0]
                    trend = "进步" if change > 0 else "退步" if change < 0 else "稳定"
                    trends[subject] = f"{trend} ({scores[0]} → {scores[-1]})"
                    current_scores[subject] = scores[-1]
        
        # 获取兴趣
        interests = student_data['兴趣爱好'].iloc[0] if '兴趣爱好' in student_data.columns else '未记录'
        
        # 准备分析消息
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
    
    def generate_student_charts(self, df, student_name, output_folder="charts"):
        """为学生生成学习图表"""
        try:
            student_data = df[df['姓名'] == student_name]
            
            if len(student_data) < 2:
                print(f"⚠️  {student_name} 的数据不足，无法生成趋势图表")
                return None
            
            # 创建输出文件夹
            if not os.path.exists(output_folder):
                os.makedirs(output_folder)
            
            # 获取所有科目（排除非成绩列）
            exclude_columns = ['姓名', '考试类型', '兴趣爱好', '考试序号']
            subjects = [col for col in df.columns if col not in exclude_columns]
            
            # 1. 成绩趋势折线图（各科目变化）
            self._create_trend_line_chart(student_data, student_name, subjects, output_folder)
            
            # 2. 各科目成绩对比柱状图
            self._create_subject_bar_chart(student_data, student_name, subjects, output_folder)
            
            # 3. 进步/退步分析图
            self._create_progress_chart(student_data, student_name, subjects, output_folder)
            
            # 4. 最新考试科目成绩雷达图
            self._create_radar_chart(student_data, student_name, subjects, output_folder)
            
            print(f"\n📊 已为 {student_name} 生成4张学习图表，保存在 '{output_folder}' 文件夹中")
            return True
            
        except Exception as e:
            print(f"❌ 生成图表时出错: {e}")
            return False
    
    def _create_trend_line_chart(self, student_data, student_name, subjects, output_folder):
        """创建成绩趋势折线图"""
        plt.figure(figsize=(12, 6))
        
        # 准备考试顺序（如果有序号就用序号，否则用考试类型）
        if '考试序号' in student_data.columns:
            exam_order = student_data['考试序号'].tolist()
            x_labels = [f"第{num}次" for num in exam_order]
        else:
            x_labels = student_data['考试类型'].tolist()
        
        # 为每个科目绘制折线
        for subject in subjects:
            if subject in student_data.columns:
                scores = student_data[subject].tolist()
                if len(scores) >= 2:
                    plt.plot(range(len(scores)), scores, marker='o', linewidth=2, label=subject)
        
        plt.title(f'{student_name} 各科成绩变化趋势', fontsize=16, fontweight='bold')
        plt.xlabel('考试次数', fontsize=12)
        plt.ylabel('分数', fontsize=12)
        plt.xticks(range(len(x_labels)), x_labels, rotation=45)
        plt.ylim(0, 105)  # 设置Y轴范围
        plt.grid(True, alpha=0.3)
        plt.legend(loc='best')
        plt.tight_layout()
        
        # 保存图表
        filename = os.path.join(output_folder, f'{student_name}_成绩趋势图.png')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✅ 已保存: {filename}")
    
    def _create_subject_bar_chart(self, student_data, student_name, subjects, output_folder):
        """创建各科目成绩对比柱状图"""
        if len(student_data) == 0:
            return
        
        # 使用最新一次考试的各科成绩
        latest_exam = student_data.iloc[-1]
        latest_scores = {}
        latest_subjects = []
        
        for subject in subjects:
            if subject in student_data.columns and not pd.isna(latest_exam[subject]):
                latest_scores[subject] = latest_exam[subject]
                latest_subjects.append(subject)
        
        if not latest_scores:
            return
        
        plt.figure(figsize=(10, 6))
        colors = plt.cm.Set3(np.linspace(0, 1, len(latest_subjects)))
        
        bars = plt.bar(latest_subjects, [latest_scores[sub] for sub in latest_subjects], 
                      color=colors, edgecolor='black', linewidth=1.2)
        
        # 在柱子上显示分数
        for bar, score in zip(bars, [latest_scores[sub] for sub in latest_subjects]):
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(score)}', ha='center', va='bottom', fontsize=10)
        
        plt.title(f'{student_name} 最新考试各科成绩', fontsize=16, fontweight='bold')
        plt.xlabel('科目', fontsize=12)
        plt.ylabel('分数', fontsize=12)
        plt.ylim(0, 105)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        filename = os.path.join(output_folder, f'{student_name}_科目成绩对比图.png')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✅ 已保存: {filename}")
    
    def _create_progress_chart(self, student_data, student_name, subjects, output_folder):
        """创建进步/退步分析图"""
        if len(student_data) < 2:
            return
        
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
            return
        
        plt.figure(figsize=(10, 6))
        
        # 根据进步/退步设置颜色
        colors = ['green' if x >= 0 else 'red' for x in progress_data]
        
        bars = plt.bar(progress_labels, progress_data, color=colors, 
                      edgecolor='black', linewidth=1.2, alpha=0.7)
        
        # 在柱子上显示变化值
        for bar, change in zip(bars, progress_data):
            height = bar.get_height()
            va = 'bottom' if change >= 0 else 'top'
            color = 'green' if change >= 0 else 'red'
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'+{change}' if change >= 0 else f'{change}',
                    ha='center', va=va, fontsize=10, fontweight='bold', color=color)
        
        plt.axhline(y=0, color='black', linewidth=0.8, linestyle='--')
        plt.title(f'{student_name} 各科成绩变化量（进步/退步）', fontsize=16, fontweight='bold')
        plt.xlabel('科目', fontsize=12)
        plt.ylabel('分数变化（期末-期中）', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        filename = os.path.join(output_folder, f'{student_name}_进步分析图.png')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✅ 已保存: {filename}")
    
    def _create_radar_chart(self, student_data, student_name, subjects, output_folder):
        """创建雷达图"""
        if len(student_data) == 0:
            return
        
        # 只使用有成绩的科目
        valid_subjects = []
        latest_scores = []
        
        for subject in subjects:
            if subject in student_data.columns:
                score = student_data.iloc[-1][subject]
                if not pd.isna(score):
                    valid_subjects.append(subject)
                    latest_scores.append(score)
        
        if len(valid_subjects) < 3:  # 雷达图至少需要3个科目
            return
        
        # 设置雷达图
        angles = np.linspace(0, 2 * np.pi, len(valid_subjects), endpoint=False).tolist()
        angles += angles[:1]  # 闭合图形
        scores = latest_scores + latest_scores[:1]
        
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, polar=True)
        
        ax.plot(angles, scores, 'o-', linewidth=2, color='blue', alpha=0.7)
        ax.fill(angles, scores, alpha=0.25, color='blue')
        
        # 设置角度标签
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(valid_subjects, fontsize=10)
        
        # 设置半径标签
        ax.set_yticks([20, 40, 60, 80, 100])
        ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=8)
        ax.set_ylim(0, 105)
        
        plt.title(f'{student_name} 各科能力雷达图', fontsize=16, fontweight='bold', pad=20)
        plt.tight_layout()
        
        filename = os.path.join(output_folder, f'{student_name}_能力雷达图.png')
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"  ✅ 已保存: {filename}")

def choose_data_input_method():
    """选择数据输入方式"""
    print("🎓 学生数据分析系统")
    print("=" * 50)
    print("请选择数据输入方式:")
    print("1. 📝 手动输入多个学生数据")
    print("2. 📊 输入单个学生的多次考试数据（推荐分析趋势）")
    print("3. 📁 从CSV文件加载数据")
    print("4. ❌ 退出程序")
    
    while True:
        choice = input("\n请选择 (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        else:
            print("❌ 请输入有效的选择 (1-4)")

def main():
    """主函数"""
    print("🎓 学生数据分析系统启动中...\n")
    
    try:
        # 初始化分析器
        analyzer = StudentDataAnalyzer()
        print("✅ 分析器初始化成功")
        
        # 选择数据输入方式
        choice = choose_data_input_method()
        
        if choice == '4':
            print("👋 再见！")
            return
        
        # 根据选择获取数据
        if choice == '1':
            df = analyzer.input_student_data()
        elif choice == '2':
            df = analyzer.input_single_student_multiple_exams()
        else:  # choice == '3'
            df = analyzer.load_data_from_csv()
        
        if df is None or len(df) == 0:
            print("❌ 没有有效数据，程序退出")
            return
        
        # 显示数据
        print("\n📊 输入的数据：")
        print(df.to_string(index=False))
        
        # 询问是否生成图表
        generate_charts = input("\n是否生成学习图表? (y/n): ").strip().lower()
        generate_charts_flag = generate_charts in ['y', 'yes', '是']
        
        # 分析学生
        students = df['姓名'].unique()
        
        print(f"\n🔍 开始分析 {len(students)} 名学生...")
        
        for student in students:
            print(f"\n{'='*50}")
            print(f"📋 正在分析学生: {student}")
            print(f"{'='*50}")
            
            # 成绩分析
            print("\n1. 📈 成绩分析报告：")
            analysis = analyzer.analyze_student_grades(df, student)
            print(analysis)
            
            # 学习计划
            print("\n2. 📝 短期学习计划：")
            short_plan = analyzer.create_study_plan(student, analysis, "短期(1-3个月)")
            print(short_plan)
            
            print("\n3. 🗓️ 长期学习计划：")
            long_plan = analyzer.create_study_plan(student, analysis, "长期(6-12个月)")
            print(long_plan)
            
            # 生涯规划
            student_data = df[df['姓名'] == student].iloc[0]
            subjects = [col for col in df.columns if col not in ['姓名', '考试类型', '兴趣爱好', '考试序号']]
            current_scores = {subject: student_data[subject] for subject in subjects if subject in student_data}
            interests = student_data.get('兴趣爱好', '未记录')
            
            print("\n4. 🎯 生涯规划建议：")
            career_advice = analyzer.provide_career_advice(student, current_scores, interests)
            print(career_advice)
            
            # 鼓励信息
            print("\n5. 💫 鼓励话语：")
            achievements = f"各科成绩良好，对{interests}有浓厚兴趣"
            encouragement = analyzer.encourage_student(student, achievements)
            print(encouragement)
            
            # 生成图表
            if generate_charts_flag:
                print("\n6. 📊 正在生成学习图表...")
                success = analyzer.generate_student_charts(df, student)
                if success:
                    print("  图表生成完成！")
            
            print(f"\n⭐ {student}的分析完成！")
            print("-" * 50)
        
        print("\n🎉 所有学生分析完成！")
        
        # 询问是否保存结果
        save_choice = input("\n是否保存分析结果到文件? (y/n): ").strip().lower()
        if save_choice in ['y', 'yes', '是']:
            filename = input("请输入文件名(不含后缀): ").strip()
            if filename:
                try:
                    with open(f"{filename}_analysis.txt", "w", encoding="utf-8") as f:
                        f.write("学生数据分析报告\n")
                        f.write("=" * 50 + "\n\n")
                        for student in students:
                            f.write(f"学生: {student}\n")
                            f.write("-" * 30 + "\n")
                            f.write(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                            f.write("说明：详细分析结果请查看生成的图表文件\n\n")
                    print(f"✅ 分析结果已保存到 {filename}_analysis.txt")
                except Exception as e:
                    print(f"❌ 保存文件失败: {e}")
        
    except Exception as e:
        print(f"❌ 系统运行出错: {e}")
        print("请检查：")
        print("1. .env文件中的API配置")
        print("2. 网络连接")
        print("3. 依赖包安装")

# 成绩分析API接口
@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        analyzer = StudentDataAnalyzer()
        
        # 检查请求类型
        if 'dataType' in request.form:
            data_type = request.form['dataType']
            
            if data_type == 'json':
                # 手动输入模式
                students_data = request.form.get('students')
                if not students_data:
                    return jsonify({'error': '缺少students数据'}), 400
                
                import json
                students = json.loads(students_data)
                
                # 转换为DataFrame
                df = pd.DataFrame(students)
                
            elif data_type == 'csv':
                # CSV上传模式
                if 'file' not in request.files:
                    return jsonify({'error': '缺少CSV文件'}), 400
                
                file = request.files['file']
                if file.filename == '':
                    return jsonify({'error': '未选择文件'}), 400
                
                # 读取CSV文件
                df = pd.read_csv(file)
                
            else:
                return jsonify({'error': '无效的数据类型'}), 400
        else:
            return jsonify({'error': '缺少dataType参数'}), 400
        
        # 分析每个学生
        analysis_results = []
        students = df['姓名'].unique()
        
        for student in students:
            # 成绩分析
            analysis = analyzer.analyze_student_grades(df, student)
            
            # 短期学习计划
            short_plan = analyzer.create_study_plan(student, analysis, "短期(1-3个月)")
            
            # 长期学习计划
            long_plan = analyzer.create_study_plan(student, analysis, "长期(6-12个月)")
            
            # 生涯规划
            student_data = df[df['姓名'] == student].iloc[0]
            subjects = [col for col in df.columns if col not in ['姓名', '考试类型', '兴趣爱好', '考试序号']]
            current_scores = {subject: student_data[subject] for subject in subjects if subject in student_data}
            interests = student_data.get('兴趣爱好', '未记录')
            career_advice = analyzer.provide_career_advice(student, current_scores, interests)
            
            # 鼓励话语
            encouragement = analyzer.encourage_student(student, f"各科成绩良好，对{interests}有浓厚兴趣")
            
            # 添加到结果列表
            analysis_results.append({
                'name': student,
                'analysis': analysis,
                'shortPlan': short_plan,
                'longPlan': long_plan,
                'careerAdvice': career_advice,
                'encouragement': encouragement
            })
        
        return jsonify(analysis_results), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 测试接口
@app.route('/test', methods=['GET'])
def test():
    return jsonify({'message': '成绩分析API正在运行'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)


