# app.py (基于 MongoDB 的登录/注册后端)
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

app = Flask(__name__)
# 允许跨域
CORS(app, resources={r"/*": {"origins": "*"}})

# 1. 连接 MongoDB 数据库
# 假设你的 MongoDB 运行在本地默认端口 27017
client = MongoClient('mongodb://localhost:27017/')
db = client['teacher_assistant']  # 数据库名称
users_collection = db['users']    # 用户集合名称

@app.route('/register', methods=['POST'])
def register():
    """ 用户注册接口 """
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return jsonify({"success": False, "message": "用户名和密码不能为空"}), 400

    # 检查用户是否已存在
    if users_collection.find_one({"username": username}):
        return jsonify({"success": False, "message": "该用户名已被注册"}), 409

    # 密码加密存储 (安全最佳实践)
    hashed_password = generate_password_hash(password)

    new_user = {
        "username": username,
        "password": hashed_password,
        "role": "teacher", # 默认为教师角色
        "created_at": datetime.datetime.utcnow()
    }

    try:
        users_collection.insert_one(new_user)
        return jsonify({"success": True, "message": "注册成功，请登录"}), 201
    except Exception as e:
        print(f"注册错误: {e}")
        return jsonify({"success": False, "message": "注册失败，请稍后重试"}), 500

@app.route('/login', methods=['POST'])
def login():
    """ 用户登录接口 """
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"收到登录请求: 用户名={username}")

    if not username or not password:
        return jsonify({"success": False, "message": "请输入用户名和密码"}), 400

    # 从数据库查找用户
    user = users_collection.find_one({"username": username})

    # 验证用户是否存在以及密码是否匹配
    if user and check_password_hash(user['password'], password):
        # 登录成功
        return jsonify({
            "success": True, 
            "message": "登录成功",
            "user": {
                "username": user['username'],
                "role": user.get('role', 'teacher'),
                "token": "fake-jwt-token-example" # 实际项目中建议换成真实的 JWT
            }
        })
    else:
        return jsonify({"success": False, "message": "用户名或密码错误"}), 401

if __name__ == '__main__':
    print("服务器启动中... 请确保 MongoDB 已开启")
    app.run(debug=True, port=5000)
