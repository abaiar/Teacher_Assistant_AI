import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useUserStore } from './store/user'

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)

// 初始化应用时检查用户登录状态
const userStore = useUserStore()
userStore.checkAuth()

app.mount('#app')
