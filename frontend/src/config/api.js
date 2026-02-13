const API_CONFIG = {
  LOGIN_SERVICE: {
    BASE_URL: 'http://127.0.0.1:5000',
    LOGIN: '/login',
    REGISTER: '/register'
  },
  PAPER_MARKING_SERVICE: {
    BASE_URL: 'http://127.0.0.1:5001',
    CORRECT: '/correct'
  },
  PAPER_COMPOSITION_SERVICE: {
    BASE_URL: 'http://127.0.0.1:5002',
    GENERATE_QUIZ: '/generate_quiz'
  },
  ACHIEVEMENT_ANALYSIS_SERVICE: {
    BASE_URL: 'http://127.0.0.1:5003',
    ANALYZE: '/analyze'
  },
  CODE_CORRECTION_SERVICE: {
    BASE_URL: 'http://127.0.0.1:5004',
    REVIEW_CODE: '/review_code',
    ENDPOINTS: {
      CHAT: '/api/mentor/chat',
      EXPLAIN: '/api/mentor/explain',
      PROMPT_CHECK: '/api/mentor/prompt_check',
      RESET: '/api/mentor/reset',
      HEALTH: '/health'
    }
  }
}

export function getApiUrl(service, endpoint) {
  const serviceConfig = API_CONFIG[service]
  if (!serviceConfig) {
    console.error(`Unknown service: ${service}`)
    return ''
  }
  return `${serviceConfig.BASE_URL}${serviceConfig.ENDPOINTS ? serviceConfig.ENDPOINTS[endpoint] : endpoint}`
}

export function getServiceUrl(serviceName) {
  const service = API_CONFIG[serviceName]
  if (!service) {
    console.error(`Unknown service: ${serviceName}`)
    return ''
  }
  return service.BASE_URL
}

export default API_CONFIG
