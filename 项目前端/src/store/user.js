import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
    isAuthenticated: false
  }),
  
  actions: {
    login(userData) {
      this.user = userData
      this.isAuthenticated = true
      localStorage.setItem('user', JSON.stringify(userData))
    },
    
    logout() {
      this.user = null
      this.isAuthenticated = false
      localStorage.removeItem('user')
    },
    
    checkAuth() {
      // 强制用户每次打开页面都需要重新登录
      // 不自动从localStorage中恢复用户状态
      this.user = null
      this.isAuthenticated = false
      localStorage.removeItem('user')
    }
  }
})
