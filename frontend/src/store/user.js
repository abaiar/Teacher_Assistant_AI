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
      localStorage.setItem('isAuthenticated', 'true')
    },
    
    logout() {
      this.user = null
      this.isAuthenticated = false
      localStorage.removeItem('user')
      localStorage.removeItem('isAuthenticated')
    },
    
    checkAuth() {
      const savedUser = localStorage.getItem('user')
      const isAuthenticated = localStorage.getItem('isAuthenticated')
      
      if (savedUser && isAuthenticated === 'true') {
        try {
          this.user = JSON.parse(savedUser)
          this.isAuthenticated = true
        } catch (e) {
          this.user = null
          this.isAuthenticated = false
          localStorage.removeItem('user')
          localStorage.removeItem('isAuthenticated')
        }
      }
    }
  }
})
