<template>
  <div class="login-container">
    <div class="login-box">
      <div class="login-header">
        <img src="../../static/img/logokuang.png" alt="Logo" class="logo">
        <h2>教师助手系统</h2>
      </div>
      
      <form @submit.prevent="handleLogin" class="login-form">
        <div class="form-group">
          <label for="username">用户名</label>
          <input 
            type="text" 
            id="username" 
            v-model="loginForm.username" 
            placeholder="请输入用户名"
            required
          >
        </div>
        
        <div class="form-group">
          <label for="password">密码</label>
          <input 
            type="password" 
            id="password" 
            v-model="loginForm.password" 
            placeholder="请输入密码"
            required
          >
        </div>
        
        <div v-if="error" class="error-message">
          {{ error }}
        </div>
        
        <button type="submit" class="login-button" :disabled="isLoading">
          {{ isLoading ? '登录中...' : '登录' }}
        </button>
      </form>
      
      <div class="login-footer">
        <p>教师助手系统 © 2025</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '../store/user'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()

const loginForm = ref({
  username: '',
  password: ''
})

const error = ref('')
const isLoading = ref(false)

const handleLogin = async () => {
  error.value = ''
  isLoading.value = true
  
  try {
    // 为了测试方便，添加一个简单的本地验证
    // 实际项目中应该调用后端API
    if (loginForm.value.username === 'admin' && loginForm.value.password === 'admin123') {
      // 登录成功，更新用户状态
      const userData = {
        username: loginForm.value.username,
        role: 'admin'
      }
      userStore.login(userData)
      
      // 获取登录前的跳转路径，如果没有则跳转到主页面
      const redirectPath = route.query.redirect || '/'
      router.push(redirectPath)
    } else {
      // 登录失败，显示错误信息
      error.value = '用户名或密码错误，请使用测试账号: admin/admin123'
    }
  } catch (err) {
    error.value = '登录失败，请检查网络连接或服务器状态'
    console.error('登录错误:', err)
  } finally {
    isLoading.value = false
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-image: url('../../static/img/background.jpg');
  background-size: cover;
  background-position: center;
}

.login-box {
  background-color: rgba(255, 255, 255, 0.95);
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 400px;
}

.login-header {
  text-align: center;
  margin-bottom: 2rem;
}

.logo {
  width: 100px;
  height: 100px;
  margin-bottom: 1rem;
}

.login-header h2 {
  color: #333;
  font-size: 1.8rem;
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.form-group label {
  color: #555;
  font-weight: 500;
}

.form-group input {
  padding: 0.8rem;
  border: 1px solid #ddd;
  border-radius: 6px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #6c63ff;
}

.error-message {
  color: #ff4444;
  text-align: center;
  padding: 0.5rem;
  background-color: #ffebee;
  border-radius: 4px;
}

.login-button {
  padding: 0.9rem;
  background-color: #6c63ff;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-button:hover:not(:disabled) {
  background-color: #5a52e8;
}

.login-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.login-footer {
  text-align: center;
  margin-top: 1.5rem;
  color: #666;
  font-size: 0.9rem;
}
</style>