import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '../store/user'

// 导入组件
import Login from '../components/Login.vue'
import Index from '../components/Index.vue'
import IntelligentCorrection from '../components/智能批改的前端页面.vue'
import IntelligentQuiz from '../components/智能组卷的前端页面.vue'
import ScoreAnalysis from '../components/成绩分析的前端页面.vue'
import CodeReview from '../components/代码批改的前端页面.vue'

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
    meta: { requiresAuth: true } // 需要登录才能访问
  },
  {
    path: '/intelligent-correction',
    name: 'IntelligentCorrection',
    component: IntelligentCorrection,
    meta: { requiresAuth: true } // 需要登录才能访问
  },
  {
    path: '/intelligent-quiz',
    name: 'IntelligentQuiz',
    component: IntelligentQuiz,
    meta: { requiresAuth: true } // 需要登录才能访问
  },
  {
    path: '/score-analysis',
    name: 'ScoreAnalysis',
    component: ScoreAnalysis,
    meta: { requiresAuth: true } // 需要登录才能访问
  },
  {
    path: '/code-review',
    name: 'CodeReview',
    component: CodeReview,
    meta: { requiresAuth: true } // 需要登录才能访问
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
