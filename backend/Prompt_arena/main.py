# -*- coding: utf-8 -*-
"""
Prompt Arena - 提示词竞技场 Flask 应用

提供三个核心 API 端点：
- POST /api/prompt_arena/new_quest: 生成新题目
- POST /api/prompt_arena/simulate: 模拟 AI 响应
- POST /api/prompt_arena/judge: 评估响应质量
"""

import os
import sys
import warnings
import dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS

if __name__ == "__main__" and __package__ is None:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from services import QuestService, SimulationService, JudgeService
else:
    from .services import QuestService, SimulationService, JudgeService

dotenv.load_dotenv()

app = Flask(__name__)
CORS(app)

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)


@app.route('/api/prompt_arena/new_quest', methods=['POST'])
def new_quest():
    """
    生成一个新的提示词训练题目
    
    Request Body (可选):
        {
            "use_ai": true/false  # 是否使用 AI 生成题目
        }
    
    Response:
        {
            "success": true,
            "quest": {
                "quest_id": "quest_xxxx",
                "category": "题目类别",
                "scenario": "场景描述",
                "objective": "任务目标",
                "constraints": ["限制条件"],
                "difficulty": "难度等级",
                "tips": ["提示"]
            }
        }
    """
    try:
        data = request.get_json() or {}
        use_ai = data.get('use_ai', False)
        
        if use_ai:
            quest = QuestService.generate_quest_with_ai()
        else:
            quest = QuestService.generate_quest()
        
        return jsonify({
            "success": True,
            "quest": quest
        }), 200
        
    except Exception as e:
        print(f"生成题目失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/prompt_arena/simulate', methods=['POST'])
def simulate():
    """
    模拟 AI 对用户提示词的响应
    
    Request Body:
        {
            "prompt": "用户编写的提示词",
            "quest_context": {
                "scenario": "场景描述",
                "objective": "任务目标",
                "constraints": ["限制条件"]
            }
        }
    
    Response:
        {
            "success": true,
            "response": "AI 的响应内容",
            "model_used": "使用的模型名称",
            "prompt_length": 提示词长度,
            "response_length": 响应长度
        }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "error": "请求体不能为空"
            }), 400
        
        user_prompt = data.get('prompt', '')
        quest_context = data.get('quest_context', {})
        
        if not user_prompt:
            return jsonify({
                "success": False,
                "error": "提示词不能为空"
            }), 400
        
        result = SimulationService.simulate_response(user_prompt, quest_context)
        
        return jsonify(result), 200
        
    except Exception as e:
        print(f"模拟响应失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/prompt_arena/judge', methods=['POST'])
def judge():
    """
    评估 AI 响应的质量
    
    Request Body:
        {
            "prompt": "用户编写的提示词",
            "response": "AI 的响应内容",
            "quest_context": {
                "scenario": "场景描述",
                "objective": "任务目标",
                "constraints": ["限制条件"],
                "scoring_dimensions": ["评分维度"]
            }
        }
    
    Response:
        {
            "success": true,
            "total_score": 总分,
            "dimensions": {
                "维度名": {"score": 分数, "comment": "评价"}
            },
            "overall_comment": "总体评价",
            "improvement_suggestions": ["改进建议"],
            "grade": "等级"
        }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                "success": False,
                "error": "请求体不能为空"
            }), 400
        
        user_prompt = data.get('prompt', '')
        ai_response = data.get('response', '')
        quest_context = data.get('quest_context', {})
        
        if not user_prompt:
            return jsonify({
                "success": False,
                "error": "提示词不能为空"
            }), 400
        
        if not ai_response:
            return jsonify({
                "success": False,
                "error": "AI 响应不能为空"
            }), 400
        
        result = JudgeService.judge_response(user_prompt, ai_response, quest_context)
        
        return jsonify(result), 200
        
    except Exception as e:
        print(f"评估失败: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


@app.route('/api/prompt_arena/health', methods=['GET'])
def health():
    """健康检查端点"""
    return jsonify({
        "status": "healthy",
        "service": "prompt_arena",
        "version": "1.0.0"
    }), 200


@app.route('/', methods=['GET'])
def index():
    """服务首页"""
    return jsonify({
        "service": "Prompt Arena - 提示词竞技场",
        "version": "1.0.0",
        "endpoints": [
            "POST /api/prompt_arena/new_quest - 生成新题目",
            "POST /api/prompt_arena/simulate - 模拟 AI 响应",
            "POST /api/prompt_arena/judge - 评估响应质量",
            "GET /api/prompt_arena/health - 健康检查"
        ]
    }), 200


if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("🚀 Prompt Arena - 提示词竞技场服务")
    print("=" * 50)
    print("端口: 5005")
    print("=" * 50 + "\n")
    
    app.run(host='0.0.0.0', port=5005, debug=False)
