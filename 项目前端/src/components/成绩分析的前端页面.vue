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
        <router-link to="/score-analysis" class="left-tag-item active">成绩分析</router-link>
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
          📊 <span class="purpleText">成绩分析</span> 功能可以帮助您分析学生的成绩趋势，提供学习建议和生涯规划。
        </div>
      </header>
      <content>
        <div class="title">
          <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
            <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
          </svg>
          输入学生数据
        </div>
        
        <!-- 学生数据输入区域 -->
        <div class="inputArea">
          <div class="inputMethodSelector">
            <label>
              <input type="radio" v-model="inputMethod" value="manual" checked>
              手动输入
            </label>
            <label>
              <input type="radio" v-model="inputMethod" value="csv">
              CSV上传
            </label>
          </div>
          
          <!-- 手动输入模式 -->
          <div v-if="inputMethod === 'manual'" class="manualInput">
            <div class="studentForm">
              <h3>学生信息</h3>
              <div class="formRow">
                <div class="formGroup">
                  <label>姓名</label>
                  <input type="text" v-model="currentStudent.name" placeholder="请输入学生姓名">
                </div>
                <div class="formGroup">
                  <label>考试类型</label>
                  <input type="text" v-model="currentStudent.examType" placeholder="如：期中/期末/月考">
                </div>
              </div>
              
              <h3>各科成绩</h3>
              <div class="scoresGrid">
                <div class="formGroup" v-for="subject in subjects" :key="subject">
                  <label>{{ subject }}</label>
                  <input type="number" v-model.number="currentStudent.scores[subject]" placeholder="分数">
                </div>
              </div>
              
              <div class="formGroup">
                <label>兴趣爱好</label>
                <input type="text" v-model="currentStudent.interests" placeholder="请输入学生的兴趣爱好">
              </div>
              
              <div class="formActions">
                <button class="addButton" @click="addStudent" :disabled="!isCurrentStudentValid">
                  添加学生
                </button>
              </div>
            </div>
            
            <!-- 已添加的学生列表 -->
            <div v-if="students.length > 0" class="studentsList">
              <h3>已添加学生 ({{ students.length }} 人)</h3>
              <div class="studentsTable">
                <table>
                  <thead>
                    <tr>
                      <th>姓名</th>
                      <th>考试类型</th>
                      <th>语文</th>
                      <th>数学</th>
                      <th>英语</th>
                      <th>物理</th>
                      <th>化学</th>
                      <th>生物</th>
                      <th>兴趣爱好</th>
                      <th>操作</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr v-for="(student, index) in students" :key="index">
                      <td>{{ student.name }}</td>
                      <td>{{ student.examType }}</td>
                      <td>{{ student.scores.语文 || '-' }}</td>
                      <td>{{ student.scores.数学 || '-' }}</td>
                      <td>{{ student.scores.英语 || '-' }}</td>
                      <td>{{ student.scores.物理 || '-' }}</td>
                      <td>{{ student.scores.化学 || '-' }}</td>
                      <td>{{ student.scores.生物 || '-' }}</td>
                      <td>{{ student.interests || '-' }}</td>
                      <td>
                        <button class="deleteButton" @click="deleteStudent(index)">
                          删除
                        </button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          
          <!-- CSV上传模式 -->
          <div v-if="inputMethod === 'csv'" class="csvUpload">
            <div class="uploadBox" @click="triggerCsvUpload">
              <input 
                type="file" 
                ref="csvFileInput" 
                accept=".csv" 
                style="display: none;"
                @change="handleCsvUpload"
              >
              <svg t="1705773709627" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1478" style="width: 48px; height: 48px; margin-bottom: 16px;">
                <path d="M512 249.976471c-99.388235 0-180.705882 81.317647-180.705882 180.705882s81.317647 180.705882 180.705882 180.705882 180.705882-81.317647 180.705882-180.705882-81.317647-180.705882-180.705882-180.705882z m0 301.17647c-66.258824 0-120.470588-54.211765-120.470588-120.470588s54.211765-120.470588 120.470588-120.470588 120.470588 54.211765 120.470588 120.470588-54.211765 120.470588-120.470588 120.470588z" p-id="1479"></path>
                <path d="M512 39.152941c-216.847059 0-391.529412 174.682353-391.529412 391.529412 0 349.364706 391.529412 572.235294 391.529412 572.235294s391.529412-222.870588 391.529412-572.235294c0-216.847059-174.682353-391.529412-391.529412-391.529412z m0 891.482353C424.658824 873.411765 180.705882 686.682353 180.705882 430.682353c0-183.717647 147.576471-331.294118 331.294118-331.294118s331.294118 147.576471 331.294118 331.294118c0 256-243.952941 442.729412-331.294118 499.952941z" p-id="1480"></path>
              </svg>
              <p>{{ csvFileName || '点击上传CSV文件' }}</p>
            </div>
          </div>
        </div>
        
        <!-- 分析操作区域 -->
        <div class="actionArea">
          <button 
            class="analysisButton" 
            :disabled="!canAnalyze || isProcessing"
            @click="startAnalysis"
          >
            {{ isProcessing ? '分析中...' : '开始成绩分析' }}
          </button>
        </div>
        
        <!-- 分析结果区域 -->
        <div v-if="analysisResults.length > 0" class="resultArea">
          <div class="title">
            <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
              <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
            </svg>
            分析结果
          </div>
          
          <!-- 学生选择器 -->
          <div class="studentSelector">
            <select v-model="selectedStudent" @change="loadStudentResults">
              <option value="">请选择学生</option>
              <option v-for="student in analysisResults" :key="student.name" :value="student.name">
                {{ student.name }}
              </option>
            </select>
          </div>
          
          <!-- 结果显示 -->
          <div v-if="selectedStudentResults" class="resultContent">
            <div class="resultSection">
              <h3>📈 成绩分析报告</h3>
              <div class="resultText">{{ selectedStudentResults.analysis }}</div>
            </div>
            
            <div class="resultSection">
              <h3>📝 短期学习计划</h3>
              <div class="resultText">{{ selectedStudentResults.shortPlan }}</div>
            </div>
            
            <div class="resultSection">
              <h3>🗓️ 长期学习计划</h3>
              <div class="resultText">{{ selectedStudentResults.longPlan }}</div>
            </div>
            
            <div class="resultSection">
              <h3>🎯 生涯规划建议</h3>
              <div class="resultText">{{ selectedStudentResults.careerAdvice }}</div>
            </div>
            
            <div class="resultSection">
              <h3>💫 鼓励话语</h3>
              <div class="resultText">{{ selectedStudentResults.encouragement }}</div>
            </div>
          </div>
        </div>
      </content>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const goHome = () => {
  router.push('/');
};
// 输入方法选择
const inputMethod = ref('manual');

// 科目列表
const subjects = ['语文', '数学', '英语', '物理', '化学', '生物'];

// 当前输入的学生信息
const currentStudent = ref({
  name: '',
  examType: '',
  scores: {},
  interests: ''
});

// 已添加的学生列表
const students = ref([]);

// CSV文件相关
const csvFileInput = ref(null);
const csvFile = ref(null);
const csvFileName = ref('');

// 分析相关
const isProcessing = ref(false);
const analysisResults = ref([]);
const selectedStudent = ref('');
const selectedStudentResults = ref(null);

// 检查当前学生信息是否有效
const isCurrentStudentValid = computed(() => {
  return currentStudent.value.name && 
         currentStudent.value.examType &&
         Object.values(currentStudent.value.scores).some(score => score !== undefined && score !== null && score !== '');
});

// 检查是否可以开始分析
const canAnalyze = computed(() => {
  if (inputMethod.value === 'manual') {
    return students.value.length > 0;
  } else {
    return csvFile.value !== null;
  }
});

// 添加学生
const addStudent = () => {
  if (!isCurrentStudentValid.value) return;
  
  // 创建学生数据副本
  const studentData = {
    name: currentStudent.value.name,
    examType: currentStudent.value.examType,
    scores: { ...currentStudent.value.scores },
    interests: currentStudent.value.interests
  };
  
  students.value.push(studentData);
  
  // 重置表单
  currentStudent.value = {
    name: '',
    examType: '',
    scores: {},
    interests: ''
  };
};

// 删除学生
const deleteStudent = (index) => {
  students.value.splice(index, 1);
};

// 触发CSV文件上传
const triggerCsvUpload = () => {
  csvFileInput.value?.click();
};

// 处理CSV文件上传
const handleCsvUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    csvFile.value = file;
    csvFileName.value = file.name;
  }
};

// 开始分析
const startAnalysis = async () => {
  if (!canAnalyze.value || isProcessing.value) return;
  
  isProcessing.value = true;
  analysisResults.value = [];
  selectedStudent.value = '';
  selectedStudentResults.value = null;
  
  try {
    let formData = new FormData();
    
    if (inputMethod.value === 'manual') {
      // 手动输入模式，发送JSON数据
      formData.append('dataType', 'json');
      formData.append('students', JSON.stringify(students.value));
    } else {
      // CSV上传模式，发送文件
      formData.append('dataType', 'csv');
      formData.append('file', csvFile.value);
    }
    
    const response = await fetch('http://localhost:5003/analyze', {
      method: 'POST',
      body: formData
    });
    
    if (!response.ok) {
      throw new Error('分析失败');
    }
    
    const results = await response.json();
    analysisResults.value = results;
    
    // 默认选择第一个学生的结果
    if (results.length > 0) {
      selectedStudent.value = results[0].name;
      loadStudentResults();
    }
  } catch (error) {
    console.error('分析错误:', error);
    alert('分析过程中发生错误，请稍后重试');
  } finally {
    isProcessing.value = false;
  }
};

// 加载选中学生的结果
const loadStudentResults = () => {
  if (!selectedStudent.value) {
    selectedStudentResults.value = null;
    return;
  }
  
  selectedStudentResults.value = analysisResults.value.find(student => student.name === selectedStudent.value);
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
  
  /* --- 新增/修改样式开始 --- */
  color: #333333;               /* 字体改为深黑色，清晰可见 */
  font-weight: bold;            /* 字体加粗 */
  font-size: 16px;              /* 稍微调大字号 */
  transition: color 0.3s ease;  /* 添加颜色变化的过渡动画，更顺滑 */
  /* --- 新增/修改样式结束 --- */
}

/* --- 新增悬停效果 --- */
.inputMethodSelector label:hover {
  color: #9370DB;               /* 鼠标悬停时变成主题紫色 */
}

/* 手动输入样式 */
.manualInput {
  background-color: #f9f9f9;
  border-radius: 8px;
  padding: 20px;
}

.studentForm h3 {
  margin: 16px 0 8px 0;
  color: #333;
}

.formRow {
  display: flex;
  gap: 20px;
  margin-bottom: 16px;
}

.formGroup {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.formGroup label {
  font-size: 14px;
  color: #666;
}

.formGroup input {
  padding: 10px;
  border: 2px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  transition: border-color 0.3s ease;
}

.formGroup input:focus {
  outline: none;
  border-color: #9370DB;
  box-shadow: 0 0 0 3px rgba(147, 112, 219, 0.1);
}

.scoresGrid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
  gap: 16px;
  margin-bottom: 16px;
}

.formActions {
  margin-top: 20px;
  text-align: right;
}

.addButton {
  background-color: #9370DB;
  color: white;
  border: none;
  padding: 10px 20px;
  font-size: 14px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.addButton:hover:not(:disabled) {
  background-color: #7B68EE;
}

.addButton:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

/* 学生列表样式 */
.studentsList {
  margin-top: 24px;
  background-color: white;
  border-radius: 8px;
  padding: 16px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.studentsTable {
  overflow-x: auto;
}

.studentsTable table {
  width: 100%;
  border-collapse: collapse;
}

.studentsTable th,
.studentsTable td {
  padding: 10px;
  text-align: left;
  border-bottom: 1px solid #eee;
}

.studentsTable th {
  background-color: #f5f5f5;
  font-weight: bold;
  color: #333;
}

.deleteButton {
  background-color: #ff4d4f;
  color: white;
  border: none;
  padding: 6px 12px;
  font-size: 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.deleteButton:hover {
  background-color: #ff7875;
}

/* CSV上传样式 */
.csvUpload {
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

/* 操作区域样式 */
.actionArea {
  text-align: center;
  margin-bottom: 30px;
}

.analysisButton {
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

.analysisButton:hover:not(:disabled) {
  background-color: #7B68EE;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.analysisButton:disabled {
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

.studentSelector {
  margin-bottom: 20px;
}

.studentSelector select {
  width: 100%;
  padding: 12px;
  border: 2px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.studentSelector select:focus {
  outline: none;
  border-color: #9370DB;
  box-shadow: 0 0 0 3px rgba(147, 112, 219, 0.1);
}

.resultSection {
  margin-bottom: 24px;
  padding: 16px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
}

.resultSection h3 {
  margin-top: 0;
  margin-bottom: 12px;
  color: #333;
  font-size: 18px;
}

.resultText {
  line-height: 1.6;
  color: #555;
  white-space: pre-wrap;
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