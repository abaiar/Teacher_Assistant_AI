# app.py (登录及主服务)
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 允许跨域，非常重要！
CORS(app, resources={r"/*": {"origins": "*"}})

# 模拟一个用户数据库
USERS = {
    "admin": "123456",
    "赵健硕": "zjs20060618"
}

@app.route('/login', methods=['POST'])
def login():
    # 因为前端使用的是 formData.append，所以这里用 request.form 获取
    username = request.form.get('username')
    password = request.form.get('password')
    
    print(f"收到登录请求: 用户名={username}, 密码={password}")

    if not username or not password:
        return jsonify({"success": False, "message": "请输入用户名和密码"}), 400

    if username in USERS and USERS[username] == password:
        # 登录成功
        return jsonify({
            "success": True, 
            "message": "登录成功",
            "user": {
                "username": username,
                "role": "teacher",
                "token": "fake-jwt-token-example"
            }
        })
    else:
        return jsonify({"success": False, "message": "用户名或密码错误"}), 401

if __name__ == '__main__':
    # 确保这里是 5000 端口，和前端对应
    print("服务已启动：http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)