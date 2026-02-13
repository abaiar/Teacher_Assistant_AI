<template>
  <div class="zyyo-filter"></div>
  <div class="zyyo-main">
    <div class="zyyo-left">
      <div class="logo" style="background-image: url('../../static/img/touxiang.png');">
        <img style="position: absolute;top:-15%;left:-10%;width: 120%; aspect-ratio: 1/1;" src="../../static/img/logokuang.png">
      </div>
      <div class="left-div left-des">
        <div class="left-des-item">
          <svg t="1705773709627" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1478">
            <path d="M512 249.976471c-99.388235 0-180.705882 81.317647-180.705882 180.705882s81.317647 180.705882 180.705882 180.705882 180.705882-81.317647 180.705882-180.705882-81.317647-180.705882-180.705882-180.705882z m0 301.17647c-66.258824 0-120.470588-54.211765-120.470588-120.470588s54.211765-120.470588 120.470588-120.470588 120.470588 54.211765 120.470588 120.470588-54.211765 120.470588-120.470588 120.470588z" p-id="1479"></path>
            <path d="M512 39.152941c-216.847059 0-391.529412 174.682353-391.529412 391.529412 0 349.364706 391.529412 572.235294 391.529412 572.235294s391.529412-222.870588 391.529412-572.235294c0-216.847059-174.682353-391.529412-391.529412-391.529412z m0 891.482353C424.658824 873.411765 180.705882 686.682353 180.705882 430.682353c0-183.717647 147.576471-331.294118 331.294118-331.294118s331.294118 147.576471 331.294118 331.294118c0 256-243.952941 442.729412-331.294118 499.952941z" p-id="1480"></path>
          </svg>
          China-Yantai
        </div>
        <div class="left-des-item">
          <svg t="1705773906032" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2474">
            <path d="M729.6 234.666667H294.4V157.866667a51.2 51.2 0 0 1 51.2-51.2h332.8a51.2 51.2 0 0 1 51.2 51.2v76.8z m179.2 51.2a51.2 51.2 0 0 1 51.2 51.2v512a51.2 51.2 0 0 1-51.2 51.2H115.2a51.2 51.2 0 0 1-51.2-51.2v-512a51.2 51.2 0 0 1 51.2-51.2h793.557333z m-768 172.032c0 16.384 13.312 29.696 29.696 29.696h683.008a29.696 29.696 0 1 0 0-59.392H170.410667a29.696 29.696 0 0 0-29.696 29.696z m252.416 118.784c0 16.384 13.312 29.696 29.696 29.696h178.176a29.696 29.696 0 1 0 0-59.392H422.912a29.738667 29.738667 0 0 0-29.696 29.696z" p-id="2475"></path>
          </svg>
          线上教师助手
        </div>
      </div>
      <div class="left-div left-tag">
        <div class="left-tag-item">Langchain</div>
        <div class="left-tag-item">Dify</div> 
        <router-link to="/code-review" class="left-tag-item active">代码批改</router-link>
        <router-link to="/intelligent-quiz" class="left-tag-item">智能组卷</router-link>
        <router-link to="/score-analysis" class="left-tag-item">成绩分析</router-link>
        <router-link to="/intelligent-correction" class="left-tag-item">智能批改</router-link>
      </div>
    </div>
    <div class="zyyo-right">
      <header>
        <button class="back-home-btn" @click="goHome" title="返回首页">
          <svg viewBox="0 0 1024 1024" width="16" height="16">
            <path d="M946.5 505L560.1 118.8l-25.9-25.9a31.5 31.5 0 0 0-44.4 0L77.5 505a63.9 63.9 0 0 0-18.8 46c.4 35.2 29.7 63.3 64.9 63.3h42.5V940h691.8V614.3h43.4c17.1 0 33.2-6.7 45.3-18.8a63.6 63.6 0 0 0 18.8-45.3c0-17-6.7-33.1-18.9-45.2zM568 868H456V664h112v204zm217.9-325.7V868H632V640c0-22.1-17.9-40-40-40H432c-22.1 0-40 17.9-40 40v228H238.1V542.3h-96l370-369.7 23.1 23.1L882 542.3h-96.1z" fill="currentColor"/>
          </svg>
          首页
        </button>
        <div class="index-logo" style="background-image: url('../../static/img/logo.png');">
          <img style="position: absolute;top:-15%;left:-10%;width: 120%; aspect-ratio: 1/1;" src="../../static/img/logokuang.png">
        </div>
        <div class="welcome">
          Hello I' m <span class="gradientText">小助老师 </span>
        </div>
        <div class="description">
          ✨ <span class="purpleText">AI 编程思维导师</span> 采用苏格拉底式教学法，引导你发现代码中的问题！
        </div>
      </header>
      
      <div class="main-content">
        <div class="code-section">
          <div class="section-header">
            <div class="section-title">
              <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
                <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
              </svg>
              代码编辑器
            </div>
            <select v-model="selectedLanguage" class="language-select">
              <option value="Python">Python</option>
              <option value="JavaScript">JavaScript</option>
              <option value="Java">Java</option>
              <option value="C++">C++</option>
              <option value="C">C</option>
            </select>
          </div>
          
          <div class="code-editor">
            <div class="line-numbers">
              <div v-for="(line, index) in codeLines" :key="index" 
                   :class="['line-number', { 'highlight': highlightedLine === index + 1 }]"
                   @click="highlightedLine = index + 1">
                {{ index + 1 }}
              </div>
            </div>
            <textarea 
              v-model="codeContent" 
              placeholder="在这里输入你的代码..."
              spellcheck="false"
            ></textarea>
          </div>
          
          <div class="error-input">
            <label>错误信息（可选）：</label>
            <input 
              v-model="errorMessage" 
              placeholder="如果有报错，粘贴错误信息..."
            >
          </div>
          
          <div class="action-buttons">
            <button class="run-btn" @click="runAndAsk" :disabled="isProcessing || !codeContent.trim()">
              <span v-if="isProcessing">⏳ 思考中...</span>
              <span v-else>🚀 运行并求助</span>
            </button>
            <button class="reset-btn" @click="resetSession">
              🔄 新对话
            </button>
          </div>
        </div>
        
        <div class="interaction-section">
          <div class="tabs">
            <button 
              v-for="tab in tabs" 
              :key="tab.id"
              :class="['tab-btn', { 'active': activeTab === tab.id }]"
              @click="activeTab = tab.id"
            >
              {{ tab.icon }} {{ tab.name }}
            </button>
          </div>
          
          <div class="tab-content">
            <div v-if="activeTab === 'chat'" class="chat-panel">
              <div class="chat-messages" ref="chatContainer">
                <div v-if="chatMessages.length === 0" class="empty-state">
                  <div class="empty-icon">💬</div>
                  <p>输入代码后点击"运行并求助"，<br>小助老师会引导你发现问题！</p>
                </div>
                <div v-for="(msg, index) in chatMessages" :key="index" 
                     :class="['message', msg.role]">
                  <div class="message-avatar">
                    <template v-if="msg.role === 'user'">👤</template>
                    <img v-else src="../../static/img/touxiang.png" alt="小助老师" class="avatar-img">
                  </div>
                  <div class="message-content" v-html="formatMessage(msg.content)"></div>
                </div>
                <div v-if="isTyping" class="message assistant typing">
                  <div class="message-avatar">
                    <img src="../../static/img/touxiang.png" alt="小助老师" class="avatar-img">
                  </div>
                  <div class="message-content">
                    <span class="typing-indicator">
                      <span></span><span></span><span></span>
                    </span>
                  </div>
                </div>
              </div>
              <div class="chat-input">
                <input 
                  v-model="userInput" 
                  placeholder="继续提问或回复小助老师..."
                  @keyup.enter="sendFollowUp"
                  :disabled="isProcessing"
                >
                <button @click="sendFollowUp" :disabled="isProcessing || !userInput.trim()">
                  发送
                </button>
              </div>
            </div>
            
            <div v-if="activeTab === 'visual'" class="visual-panel">
              <div v-if="visualExplanations.length === 0" class="empty-state">
                <div class="empty-icon">🎬</div>
                <p>点击"像讲故事一样运行"按钮，<br>看看代码是如何一步步执行的！</p>
                <button class="story-btn" @click="explainCode" :disabled="isExplaining || !codeContent.trim()">
                  {{ isExplaining ? '📖 讲解中...' : '✨ 像讲故事一样运行' }}
                </button>
              </div>
              <div v-else class="visual-flow">
                <div class="flow-header">
                  <span>📚 代码执行故事</span>
                  <button class="clear-btn" @click="visualExplanations = []">清除</button>
                </div>
                <div class="flow-steps">
                  <div v-for="(step, index) in visualExplanations" :key="index"
                       :class="['flow-step', { 'current': highlightedLine === step.line }]"
                       @mouseenter="highlightedLine = step.line">
                    <div class="step-line">第 {{ step.line }} 行</div>
                    <div class="step-desc">{{ step.desc }}</div>
                  </div>
                </div>
              </div>
            </div>
            
            <div v-if="activeTab === 'prompt'" class="prompt-panel">
              <div class="prompt-intro">
                <h3>🎯 魔法指令练习</h3>
                <p>学习如何写好 AI 提示词，让 AI 更好地理解你的需求！</p>
              </div>
              <div class="prompt-task">
                <label>目标任务：</label>
                <select v-model="promptTask">
                  <option value="让 AI 生成代码">让 AI 生成代码</option>
                  <option value="让 AI 解释代码">让 AI 解释代码</option>
                  <option value="让 AI 优化代码">让 AI 优化代码</option>
                  <option value="让 AI 找 Bug">让 AI 找 Bug</option>
                </select>
              </div>
              <div class="prompt-input-area">
                <label>你写的 Prompt：</label>
                <textarea 
                  v-model="userPrompt" 
                  placeholder="例如：帮我写一个计算斐波那契数列的函数"
                  rows="4"
                ></textarea>
              </div>
              <button class="check-btn" @click="checkPrompt" :disabled="isCheckingPrompt || !userPrompt.trim()">
                {{ isCheckingPrompt ? '🔍 评价中...' : '🔍 让小助老师点评' }}
              </button>
              <div v-if="promptResult" class="prompt-result" v-html="formatMessage(promptResult)"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, nextTick, watch } from 'vue';
import { useRouter } from 'vue-router';
import { getServiceUrl } from '../config/api';

const router = useRouter();
const MENTOR_URL = getServiceUrl('CODE_CORRECTION_SERVICE');

const goHome = () => {
  router.push('/');
};

const selectedLanguage = ref('Python');
const codeContent = ref('');
const errorMessage = ref('');
const highlightedLine = ref(0);

const codeLines = computed(() => {
  return codeContent.value.split('\n');
});

const tabs = [
  { id: 'chat', name: '聊天室', icon: '💬' },
  { id: 'visual', name: '透视', icon: '🎬' },
  { id: 'prompt', name: '魔法', icon: '✨' }
];
const activeTab = ref('chat');

const chatMessages = ref([]);
const userInput = ref('');
const isProcessing = ref(false);
const isTyping = ref(false);
const chatContainer = ref(null);

const visualExplanations = ref([]);
const isExplaining = ref(false);

const userPrompt = ref('');
const promptTask = ref('让 AI 生成代码');
const promptResult = ref('');
const isCheckingPrompt = ref(false);

const sessionId = ref(`session_${Date.now()}`);

const formatMessage = (content) => {
  if (!content) return '';
  let html = content;
  html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/```(\w*)\n?([\s\S]*?)```/g, '<pre><code>$2</code></pre>');
  html = html.replace(/`(.*?)`/g, '<code class="inline">$1</code>');
  html = html.replace(/\n/g, '<br>');
  return html;
};

const scrollToBottom = async () => {
  await nextTick();
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

const runAndAsk = async () => {
  if (!codeContent.value.trim() || isProcessing.value) return;
  
  isProcessing.value = true;
  isTyping.value = true;
  
  chatMessages.value.push({
    role: 'user',
    content: `我运行了这段 ${selectedLanguage.value} 代码，请帮我看看有什么问题：\n\`\`\`\n${codeContent.value}\n\`\`\``
  });
  
  await scrollToBottom();
  
  try {
    const response = await fetch(`${MENTOR_URL}/api/mentor/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        code: codeContent.value,
        error_message: errorMessage.value,
        language: selectedLanguage.value,
        session_id: sessionId.value,
        user_message: ''
      })
    });
    
    isTyping.value = false;
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let fullResponse = '';
    
    chatMessages.value.push({
      role: 'assistant',
      content: ''
    });
    
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      
      const chunk = decoder.decode(value);
      fullResponse += chunk;
      chatMessages.value[chatMessages.value.length - 1].content = fullResponse;
      await scrollToBottom();
    }
    
  } catch (error) {
    console.error('请求错误:', error);
    isTyping.value = false;
    chatMessages.value.push({
      role: 'assistant',
      content: '😅 哎呀，出了点问题，请稍后再试...'
    });
  } finally {
    isProcessing.value = false;
  }
};

const sendFollowUp = async () => {
  if (!userInput.value.trim() || isProcessing.value) return;
  
  const message = userInput.value;
  userInput.value = '';
  
  chatMessages.value.push({
    role: 'user',
    content: message
  });
  
  isProcessing.value = true;
  isTyping.value = true;
  await scrollToBottom();
  
  try {
    const response = await fetch(`${MENTOR_URL}/api/mentor/chat`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        code: codeContent.value,
        error_message: errorMessage.value,
        language: selectedLanguage.value,
        session_id: sessionId.value,
        user_message: message
      })
    });
    
    isTyping.value = false;
    
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    let fullResponse = '';
    
    chatMessages.value.push({
      role: 'assistant',
      content: ''
    });
    
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      
      const chunk = decoder.decode(value);
      fullResponse += chunk;
      chatMessages.value[chatMessages.value.length - 1].content = fullResponse;
      await scrollToBottom();
    }
    
  } catch (error) {
    console.error('请求错误:', error);
    isTyping.value = false;
    chatMessages.value.push({
      role: 'assistant',
      content: '😅 哎呀，出了点问题，请稍后再试...'
    });
  } finally {
    isProcessing.value = false;
  }
};

const explainCode = async () => {
  if (!codeContent.value.trim() || isExplaining.value) return;
  
  isExplaining.value = true;
  
  try {
    const response = await fetch(`${MENTOR_URL}/api/mentor/explain`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        code: codeContent.value,
        language: selectedLanguage.value
      })
    });
    
    const result = await response.json();
    
    if (result.status === 'success') {
      visualExplanations.value = result.data;
      if (visualExplanations.value.length > 0) {
        highlightedLine.value = visualExplanations.value[0].line;
      }
    } else {
      alert('讲解失败，请稍后重试');
    }
  } catch (error) {
    console.error('请求错误:', error);
    alert('讲解过程中发生错误');
  } finally {
    isExplaining.value = false;
  }
};

const checkPrompt = async () => {
  if (!userPrompt.value.trim() || isCheckingPrompt.value) return;
  
  isCheckingPrompt.value = true;
  promptResult.value = '';
  
  try {
    const response = await fetch(`${MENTOR_URL}/api/mentor/prompt_check`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        user_prompt: userPrompt.value,
        target_task: promptTask.value
      })
    });
    
    const result = await response.json();
    
    if (result.status === 'success') {
      promptResult.value = result.data;
    } else {
      alert('评价失败，请稍后重试');
    }
  } catch (error) {
    console.error('请求错误:', error);
    alert('评价过程中发生错误');
  } finally {
    isCheckingPrompt.value = false;
  }
};

const resetSession = async () => {
  try {
    await fetch(`${MENTOR_URL}/api/mentor/reset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        session_id: sessionId.value
      })
    });
  } catch (error) {
    console.error('重置会话错误:', error);
  }
  
  sessionId.value = `session_${Date.now()}`;
  chatMessages.value = [];
  visualExplanations.value = [];
  promptResult.value = '';
  highlightedLine.value = 0;
};
</script>

<style scoped>
.main-content {
  display: flex;
  gap: 20px;
  padding: 20px;
  height: calc(100vh - 200px);
  min-height: 500px;
}

/* 代码编辑区域 - 毛玻璃风格设计 */
.code-section {
  flex: 6;
  display: flex;
  flex-direction: column;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* 代码区域头部 - 毛玻璃风格 */
.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  background: var(--gradient);
  color: white;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  font-size: 16px;
}

.section-title svg {
  width: 20px;
  height: 20px;
  fill: white;
}

.language-select {
  padding: 8px 16px;
  border-radius: 20px;
  border: 1px solid #9370DB;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.language-select:hover {
  background-color: #9370DB;
  color: white;
}

.language-select option {
  background: var(--item_bg_color);
  color: var(--main_text_color);
}

/* 代码编辑器 - 毛玻璃风格 */
.code-editor {
  flex: 1;
  display: flex;
  overflow: hidden;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.line-numbers {
  width: 50px;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-right: 1px solid rgba(255, 255, 255, 0.1);
  overflow-y: auto;
  padding: 12px 0;
}

.line-number {
  padding: 0 12px;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.5);
  text-align: right;
  cursor: pointer;
  transition: all 0.2s ease;
}

.line-number:hover {
  background: rgba(255, 255, 255, 0.1);
  color: rgba(255, 255, 255, 0.8);
}

.line-number.highlight {
  background: rgba(116, 123, 255, 0.3);
  color: var(--purple_text_color);
  font-weight: bold;
}

.code-editor textarea {
  flex: 1;
  padding: 12px 16px;
  border: none;
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 14px;
  line-height: 1.6;
  resize: none;
  outline: none;
  background: rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  color: var(--main_text_color);
}

.code-editor textarea::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

/* 错误信息输入 - 毛玻璃风格 */
.error-input {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.error-input label {
  font-size: 14px;
  color: var(--main_text_color);
  opacity: 0.8;
  white-space: nowrap;
}

.error-input input {
  flex: 1;
  padding: 8px 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.1);
  color: var(--main_text_color);
  transition: all 0.3s ease;
}

.error-input input::placeholder {
  color: rgba(255, 255, 255, 0.4);
}

.error-input input:focus {
  outline: none;
  border-color: var(--purple_text_color);
  background: rgba(255, 255, 255, 0.15);
}

/* 操作按钮区域 - 毛玻璃风格 */
.action-buttons {
  display: flex;
  gap: 12px;
  padding: 16px 20px;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
}

.run-btn {
  flex: 1;
  padding: 14px 24px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.run-btn:hover:not(:disabled) {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

.run-btn:disabled {
  background: rgba(255, 255, 255, 0.2);
  color: #9370DB;
  cursor: not-allowed;
  transform: none;
}

.reset-btn {
  padding: 14px 24px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.reset-btn:hover {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

/* 右侧交互栏 - 毛玻璃风格设计 */
.interaction-section {
  flex: 4;
  display: flex;
  flex-direction: column;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* 标签栏 - 毛玻璃风格 */
.tabs {
  display: flex;
  background: rgba(255, 255, 255, 0.05);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
}

.tab-btn {
  flex: 1;
  padding: 14px 16px;
  background: transparent;
  border: none;
  font-size: 14px;
  color: var(--main_text_color);
  opacity: 0.7;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
}

.tab-btn:hover {
  background: var(--item_hover_color);
  opacity: 0.9;
}

.tab-btn.active {
  color: var(--purple_text_color);
  font-weight: 600;
  opacity: 1;
  background: rgba(255, 255, 255, 0.1);
}

.tab-btn.active::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 40px;
  height: 3px;
  background: var(--gradient);
  border-radius: 2px;
}

.tab-content {
  flex: 1;
  overflow: hidden;
}

.chat-panel {
  height: 100%;
  display: flex;
  flex-direction: column;
}

/* 聊天消息区域 - 毛玻璃风格 */
.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 16px;
}

.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--main_text_color);
  opacity: 0.7;
  text-align: center;
}

.empty-state p {
  color: var(--main_text_color);
  font-size: 14px;
  line-height: 1.6;
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 16px;
}

/* 消息气泡 - 毛玻璃风格 */
.message {
  display: flex;
  gap: 12px;
  margin-bottom: 16px;
}

.message-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  flex-shrink: 0;
  overflow: hidden;
}

.message.user .message-avatar {
  background: var(--purple_text_color);
}

.message.assistant .message-avatar {
  background: var(--gradient);
  padding: 2px;
}

.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}

.message-content {
  flex: 1;
  padding: 12px 16px;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.6;
  color: var(--main_text_color);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.message.assistant .message-content {
  color: var(--main_text_color);
  background: var(--item_bg_color);
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.message.user .message-content {
  background: var(--gradient);
  color: white;
  border: none;
}

/* 代码块样式 - 适配毛玻璃主题 */
.message-content :deep(pre) {
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #f8f8f2;
  padding: 12px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 8px 0;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.message-content :deep(code) {
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 13px;
}

.message-content :deep(code.inline) {
  background: rgba(0, 0, 0, 0.15);
  color: var(--purple_text_color);
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 600;
}

.message.assistant .message-content :deep(code.inline) {
  background: rgba(116, 123, 255, 0.2);
  color: var(--purple_text_color);
}

.message.user .message-content :deep(code.inline) {
  background: rgba(255, 255, 255, 0.25);
  color: #fff;
}

/* 输入指示器 - 适配毛玻璃主题 */
.typing-indicator {
  display: flex;
  gap: 4px;
}

.typing-indicator span {
  width: 8px;
  height: 8px;
  background: var(--purple_text_color);
  border-radius: 50%;
  animation: typing 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing {
  0%, 60%, 100% {
    transform: translateY(0);
  }
  30% {
    transform: translateY(-10px);
  }
}

/* 聊天输入框 - 毛玻璃风格 */
.chat-input {
  display: flex;
  gap: 12px;
  padding: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
}

.chat-input input {
  flex: 1;
  padding: 12px 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 24px;
  font-size: 14px;
  background: rgba(255, 255, 255, 0.1);
  color: var(--main_text_color);
}

.chat-input input::placeholder {
  color: var(--main_text_color);
  opacity: 0.5;
}

.chat-input input:focus {
  outline: none;
  border-color: var(--purple_text_color);
  background: rgba(255, 255, 255, 0.15);
}

.chat-input button {
  padding: 12px 24px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.chat-input button:hover:not(:disabled) {
  background-color: #9370DB;
  color: white;
  transform: scale(1.05);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

.chat-input button:disabled {
  background: rgba(255, 255, 255, 0.2);
  color: #9370DB;
  cursor: not-allowed;
}

/* 可视化面板 - 毛玻璃风格 */
.visual-panel {
  height: 100%;
  padding: 16px;
  overflow-y: auto;
}

.visual-panel .empty-state {
  height: 100%;
}

.story-btn {
  margin-top: 20px;
  padding: 14px 28px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.story-btn:hover:not(:disabled) {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

.story-btn:disabled {
  background: rgba(255, 255, 255, 0.2);
  color: #9370DB;
  cursor: not-allowed;
}

/* 可视化流程 - 毛玻璃风格 */
.visual-flow {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.flow-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.flow-header span {
  font-weight: 600;
  color: var(--main_text_color);
}

.clear-btn {
  padding: 6px 12px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.clear-btn:hover {
  background-color: #9370DB;
  color: white;
}

.flow-steps {
  flex: 1;
  overflow-y: auto;
}

.flow-step {
  padding: 12px 16px;
  margin-bottom: 8px;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 12px;
  border-left: 4px solid rgba(255, 255, 255, 0.2);
  cursor: pointer;
  transition: all 0.3s ease;
}

.flow-step:hover {
  background: var(--item_hover_color);
}

.flow-step.current {
  border-left-color: var(--purple_text_color);
  background: rgba(116, 123, 255, 0.15);
}

.step-line {
  font-weight: 600;
  color: var(--purple_text_color);
  margin-bottom: 4px;
  font-size: 13px;
}

.step-desc {
  color: var(--main_text_color);
  font-size: 14px;
  line-height: 1.5;
  font-weight: 500;
}

/* Prompt 面板 - 毛玻璃风格 */
.prompt-panel {
  height: 100%;
  padding: 16px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
}

.prompt-intro {
  text-align: center;
  margin-bottom: 20px;
}

.prompt-intro h3 {
  color: var(--main_text_color);
  margin-bottom: 8px;
}

.prompt-intro p {
  color: var(--main_text_color);
  opacity: 0.7;
  font-size: 14px;
}

.prompt-task {
  margin-bottom: 16px;
}

.prompt-task label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: var(--main_text_color);
}

.prompt-task select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  font-size: 14px;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  color: var(--main_text_color);
}

.prompt-input-area {
  margin-bottom: 16px;
}

.prompt-input-area label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: var(--main_text_color);
}

.prompt-input-area textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  font-size: 14px;
  resize: vertical;
  font-family: inherit;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  color: var(--main_text_color);
}

.prompt-input-area textarea::placeholder {
  color: var(--main_text_color);
  opacity: 0.5;
}

.prompt-input-area textarea:focus {
  outline: none;
  border-color: var(--purple_text_color);
  background: rgba(255, 255, 255, 0.15);
}

.check-btn {
  width: 100%;
  padding: 14px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-bottom: 16px;
}

.check-btn:hover:not(:disabled) {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

.check-btn:disabled {
  background: rgba(255, 255, 255, 0.2);
  color: #9370DB;
  cursor: not-allowed;
}

.prompt-result {
  flex: 1;
  padding: 16px;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 12px;
  font-size: 14px;
  line-height: 1.6;
  overflow-y: auto;
  color: var(--main_text_color);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.prompt-result :deep(pre) {
  background: rgba(0, 0, 0, 0.6);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  color: #f8f8f2;
  padding: 12px;
  border-radius: 8px;
  overflow-x: auto;
  margin: 8px 0;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.prompt-result :deep(code) {
  font-family: 'Fira Code', 'Consolas', monospace;
  font-size: 13px;
  color: var(--purple_text_color);
  background: rgba(0, 0, 0, 0.15);
  padding: 2px 6px;
  border-radius: 4px;
}

.prompt-result :deep(strong) {
  color: var(--purple_text_color);
}

.prompt-result :deep(table) {
  width: 100%;
  border-collapse: collapse;
  margin: 12px 0;
}

.prompt-result :deep(th),
.prompt-result :deep(td) {
  padding: 8px 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  text-align: left;
}

.prompt-result :deep(th) {
  background: var(--purple_text_color);
  color: white;
}

.left-tag-item.active {
  color: #9370DB;
  font-weight: bold;
}

header {
  position: relative;
}

.back-home-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  z-index: 10;
}

.back-home-btn svg {
  fill: currentColor;
  margin-top: -2px;
}

.back-home-btn:hover {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.3);
}

.back-home-btn:active {
  transform: translateY(0);
}
</style>
