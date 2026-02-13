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
        <router-link to="/code-review" class="left-tag-item">代码批改</router-link>
        <router-link to="/intelligent-quiz" class="left-tag-item">智能组卷</router-link>
        <router-link to="/score-analysis" class="left-tag-item">成绩分析</router-link>
        <router-link to="/intelligent-correction" class="left-tag-item">智能批改</router-link>
        <router-link to="/prompt-arena" class="left-tag-item active">提示词竞技场</router-link>
      </div>
    </div>
    <div class="zyyo-right arena-container">
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
          Hello I' m <span class="gradientText">提示词竞技场</span>
        </div>
        <div class="description">
          🎯 <span class="purpleText">提示词竞技场</span> 是一个交互式训练平台，帮助你提升 AI 提示词编写能力。
        </div>
      </header>
      
      <content class="arena-content">
        <div class="arena-layout">
          <!-- 左侧主区域：任务目标 + 提示词输入 -->
          <div class="arena-panel main-panel">
            <!-- 任务目标区域 -->
            <div class="quest-section">
              <div class="section-header">
                <svg viewBox="0 0 1024 1024" width="18" height="18">
                  <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64z m0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="currentColor"/>
                  <path d="M464 336a48 48 0 1 0 96 0 48 48 0 1 0-96 0z m72 112h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8h48c4.4 0 8-3.6 8-8V456c0-4.4-3.6-8-8-8z" fill="currentColor"/>
                </svg>
                <span>任务目标</span>
                <button v-if="currentQuest" class="refresh-btn" @click="generateQuest" :disabled="isGenerating" title="换一题">
                  <svg viewBox="0 0 1024 1024" width="14" height="14">
                    <path d="M832 128H192c-35.2 0-64 28.8-64 64v640c0 35.2 28.8 64 64 64h640c35.2 0 64-28.8 64-64V192c0-35.2-28.8-64-64-64z m-544 640H224V224h64v544z m480 0H288V224h480v544z" fill="currentColor"/>
                  </svg>
                </button>
              </div>
              <div class="quest-content">
                <div v-if="!currentQuest" class="quest-empty">
                  <p>点击下方按钮生成新题目</p>
                  <button class="generate-btn" @click="generateQuest" :disabled="isGenerating">
                    {{ isGenerating ? '生成中...' : '生成题目' }}
                  </button>
                </div>
                <div v-else class="quest-info-compact">
                  <div class="quest-header-row">
                    <span class="quest-category">{{ currentQuest.category }}</span>
                    <span class="quest-difficulty" :class="currentQuest.difficulty">{{ currentQuest.difficulty }}</span>
                  </div>
                  <p class="quest-scenario"><strong>场景：</strong>{{ currentQuest.scenario }}</p>
                  <p class="quest-objective"><strong>目标：</strong>{{ currentQuest.objective }}</p>
                  <div class="quest-constraints-compact" v-if="currentQuest.constraints && currentQuest.constraints.length">
                    <strong>限制：</strong>
                    <span v-for="(constraint, index) in currentQuest.constraints" :key="index" class="constraint-tag">
                      {{ constraint }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- 提示词输入区域 -->
            <div class="chat-section">
              <div class="section-header">
                <svg viewBox="0 0 1024 1024" width="18" height="18">
                  <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64z m0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="currentColor"/>
                  <path d="M464 336a48 48 0 1 0 96 0 48 48 0 1 0-96 0z m72 112h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8h48c4.4 0 8-3.6 8-8V456c0-4.4-3.6-8-8-8z" fill="currentColor"/>
                </svg>
                <span>提示词输入与对话</span>
              </div>
              <div class="chat-body">
                <div class="chat-messages" ref="chatContainer">
                  <div v-if="messages.length === 0" class="chat-placeholder">
                    <div class="placeholder-content">
                      <span class="placeholder-icon">💬</span>
                      <p>在下方输入你的提示词，点击"模拟"查看 AI 响应</p>
                    </div>
                  </div>
                  <div v-for="(msg, index) in messages" :key="index" class="chat-message" :class="msg.role">
                    <div class="message-avatar">{{ msg.role === 'user' ? '👤' : '🤖' }}</div>
                    <div class="message-content">
                      <div class="message-label">{{ msg.role === 'user' ? '你的提示词' : 'AI 响应' }}</div>
                      <div class="message-text">{{ msg.content }}</div>
                    </div>
                  </div>
                </div>
                <div class="chat-input-area">
                  <textarea v-model="userPrompt" placeholder="在此输入你的提示词..." :disabled="isSimulating || !currentQuest" rows="2"></textarea>
                  <div class="chat-actions">
                    <button class="action-btn simulate-btn" @click="simulateResponse" :disabled="!userPrompt.trim() || isSimulating || !currentQuest">
                      {{ isSimulating ? '模拟中...' : '模拟' }}
                    </button>
                    <button class="action-btn judge-btn" @click="judgeResponse" :disabled="!aiResponse || isJudging">
                      {{ isJudging ? '评分中...' : '评分' }}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          
          <!-- 右侧评分结果 -->
          <div class="arena-panel score-panel">
            <div class="panel-header">
              <svg viewBox="0 0 1024 1024" width="20" height="20">
                <path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64z m0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" fill="currentColor"/>
                <path d="M464 336a48 48 0 1 0 96 0 48 48 0 1 0-96 0z m72 112h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8h48c4.4 0 8-3.6 8-8V456c0-4.4-3.6-8-8-8z" fill="currentColor"/>
              </svg>
              <span>评分结果</span>
            </div>
            <div class="panel-body">
              <div v-if="!judgeResult" class="empty-state">
                <div class="empty-icon">🏆</div>
                <p>完成模拟后点击"评分"查看结果</p>
              </div>
              <div v-else class="score-info">
                <div class="total-score">
                  <div class="score-circle" :class="getGradeClass(judgeResult.total_score)">
                    <span class="score-number">{{ judgeResult.total_score }}</span>
                    <span class="score-label">总分</span>
                  </div>
                  <div class="grade-badge" :class="getGradeClass(judgeResult.total_score)">
                    {{ judgeResult.grade || getGrade(judgeResult.total_score) }}
                  </div>
                </div>
                
                <div class="dimension-scores">
                  <h4>维度评分</h4>
                  <div v-for="(dim, name) in judgeResult.dimensions" :key="name" class="dimension-item">
                    <div class="dimension-header">
                      <span class="dimension-name">{{ name }}</span>
                      <span class="dimension-score">{{ dim.score }}分</span>
                    </div>
                    <div class="dimension-bar">
                      <div class="dimension-fill" :style="{ width: dim.score + '%' }"></div>
                    </div>
                    <p class="dimension-comment">{{ dim.comment }}</p>
                  </div>
                </div>
                
                <div class="overall-comment">
                  <h4>总体评价</h4>
                  <p>{{ judgeResult.overall_comment }}</p>
                </div>
                
                <div class="suggestions">
                  <h4>改进建议</h4>
                  <ul>
                    <li v-for="(suggestion, index) in judgeResult.improvement_suggestions" :key="index">
                      {{ suggestion }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </content>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue';
import { useRouter } from 'vue-router';
import { getServiceUrl } from '../config/api';

const router = useRouter();
const PROMPT_ARENA_URL = getServiceUrl('PROMPT_ARENA_SERVICE');

const goHome = () => {
  router.push('/');
};

const currentQuest = ref(null);
const userPrompt = ref('');
const messages = ref([]);
const aiResponse = ref('');
const judgeResult = ref(null);

const isGenerating = ref(false);
const isSimulating = ref(false);
const isJudging = ref(false);

const chatContainer = ref(null);

const generateQuest = async () => {
  isGenerating.value = true;
  currentQuest.value = null;
  messages.value = [];
  aiResponse.value = '';
  judgeResult.value = null;
  
  try {
    const response = await fetch(`${PROMPT_ARENA_URL}/api/prompt_arena/new_quest`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({})
    });
    
    const result = await response.json();
    
    if (result.success) {
      currentQuest.value = result.quest;
    } else {
      alert('生成题目失败: ' + result.error);
    }
  } catch (error) {
    console.error('生成题目失败:', error);
    alert('生成题目失败，请检查服务是否启动');
  } finally {
    isGenerating.value = false;
  }
};

const simulateResponse = async () => {
  if (!userPrompt.value.trim() || !currentQuest.value) return;
  
  isSimulating.value = true;
  
  messages.value.push({
    role: 'user',
    content: userPrompt.value
  });
  
  await nextTick();
  scrollToBottom();
  
  try {
    const response = await fetch(`${PROMPT_ARENA_URL}/api/prompt_arena/simulate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        prompt: userPrompt.value,
        quest_context: {
          scenario: currentQuest.value.scenario,
          objective: currentQuest.value.objective,
          constraints: currentQuest.value.constraints
        }
      })
    });
    
    const result = await response.json();
    
    if (result.success) {
      aiResponse.value = result.response;
      messages.value.push({
        role: 'assistant',
        content: result.response
      });
    } else {
      messages.value.push({
        role: 'assistant',
        content: '模拟失败: ' + (result.error || '未知错误')
      });
    }
    
    await nextTick();
    scrollToBottom();
    
  } catch (error) {
    console.error('模拟响应失败:', error);
    messages.value.push({
      role: 'assistant',
      content: '模拟失败，请检查服务是否启动'
    });
  } finally {
    isSimulating.value = false;
  }
};

const judgeResponse = async () => {
  if (!aiResponse.value || !currentQuest.value) return;
  
  isJudging.value = true;
  
  try {
    const response = await fetch(`${PROMPT_ARENA_URL}/api/prompt_arena/judge`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        prompt: userPrompt.value,
        response: aiResponse.value,
        quest_context: {
          scenario: currentQuest.value.scenario,
          objective: currentQuest.value.objective,
          constraints: currentQuest.value.constraints,
          scoring_dimensions: ['任务完成度', '响应质量', '提示词清晰度', '限制遵守度', '创新性']
        }
      })
    });
    
    const result = await response.json();
    
    if (result.success) {
      judgeResult.value = result;
    } else {
      alert('评分失败: ' + result.error);
    }
  } catch (error) {
    console.error('评分失败:', error);
    alert('评分失败，请检查服务是否启动');
  } finally {
    isJudging.value = false;
  }
};

const scrollToBottom = () => {
  if (chatContainer.value) {
    chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  }
};

const getGrade = (score) => {
  if (score >= 90) return 'S';
  if (score >= 80) return 'A';
  if (score >= 70) return 'B';
  if (score >= 60) return 'C';
  return 'D';
};

const getGradeClass = (score) => {
  if (score >= 90) return 'grade-s';
  if (score >= 80) return 'grade-a';
  if (score >= 70) return 'grade-b';
  if (score >= 60) return 'grade-c';
  return 'grade-d';
};
</script>

<style scoped>
.arena-container {
  width: calc(100% - 160px);
}

.arena-content {
  padding: 15px;
}

/* 两栏布局：左侧65%，右侧35% */
.arena-layout {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 15px;
  height: calc(100vh - 180px);
  min-height: 500px;
}

/* 竞技场面板 - 炫彩毛玻璃风格设计 */
.arena-panel {
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 
    0 4px 20px rgba(0, 0, 0, 0.1),
    0 0 40px rgba(147, 112, 219, 0.1),
    inset 0 1px 0 rgba(255, 255, 255, 0.1);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transition: all 0.3s ease;
  position: relative;
}

.arena-panel::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent
  );
}

.arena-panel:hover {
  transform: translateY(-2px);
  box-shadow: 
    0 8px 30px rgba(0, 0, 0, 0.15),
    0 0 60px rgba(147, 112, 219, 0.15),
    inset 0 1px 0 rgba(255, 255, 255, 0.15);
}

/* 主面板 - 左侧大面板 */
.main-panel {
  display: flex;
  flex-direction: column;
  gap: 0;
}

/* 任务区域 - 紧凑设计 */
.quest-section {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
  background: linear-gradient(135deg, rgba(147, 112, 219, 0.05), transparent);
}

.section-header {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 16px;
  background: var(--gradient);
  color: white;
  font-weight: 600;
  font-size: 14px;
  position: relative;
  overflow: hidden;
}

.section-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  animation: shimmer 3s infinite;
}

@keyframes shimmer {
  0% { left: -100%; }
  100% { left: 100%; }
}

.section-header svg {
  fill: white;
}

/* 刷新按钮 - 改为返回首页按钮风格 */
.refresh-btn {
  margin-left: auto;
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 6px 12px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB;
  border: 1px solid #9370DB;
  border-radius: 20px;
  cursor: pointer;
  font-size: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 1;
}

.refresh-btn:hover:not(:disabled) {
  background-color: #9370DB;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(147, 112, 219, 0.4);
}

.refresh-btn:active {
  transform: translateY(0);
}

.refresh-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none;
}

.quest-content {
  padding: 12px 16px;
}

.quest-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 12px;
  padding: 20px;
  text-align: center;
}

.quest-empty p {
  color: var(--main_text_color);
  opacity: 0.7;
  font-size: 14px;
}

/* 紧凑的任务信息 */
.quest-info-compact {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.quest-header-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 4px;
}

.quest-category {
  display: inline-block;
  background: var(--left_tag_item);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  padding: 3px 10px;
  border-radius: 12px;
  font-size: 12px;
  color: var(--main_text_color);
  font-weight: 500;
}

.quest-scenario,
.quest-objective {
  color: var(--main_text_color);
  font-size: 13px;
  line-height: 1.5;
  margin: 0;
}

.quest-scenario strong,
.quest-objective strong {
  color: var(--purple_text_color);
  font-weight: 600;
}

.quest-constraints-compact {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--main_text_color);
}

.quest-constraints-compact strong {
  color: var(--purple_text_color);
  font-weight: 600;
}

.constraint-tag {
  background: rgba(147, 112, 219, 0.2);
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
  color: var(--main_text_color);
}

.quest-difficulty {
  display: inline-block;
  padding: 2px 8px;
  border-radius: 10px;
  font-size: 11px;
  font-weight: 600;
}

.quest-difficulty.简单 {
  background: rgba(76, 175, 80, 0.25);
  color: #4CAF50;
}

.quest-difficulty.中等 {
  background: rgba(255, 152, 0, 0.25);
  color: #FF9800;
}

.quest-difficulty.困难 {
  background: rgba(244, 67, 54, 0.25);
  color: #F44336;
}

/* 生成按钮 - 炫彩风格 */
.generate-btn {
  background: var(--gradient);
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 15px rgba(147, 112, 219, 0.3);
  position: relative;
  overflow: hidden;
}

.generate-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
  transition: left 0.5s;
}

.generate-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(147, 112, 219, 0.5);
}

.generate-btn:hover:not(:disabled)::before {
  left: 100%;
}

.generate-btn:disabled {
  background: rgba(255, 255, 255, 0.2);
  cursor: not-allowed;
  box-shadow: none;
}

.generate-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

/* 聊天区域 - 占据剩余空间 */
.chat-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.chat-section .chat-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* 面板头部 - 炫彩渐变风格 */
.panel-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 14px 16px;
  background: var(--gradient);
  font-weight: 600;
  font-size: 15px;
  color: white;
  position: relative;
  overflow: hidden;
}

.panel-header::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
  animation: shimmer 3s infinite;
}

.panel-header svg {
  fill: white;
}

/* 面板内容区域 */
.panel-body {
  flex: 1;
  padding: 16px;
  overflow-y: auto;
}

/* 空状态 - 毛玻璃风格 */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  text-align: center;
  color: var(--main_text_color);
  opacity: 0.7;
  padding: 20px;
}

.empty-icon {
  font-size: 48px;
  margin-bottom: 12px;
}

.empty-state p {
  font-size: 14px;
  line-height: 1.5;
}

/* 聊天面板 - 毛玻璃风格 */
.chat-panel {
  display: flex;
  flex-direction: column;
}

.chat-body {
  display: flex;
  flex-direction: column;
  padding: 0;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 12px 16px;
}

.chat-placeholder {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: var(--main_text_color);
  opacity: 0.7;
  text-align: center;
}

.placeholder-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
}

.placeholder-icon {
  font-size: 32px;
}

/* 聊天消息 - 毛玻璃风格 */
.chat-message {
  display: flex;
  gap: 10px;
  margin-bottom: 12px;
}

.chat-message.user {
  flex-direction: row-reverse;
}

.message-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 16px;
  flex-shrink: 0;
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.message-content {
  max-width: 85%;
}

.message-label {
  font-size: 10px;
  color: var(--main_text_color);
  opacity: 0.6;
  margin-bottom: 2px;
}

.chat-message.user .message-label {
  text-align: right;
}

.message-text {
  background: var(--item_bg_color);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 13px;
  line-height: 1.5;
  color: var(--main_text_color);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-message.user .message-text {
  background: var(--gradient);
  color: white;
  border: none;
}

/* 聊天输入区域 - 毛玻璃风格 */
.chat-input-area {
  padding: 12px 16px;
  background: rgba(0, 0, 0, 0.2);
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-input-area textarea {
  width: 100%;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  padding: 10px 12px;
  color: var(--main_text_color);
  font-size: 13px;
  resize: none;
  font-family: inherit;
  transition: all 0.3s ease;
}

.chat-input-area textarea:focus {
  outline: none;
  border-color: var(--purple_text_color);
  background: rgba(255, 255, 255, 0.15);
}

.chat-input-area textarea::placeholder {
  color: var(--main_text_color);
  opacity: 0.5;
}

.chat-actions {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

/* 操作按钮 - 炫彩风格 */
.action-btn {
  flex: 1;
  padding: 10px 16px;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-size: 13px;
  font-weight: 600;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.simulate-btn {
  background: var(--gradient);
  color: white;
  box-shadow: 0 4px 15px rgba(147, 112, 219, 0.3);
}

.judge-btn {
  background: linear-gradient(135deg, #4CAF50, #45a049);
  color: white;
  box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
}

.action-btn::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
  transition: left 0.5s;
}

.action-btn:hover:not(:disabled) {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(147, 112, 219, 0.4);
}

.action-btn:hover:not(:disabled)::before {
  left: 100%;
}

.action-btn:disabled {
  background: rgba(255, 255, 255, 0.2);
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

.action-btn:active:not(:disabled) {
  transform: translateY(-1px);
}

/* 评分信息 - 毛玻璃风格 */
.score-info {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.total-score {
  text-align: center;
  padding: 12px 0;
}

/* 分数圆环 - 炫彩发光风格 */
.score-circle {
  width: 90px;
  height: 90px;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 auto;
  position: relative;
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  border: 3px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 0 20px rgba(147, 112, 219, 0.3),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
  animation: pulse-glow 2s ease-in-out infinite;
}

@keyframes pulse-glow {
  0%, 100% {
    box-shadow: 
      0 0 20px rgba(147, 112, 219, 0.3),
      inset 0 0 20px rgba(255, 255, 255, 0.1);
  }
  50% {
    box-shadow: 
      0 0 30px rgba(147, 112, 219, 0.5),
      inset 0 0 20px rgba(255, 255, 255, 0.15);
  }
}

.score-circle::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: 50%;
  border: 3px solid currentColor;
  opacity: 0.4;
}

.score-circle.grade-s {
  color: #FFD700;
  background: linear-gradient(135deg, rgba(255, 215, 0, 0.2), rgba(255, 165, 0, 0.2));
  box-shadow: 
    0 0 30px rgba(255, 215, 0, 0.4),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}

.score-circle.grade-a {
  color: #4CAF50;
  background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(139, 195, 74, 0.2));
  box-shadow: 
    0 0 30px rgba(76, 175, 80, 0.4),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}

.score-circle.grade-b {
  color: #2196F3;
  background: linear-gradient(135deg, rgba(33, 150, 243, 0.2), rgba(100, 181, 246, 0.2));
  box-shadow: 
    0 0 30px rgba(33, 150, 243, 0.4),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}

.score-circle.grade-c {
  color: #FF9800;
  background: linear-gradient(135deg, rgba(255, 152, 0, 0.2), rgba(255, 183, 77, 0.2));
  box-shadow: 
    0 0 30px rgba(255, 152, 0, 0.4),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}

.score-circle.grade-d {
  color: #F44336;
  background: linear-gradient(135deg, rgba(244, 67, 54, 0.2), rgba(239, 83, 80, 0.2));
  box-shadow: 
    0 0 30px rgba(244, 67, 54, 0.4),
    inset 0 0 20px rgba(255, 255, 255, 0.1);
}

.score-number {
  font-size: 28px;
  font-weight: 700;
}

.score-label {
  font-size: 11px;
  opacity: 0.7;
}

/* 等级徽章 - 炫彩发光风格 */
.grade-badge {
  display: inline-block;
  margin-top: 8px;
  padding: 6px 20px;
  border-radius: 20px;
  font-size: 18px;
  font-weight: 700;
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
  background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 
    0 4px 15px rgba(0, 0, 0, 0.2),
    0 0 20px rgba(147, 112, 219, 0.3);
  text-shadow: 0 0 10px currentColor;
}

/* 维度评分 - 毛玻璃风格 */
.dimension-scores h4,
.overall-comment h4,
.suggestions h4 {
  font-size: 13px;
  margin-bottom: 10px;
  color: var(--main_text_color);
}

.dimension-item {
  margin-bottom: 12px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
}

.dimension-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
}

.dimension-name {
  font-size: 12px;
  color: var(--main_text_color);
  opacity: 0.8;
}

.dimension-score {
  font-size: 12px;
  font-weight: 600;
  color: var(--purple_text_color);
}

.dimension-bar {
  height: 5px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 3px;
  overflow: hidden;
}

.dimension-fill {
  height: 100%;
  background: var(--gradient);
  border-radius: 3px;
  transition: width 0.5s ease;
}

.dimension-comment {
  font-size: 11px;
  color: var(--main_text_color);
  opacity: 0.7;
  margin-top: 4px;
  line-height: 1.4;
}

/* 总体评价和建议 - 毛玻璃风格 */
.overall-comment,
.suggestions {
  padding: 10px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  backdrop-filter: blur(var(--card_filter));
  -webkit-backdrop-filter: blur(var(--card_filter));
}

.overall-comment p,
.suggestions li {
  font-size: 12px;
  color: var(--main_text_color);
  opacity: 0.8;
  line-height: 1.5;
}

.suggestions ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.suggestions li {
  position: relative;
  padding-left: 16px;
  margin-bottom: 6px;
}

.suggestions li::before {
  content: '💡';
  position: absolute;
  left: 0;
  font-size: 11px;
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

.left-tag-item.active {
  color: #9370DB;
  font-weight: bold;
}

/* 响应式设计 */
@media (max-width: 1200px) {
  .arena-layout {
    grid-template-columns: 1fr;
    height: auto;
  }
  
  .main-panel {
    min-height: 500px;
  }
  
  .score-panel {
    max-height: 400px;
  }
}

@media (max-width: 768px) {
  .arena-container {
    width: 100%;
  }
  
  .arena-content {
    padding: 10px;
  }
  
  .arena-layout {
    gap: 10px;
  }
  
  .quest-info-compact {
    gap: 6px;
  }
  
  .quest-scenario,
  .quest-objective {
    font-size: 12px;
  }
}
</style>
