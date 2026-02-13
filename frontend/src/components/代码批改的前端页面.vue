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
          Hello I' m <span class="gradientText">师小助 </span>
        </div>
          <div class="description">
            ✨ <span class="purpleText">代码批改</span> 功能可以帮助您快速批改学生的代码，自动识别错误并给出详细分析和优化建议。
          </div>
      </header>
      <content>
        <div class="title">
          <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
            <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
          </svg>
          输入代码
        </div>
        
        <!-- 代码输入区域 -->
        <div class="inputArea">
          <div class="inputMethodSelector">
            <label>
              <input type="radio" v-model="inputMethod" value="manual" checked>
              手动输入
            </label>
            <label>
              <input type="radio" v-model="inputMethod" value="file">
              文件上传
            </label>
          </div>
          
          <!-- 手动输入模式 -->
          <div v-if="inputMethod === 'manual'" class="manualInput">
            <div class="codeInput">
              <h3>代码内容</h3>
              <textarea 
                v-model="codeContent" 
                placeholder="请输入要批改的代码..."
                rows="12"
              ></textarea>
            </div>
          </div>
          
          <!-- 文件上传模式 -->
          <div v-if="inputMethod === 'file'" class="fileUpload">
            <div class="uploadBox" @click="triggerFileUpload">
              <input 
                type="file" 
                ref="codeFileInput" 
                accept=".py,.java,.c,.cpp,.js,.html,.css,.ts,.php" 
                style="display: none;"
                @change="handleFileUpload"
              >
              <svg t="1705773709627" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1478" style="width: 48px; height: 48px; margin-bottom: 16px;">
                <path d="M512 249.976471c-99.388235 0-180.705882 81.317647-180.705882 180.705882s81.317647 180.705882 180.705882 180.705882 180.705882-81.317647 180.705882-180.705882-81.317647-180.705882-180.705882-180.705882z m0 301.17647c-66.258824 0-120.470588-54.211765-120.470588-120.470588s54.211765-120.470588 120.470588-120.470588 120.470588 54.211765 120.470588 120.470588-54.211765 120.470588-120.470588 120.470588z" p-id="1479"></path>
                <path d="M512 39.152941c-216.847059 0-391.529412 174.682353-391.529412 391.529412 0 349.364706 391.529412 572.235294 391.529412 572.235294s391.529412-222.870588 391.529412-572.235294c0-216.847059-174.682353-391.529412-391.529412-391.529412z m0 891.482353C424.658824 873.411765 180.705882 686.682353 180.705882 430.682353c0-183.717647 147.576471-331.294118 331.294118-331.294118s331.294118 147.576471 331.294118 331.294118c0 256-243.952941 442.729412-331.294118 499.952941z" p-id="1480"></path>
              </svg>
              <p>{{ fileName || '点击上传代码文件' }}</p>
            </div>
          </div>
        </div>
        
        <!-- 额外问题输入 -->
        <div class="questionInput">
          <h3>额外问题（可选）</h3>
          <input 
            type="text" 
            v-model="question" 
            placeholder="如：请分析这段代码的时间复杂度，或请指出其中的错误..."
          >
        </div>
        
        <!-- 批改操作区域 -->
        <div class="actionArea">
          <button 
            class="reviewButton" 
            :disabled="!canReview || isProcessing"
            @click="startReview"
          >
            {{ isProcessing ? '批改中...' : '开始代码批改' }}
          </button>
        </div>
        
        <!-- 批改结果区域 -->
        <div v-if="reviewResult" class="resultArea">
          <div class="title">
            <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
              <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
            </svg>
            批改结果
          </div>
          <div class="resultContent" v-html="formattedReviewResult"></div>
        </div>
      </content>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { getServiceUrl } from '../config/api';

const router = useRouter();
const CODE_CORRECTION_URL = getServiceUrl('CODE_CORRECTION_SERVICE');

const goHome = () => {
  router.push('/');
};
const inputMethod = ref('manual');

const codeContent = ref('');

const codeFileInput = ref(null);
const codeFile = ref(null);
const fileName = ref('');

const question = ref('');

const isProcessing = ref(false);
const reviewResult = ref('');

const canReview = computed(() => {
  if (inputMethod.value === 'manual') {
    return codeContent.value.trim() !== '';
  } else {
    return codeFile.value !== null;
  }
});

const triggerFileUpload = () => {
  codeFileInput.value?.click();
};

const handleFileUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    codeFile.value = file;
    fileName.value = file.name;
  }
};

const formattedReviewResult = computed(() => {
  if (!reviewResult.value) return '';
  
  let html = reviewResult.value;
  
  html = html.replace(/^## (.*$)/gm, '<h2>$1</h2>');
  html = html.replace(/^# (.*$)/gm, '<h1>$1</h1>');
  
  html = html.replace(/^- (.*$)/gm, '<li>$1</li>');
  html = html.replace(/(<li>.*<\/li>)/gs, '<ul>$1</ul>');
  
  html = html.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
  
  html = html.replace(/\n/g, '<br>');
  
  return html;
});

const startReview = async () => {
  if (!canReview.value || isProcessing.value) return;
  
  isProcessing.value = true;
  reviewResult.value = '';
  
  try {
    const formData = new FormData();
    
    if (inputMethod.value === 'manual') {
      formData.append('code', codeContent.value.trim());
    } else {
      formData.append('file', codeFile.value);
    }
    
    if (question.value.trim()) {
      formData.append('question', question.value.trim());
    }
    
    const response = await fetch(`${CODE_CORRECTION_URL}/review_code`, {
      method: 'POST',
      body: formData
    });
    
    const result = await response.json();
    
    if (result.status !== 'success') {
      throw new Error(result.message || '批改失败');
    }
    
    reviewResult.value = result.data;
  } catch (error) {
    console.error('批改错误:', error);
    alert('批改过程中发生错误，请稍后重试');
  } finally {
    isProcessing.value = false;
  }
};
</script>

<style scoped>
.inputArea {
  margin-bottom: 30px;
}

.inputMethodSelector {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  padding: 16px;
  background-color: #f5f5f5;
  border-radius: 8px;
}

.inputMethodSelector label {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  
  /* --- 新增/修改以下样式 --- */
  color: #333333;      /* 将文字改为深黑色，对比度更高 */
  font-weight: 600;    /* 加粗字体，让文字更清晰 */
  font-size: 16px;     /* 稍微调大字号（可选） */
}
.inputMethodSelector label:hover {
  color: #9370DB;      /* 悬停时变成你的主题紫色 */
}
/* 手动输入样式 */
.manualInput {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.codeInput h3 {
  margin: 0 0 12px 0;
  color: #333;
}

.codeInput textarea {
  width: 100%;
  padding: 12px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 14px;
  font-family: 'Courier New', Courier, monospace;
  resize: vertical;
  transition: border-color 0.3s ease;
}

.codeInput textarea:focus {
  outline: none;
  border-color: #9370DB;
  box-shadow: 0 0 0 3px rgba(147, 112, 219, 0.1);
}

/* 文件上传样式 */
.fileUpload {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.uploadBox {
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 32px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #f9f9f9;
}

.uploadBox:hover {
  border-color: #9370DB;
  background-color: #f0f0ff;
}

/* 问题输入样式 */
.questionInput {
  margin-bottom: 30px;
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.questionInput h3 {
  margin: 0 0 12px 0;
  color: #333;
}

.questionInput input {
  width: 100%;
  padding: 12px;
  border: 2px solid #ccc;
  border-radius: 8px;
  font-size: 14px;
  transition: border-color 0.3s ease;
}

.questionInput input:focus {
  outline: none;
  border-color: #9370DB;
  box-shadow: 0 0 0 3px rgba(147, 112, 219, 0.1);
}

/* 操作区域样式 */
.actionArea {
  text-align: center;
  margin-bottom: 30px;
}

.reviewButton {
  background-color: #9370DB;
  color: white;
  border: none;
  padding: 16px 32px;
  font-size: 18px;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.reviewButton:hover:not(:disabled) {
  background-color: #7B68EE;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.reviewButton:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  transform: none;
  box-shadow: none;
}

/* 结果区域样式 */
.resultArea {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 24px;
  margin-top: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.resultContent {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: #333333;
}

/* 使用 :deep() 穿透作用域，影响 v-html 生成的标签 */
.resultContent :deep(h1) {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #000000;
}

.resultContent :deep(h2) {
  font-size: 20px;
  font-weight: bold;
  margin: 16px 0 8px 0;
  color: #333333;
}

.resultContent :deep(ul) {
  margin: 8px 0;
  padding-left: 20px;
}

.resultContent :deep(li) {
  margin: 4px 0;
  color: #444444;
}

.resultContent :deep(pre) {
  background-color: #f0f0f0;
  border-radius: 4px;
  padding: 12px;
  overflow-x: auto;
  margin: 8px 0;
}

.resultContent :deep(code) {
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #333;
}

.left-tag-item.active {
  color: #9370DB;
  font-weight: bold;
}
/* 确保 header 能够作为定位基准 (原代码中 header 可能没有 position 属性，需加上) */
header {
  position: relative; /* 关键：让绝对定位的按钮相对于 header 定位 */
}

/* 返回按钮样式 */
.back-home-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #9370DB; /* 主题紫色 */
  border: 1px solid #9370DB;
  border-radius: 20px; /* 圆角胶囊形状 */
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  z-index: 10;
}

.back-home-btn svg {
  fill: currentColor; /* 让图标颜色跟随文字颜色 */
  margin-top: -2px;   /* 微调图标位置 */
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