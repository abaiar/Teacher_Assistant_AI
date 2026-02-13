import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '../store/user'

// 导入组件
import Login from '../components/Login.vue'
import Index from '../components/Index.vue'
import IntelligentCorrection from '../components/intelligent-correction.vue'
import IntelligentQuiz from '../components/intelligent-quiz.vue'
import ScoreAnalysis from '../components/score-analysis.vue'
import CodeReview from '../components/code-review.vue'
import PromptArena from '../components/PromptArena.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/',
    name: 'Index',
    component: Index,
    meta: { requiresAuth: true }
  },
  {
    path: '/intelligent-correction',
    name: 'IntelligentCorrection',
    component: IntelligentCorrection,
    meta: { requiresAuth: true }
  },
  {
    path: '/intelligent-quiz',
    name: 'IntelligentQuiz',
    component: IntelligentQuiz,
    meta: { requiresAuth: true }
  },
  {
    path: '/score-analysis',
    name: 'ScoreAnalysis',
    component: ScoreAnalysis,
    meta: { requiresAuth: true }
  },
  {
    path: '/code-review',
    name: 'CodeReview',
    component: CodeReview,
    meta: { requiresAuth: true }
  },
  {
    path: '/prompt-arena',
    name: 'PromptArena',
    component: PromptArena,
    meta: { requiresAuth: true }
  },
  {
    path: '/:pathMatch(.*)*',
    redirect: '/login'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  
  // 检查是否需要登录
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // 检查用户是否已登录
    if (!userStore.isAuthenticated) {
      // 未登录，跳转到登录页面
      next({
        path: '/login',
        query: { redirect: to.fullPath } // 保存当前路径，登录后跳转回来
      })
    } else {
      // 已登录，继续访问
      next()
    }
  } else {
    // 不需要登录的页面，直接访问
    next()
  }
})

export default router
