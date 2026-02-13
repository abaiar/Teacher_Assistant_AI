# -*- coding: utf-8 -*-
"""
Prompt Arena 核心服务模块

提供三个核心 AI 服务：
1. 出题服务 (QuestService): 生成多样化的任务场景
2. 模拟服务 (SimulationService): 模拟目标 AI 响应
3. 裁判服务 (JudgeService): 评估 AI 响应质量
"""

import os
import json
import random
import dotenv
from typing import Dict, List, Optional, Any
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_core.messages import HumanMessage, SystemMessage

dotenv.load_dotenv()

DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
ALI_MODEL_NAME = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not DASHSCOPE_API_KEY:
    raise ValueError("未找到 DASHSCOPE_API_KEY，请检查 .env 文件")

_MODEL = ChatTongyi(model=ALI_MODEL_NAME, streaming=False, api_key=DASHSCOPE_API_KEY)


QUEST_TEMPLATES = [
    {
        "category": "创意写作",
        "scenarios": [
            "让 AI 写一首关于春天的现代诗",
            "让 AI 创作一个科幻微小说的开头",
            "让 AI 写一段产品广告文案",
            "让 AI 编写一个童话故事的开头",
            "让 AI 写一首藏头诗"
        ],
        "constraints": [
            "字数限制在100字以内",
            "必须包含至少3个形容词",
            "风格要幽默诙谐",
            "不能使用常见的陈词滥调",
            "必须包含一个转折"
        ]
    },
    {
        "category": "知识解释",
        "scenarios": [
            "让 AI 向小学生解释什么是光合作用",
            "让 AI 用类比的方式解释机器学习",
            "让 AI 解释量子纠缠现象",
            "让 AI 解释区块链的工作原理",
            "让 AI 解释相对论的基本概念"
        ],
        "constraints": [
            "使用通俗易懂的语言",
            "必须包含至少一个生活化的例子",
            "避免使用专业术语",
            "解释要生动有趣",
            "字数控制在200字以内"
        ]
    },
    {
        "category": "代码生成",
        "scenarios": [
            "让 AI 写一个 Python 函数实现冒泡排序",
            "让 AI 写一个 JavaScript 函数验证邮箱格式",
            "让 AI 写一个 SQL 查询语句",
            "让 AI 写一个正则表达式匹配手机号",
            "让 AI 写一个简单的 HTML 页面结构"
        ],
        "constraints": [
            "代码必须有注释",
            "要处理边界情况",
            "代码风格要规范",
            "必须包含错误处理",
            "要考虑性能优化"
        ]
    },
    {
        "category": "逻辑推理",
        "scenarios": [
            "让 AI 分析一个商业案例的利弊",
            "让 AI 推理一个逻辑谜题",
            "让 AI 分析某个决策的潜在风险",
            "让 AI 比较两种技术方案的优劣",
            "让 AI 预测某个趋势的发展"
        ],
        "constraints": [
            "必须给出明确的推理步骤",
            "要考虑多个角度",
            "结论要有数据支撑",
            "要指出潜在的假设",
            "要提供反向思考"
        ]
    },
    {
        "category": "角色扮演",
        "scenarios": [
            "让 AI 扮演一位历史人物回答问题",
            "让 AI 扮演一位职业顾问给出建议",
            "让 AI 扮演一位心理咨询师进行对话",
            "让 AI 扮演一位教师讲解知识点",
            "让 AI 扮演一位产品经理分析需求"
        ],
        "constraints": [
            "语气要符合角色特点",
            "回答要专业且有深度",
            "要体现角色的知识背景",
            "要使用角色特有的表达方式",
            "要保持角色的一致性"
        ]
    }
]


class QuestService:
    """出题服务：生成多样化的任务场景"""
    
    @staticmethod
    def generate_quest() -> Dict[str, Any]:
        """
        生成一个完整的题目
        
        Returns:
            包含场景描述、任务目标、限制条件的字典
        """
        template = random.choice(QUEST_TEMPLATES)
        scenario = random.choice(template["scenarios"])
        constraints = random.sample(
            template["constraints"], 
            min(2, len(template["constraints"]))
        )
        
        quest_id = f"quest_{random.randint(1000, 9999)}"
        
        return {
            "quest_id": quest_id,
            "category": template["category"],
            "scenario": scenario,
            "objective": f"编写一个高质量的提示词，{scenario}",
            "constraints": constraints,
            "difficulty": random.choice(["简单", "中等", "困难"]),
            "tips": [
                "明确指出 AI 需要扮演的角色",
                "提供具体的输出格式要求",
                "给出示例可以帮助 AI 更好理解"
            ]
        }
    
    @staticmethod
    def generate_quest_with_ai() -> Dict[str, Any]:
        """
        使用 AI 生成更丰富的题目
        
        Returns:
            AI 生成的题目内容
        """
        system_prompt = """你是一个专业的提示词训练题目设计专家。
请生成一个用于训练用户提示词编写能力的题目。

题目应该包含：
1. 场景描述：用户需要让 AI 完成的具体任务
2. 任务目标：明确说明提示词需要达成的效果
3. 限制条件：2-3个具体的限制要求
4. 评分维度：列出3个评分标准

请以 JSON 格式返回，格式如下：
{
    "category": "题目类别",
    "scenario": "场景描述",
    "objective": "任务目标",
    "constraints": ["限制1", "限制2"],
    "scoring_dimensions": ["维度1", "维度2", "维度3"],
    "difficulty": "难度等级"
}"""

        try:
            response = _MODEL.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content="请生成一个有创意的提示词训练题目，主题随机选择。")
            ])
            
            content = response.content
            
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                quest_data = json.loads(json_str)
                quest_data["quest_id"] = f"quest_ai_{random.randint(1000, 9999)}"
                return quest_data
            else:
                return QuestService.generate_quest()
                
        except Exception as e:
            print(f"AI 生成题目失败: {str(e)}")
            return QuestService.generate_quest()


class SimulationService:
    """模拟服务：模拟目标 AI 响应"""
    
    @staticmethod
    def simulate_response(user_prompt: str, quest_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        模拟 AI 对用户提示词的响应
        
        Args:
            user_prompt: 用户编写的提示词
            quest_context: 题目上下文信息
            
        Returns:
            模拟的 AI 响应结果
        """
        system_prompt = f"""你是一个被测试的目标 AI 模型。
当前测试场景：{quest_context.get('scenario', '通用任务')}
任务目标：{quest_context.get('objective', '完成用户请求')}
限制条件：{', '.join(quest_context.get('constraints', []))}

请根据用户提供的提示词，生成符合要求的响应。
响应要真实自然，就像一个真实的 AI 助手一样。
如果提示词不清晰或不完整，按照最合理的理解进行响应。"""

        try:
            response = _MODEL.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ])
            
            return {
                "success": True,
                "response": response.content,
                "model_used": ALI_MODEL_NAME,
                "prompt_length": len(user_prompt),
                "response_length": len(response.content)
            }
            
        except Exception as e:
            return {
                "success": False,
                "response": f"模拟失败: {str(e)}",
                "error": str(e)
            }


class JudgeService:
    """裁判服务：评估 AI 响应质量"""
    
    @staticmethod
    def judge_response(
        user_prompt: str, 
        ai_response: str, 
        quest_context: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        评估 AI 响应的质量
        
        Args:
            user_prompt: 用户编写的提示词
            ai_response: AI 的响应内容
            quest_context: 题目上下文信息
            
        Returns:
            评分结果和评价意见
        """
        scoring_dimensions = quest_context.get('scoring_dimensions', [
            "任务完成度", "响应质量", "提示词清晰度"
        ])
        
        system_prompt = f"""你是一个专业的提示词质量评估专家。
请根据以下标准评估用户的提示词和 AI 响应：

题目场景：{quest_context.get('scenario', '通用任务')}
任务目标：{quest_context.get('objective', '完成用户请求')}
限制条件：{', '.join(quest_context.get('constraints', []))}
评分维度：{', '.join(scoring_dimensions)}

用户的提示词：
{user_prompt}

AI 的响应：
{ai_response}

请从以下几个维度进行评估，每个维度满分100分：
1. 任务完成度：AI 响应是否完成了任务目标
2. 响应质量：AI 响应的内容质量如何
3. 提示词清晰度：用户的提示词是否清晰明确
4. 限制遵守度：是否遵守了题目限制条件
5. 创新性：提示词是否有创新之处

请以 JSON 格式返回评估结果：
{{
    "total_score": 总分(满分100),
    "dimensions": {{
        "任务完成度": {{"score": 分数, "comment": "评价"}},
        "响应质量": {{"score": 分数, "comment": "评价"}},
        "提示词清晰度": {{"score": 分数, "comment": "评价"}},
        "限制遵守度": {{"score": 分数, "comment": "评价"}},
        "创新性": {{"score": 分数, "comment": "评价"}}
    }},
    "overall_comment": "总体评价",
    "improvement_suggestions": ["改进建议1", "改进建议2", "改进建议3"],
    "grade": "等级(S/A/B/C/D)"
}}"""

        try:
            response = _MODEL.invoke([
                SystemMessage(content=system_prompt),
                HumanMessage(content="请对以上提示词和响应进行专业评估。")
            ])
            
            content = response.content
            
            json_start = content.find('{')
            json_end = content.rfind('}') + 1
            if json_start != -1 and json_end > json_start:
                json_str = content[json_start:json_end]
                result = json.loads(json_str)
                
                if 'total_score' not in result:
                    scores = [d.get('score', 0) for d in result.get('dimensions', {}).values() if isinstance(d, dict)]
                    result['total_score'] = sum(scores) // len(scores) if scores else 0
                
                return {
                    "success": True,
                    **result
                }
            else:
                return JudgeService._default_judge_result()
                
        except Exception as e:
            print(f"评估失败: {str(e)}")
            return JudgeService._default_judge_result()
    
    @staticmethod
    def _default_judge_result() -> Dict[str, Any]:
        """返回默认的评估结果"""
        return {
            "success": True,
            "total_score": 60,
            "dimensions": {
                "任务完成度": {"score": 60, "comment": "基本完成任务"},
                "响应质量": {"score": 60, "comment": "响应质量一般"},
                "提示词清晰度": {"score": 60, "comment": "提示词基本清晰"},
                "限制遵守度": {"score": 60, "comment": "部分遵守限制"},
                "创新性": {"score": 60, "comment": "中规中矩"}
            },
            "overall_comment": "评估系统暂时无法给出详细评价，请稍后重试。",
            "improvement_suggestions": [
                "尝试使提示词更加具体明确",
                "可以添加更多上下文信息",
                "考虑添加输出格式要求"
            ],
            "grade": "C"
        }
