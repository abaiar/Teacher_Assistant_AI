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
          <router-link to="/prompt-arena" class="left-tag-item">提示词竞技场</router-link>
        </div>
      <div class="left-div left-time">
        <ul id="line">
          <li>
            <div class="focus"></div>
            <div>敬请期待</div>
            <div>2026.3</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>进军人工智能通识教育</div>
            <div>2026.2</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>服务器部署</div>
            <div>2026.1</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>Langchain版本V2.0</div>
            <div>2025.12</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>Langchain版本V1.0</div>
            <div>2025.11</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>进行全面升级</div>
            <div>2025.9</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>完成初版</div>
            <div>2025.8</div>
          </li>
          <li>
            <div class="focus"></div>
            <div>项目启动</div>
            <div>2025.7</div>
          </li>
        </ul>
      </div>
    </div>
    <div class="zyyo-right">
      <header>
        <button class="logout-btn" @click="handleLogout" title="退出登录">
          <svg viewBox="0 0 1024 1024" width="16" height="16">
            <circle cx="512" cy="512" r="450" fill="currentColor"/>
          </svg>
          退出
        </button>
        <div class="index-logo" style="background-image: url('../../static/img/logo.png');">
          <img style="position: absolute;top:-15%;left:-10%;width: 120%; aspect-ratio: 1/1;" src="../../static/img/logokuang.png">
        </div>
        <div class="welcome">
          Hello I' m <span class="gradientText">师小助 </span>
        </div>
        <div class="description">
          📝 <span class="purpleText">师小助</span> 是一款为教师提供 
          <span class="purpleText textBackground">智能批改</span> 
          <span class="purpleText textBackground">成绩分析</span>  
          <span class="purpleText textBackground">智能组卷</span> 
          <span class="purpleText textBackground">代码分析</span>
          功能提高教学效率的教师辅助工具。
        </div>
        <div class="description">
          👦 我们在下方提供 <span class="purpleText textBackground">启动按键</span> 及 
          <span class="purpleText textBackground">使用教程</span>，建议用户在启动前先观看教程，以确保正常使用。
        </div>
        <div class="description">
          🚀 <span class="purpleText">师小助</span> 目前处于初始阶段，未来将持续更新和完善，敬请期待！
        </div>
        <div class="iconContainer">
          <a class="iconItem" href="https://github.com/abaiar/Teacher_Assistant_AI" target="_blank">
            <svg t="1704870335945" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2487">
              <path d="M511.6 76.3C264.3 76.2 64 276.4 64 523.5 64 718.9 189.3 885 363.8 946c23.5 5.9 19.9-10.8 19.9-22.2v-77.5c-135.7 15.9-141.2-73.9-150.3-88.9C215 726 171.5 718 184.5 703c30.9-15.9 62.4 4 98.9 57.9 26.4 39.1 77.9 32.5 104 26 5.7-23.5 17.9-44.5 34.7-60.8-140.6-25.2-199.2-111-199.2-213 0-49.5 16.3-95 48.3-131.7-20.4-60.5 1.9-112.3 4.9-120 58.1-5.2 118.5 41.6 123.2 45.3 33-8.9 70.7-13.6 112.9-13.6 42.4 0 80.2 4.9 113.5 13.9 11.3-8.6 67.3-48.8 121.3-43.9 2.9 7.7 24.7 58.3 5.5 118 32.4 36.8 48.9 82.7 48.9 132.3 0 102.2-59 188.1-200 212.9 23.5 23.2 38.1 55.4 38.1 91v112.5c0.8 9 0 17.9 15 17.9 177.1-59.7 304.6-227 304.6-424.1 0-247.2-200.4-447.3-447.5-447.3z"  p-id="2488"></path>
            </svg>
            <div class="iconTip">Github</div>
          </a>
          <a class="iconItem" href="https://qm.qq.com/q/iJCJ0Frfe8" target="_blank">
            <svg t="1704870588438" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="3174" >
              <path d="M926.47619 355.644952V780.190476a73.142857 73.142857 0 0 1-73.142857 73.142857H170.666667a73.142857 73.142857 0 0 1-73.142857-73.142857V355.644952l304.103619 257.828572a170.666667 170.666667 0 0 0 220.745142 0L926.47619 355.644952zM853.333333 170.666667a74.044952 74.044952 0 0 1 26.087619 4.778666 72.704 72.704 0 0 1 30.622477 22.186667 73.508571 73.508571 0 0 1 10.678857 17.67619c3.169524 7.509333 5.12 15.652571 5.607619 24.210286L926.47619 243.809524v24.380952L559.469714 581.241905a73.142857 73.142857 0 0 1-91.306666 2.901333l-3.632762-2.925714L97.52381 268.190476v-24.380952a72.899048 72.899048 0 0 1 40.155428-65.292191A72.97219 72.97219 0 0 1 170.666667 170.666667h682.666666z"  p-id="3175"></path>
            </svg>
            <div class="iconTip">Mail</div>
          </a>
          <a class="iconItem" @click="pop('../../static/img/qq.jpg')" href="javascript:void(0)">
            <svg t="1712319361023" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1861">
              <path d="M824.8 613.2c-16-51.4-34.4-94.6-62.7-165.3C766.5 262.2 689.3 112 511.5 112 331.7 112 256.2 265.2 261 447.9c-28.4 70.8-46.7 113.7-62.7 165.3-34 109.5-23 154.8-14.6 155.8 18 2.2 70.1-82.4 70.1-82.4 0 49 25.2 112.9 79.8 159-26.4 8.1-85.7 29.9-71.6 53.8 11.4 19.3 196.2 12.3 249.5 6.3 53.3 6 238.1 13 249.5-6.3 14.1-23.8-45.3-45.7-71.6-53.8 54.6-46.2 79.8-110.1 79.8-159 0 0 52.1 84.6 70.1 82.4 8.5-1.1 19.5-46.4-14.5-155.8z" p-id="1862"></path>
            </svg>
            <div class="iconTip">QQ</div>
          </a>
          <a class="switch" href="javascript:void(0)">
                    <div class="onoffswitch">
            <input type="checkbox" name="onoffswitch" class="onoffswitch-checkbox" id="myonoffswitch" @click="toggleMode">
            <label class="onoffswitch-label" for="myonoffswitch">
                <span class="onoffswitch-inner"></span>
                <span class="onoffswitch-switch"></span>
            </label>
        </div>
          </a>
        </div>
        <div class="tanChiShe">
          <img id="tanChiShe" src="../../static/svg/snake-Light.svg" alt="">
        </div>
      </header>
      <content>
        <div class="title">
          <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
            <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z"  p-id="1892"></path>
          </svg>
          人工智能通识教育 
        </div>
        <div class="projectList">
          <a class="projectItem ai-course-item" target="_self" href="https://www.bilibili.com/video/BV1Je44zFEtJ/?spm_id_from=333.1387.homepage.video_card.click&vd_source=d0a9d0769d591135f53266e046b649ff">
            <div class="ai-course-content gradientText">The Future Is Now, Step In</div>
          </a>
        </div>
        <div class="title">
          <svg t="1705257422086" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1891">
            <path d="M629.333333 202.666667v213.333333h277.333334v448h-512v-213.333333h-277.333334v-448h512z m213.333334 277.333333h-213.333334v170.666667h-170.666666v149.333333h384v-320z m-277.333334-213.333333h-384v320h213.333334v-170.666667h170.666666v-149.333333z m0 213.333333h-106.666666v106.666667h106.666666v-106.666667z" p-id="1892"></path>
          </svg>
          基础功能 
        </div>
        <div class="projectList">
          <!-- 智能批改项目 - 使用Vue Router跳转 -->
          <router-link class="projectItem a" to="/intelligent-correction">
            <div class="projectItemLeft">
              <h1>智能批改</h1>
              <p>一键批改学生试题并给出分析结果</p>
            </div>
            <div class="projectItemRight">
              <img src="../../static/img/i1.png" alt="">
            </div>
          </router-link>
          <!-- 成绩分析项目 - 使用Vue Router跳转 -->
          <router-link class="projectItem b" to="/score-analysis">
            <div class="projectItemLeft">
              <h1>成绩分析</h1>
              <p>分析学生成绩，给出建议及发展规划</p>
            </div>
            <div class="projectItemRight">
              <img src="../../static/img/i2.png" alt="">
            </div>
          </router-link>
          <!-- 智能组卷项目 - 使用Vue Router跳转 -->
          <router-link class="projectItem a" to="/intelligent-quiz">
            <div class="projectItemLeft">
              <h1>智能组卷</h1>
              <p>根据用户需求，自动组卷</p>
            </div>
            <div class="projectItemRight">
              <img src="../../static/img/i3.png" alt="">
            </div>
          </router-link>
          <!-- 代码批改项目 - 使用Vue Router跳转 -->
          <router-link class="projectItem b" to="/code-review">
            <div class="projectItemLeft">
              <h1>代码批改</h1>
              <p>评测学生代码，进行打分</p>
            </div>
            <div class="projectItemRight">
              <img src="../../static/img/i4.png" alt="">
            </div>
          </router-link>
          <!-- 提示词竞技场项目 - 使用Vue Router跳转 -->
          <router-link class="projectItem a" to="/prompt-arena">
            <div class="projectItemLeft">
              <h1>提示词竞技场</h1>
              <p>训练提示词编写能力，提升AI交互效果</p>
            </div>
            <div class="projectItemRight">
              <img src="../../static/img/i5.png" alt="">
            </div>
          </router-link>
        </div>
      </content>
    </div>
  </div>
  <div class="tc">
    <div onclick="" class="tc-main">
      <img class="tc-img" src="" alt="" srcset="">
    </div>
  </div>
</template>

<script>
import { useRouter } from 'vue-router'
import { useUserStore } from '../store/user'

export default {
  name: 'Index',
  methods: {
    pop(imagePath) {
      // 这里实现图片弹窗功能
      const tc = document.querySelector('.tc')
      const tcImg = document.querySelector('.tc-img')
      tcImg.src = imagePath
      tc.style.display = 'block'
    },
    toggleMode() {
      const html = document.documentElement;
      const tanChiSheImg = document.getElementById('tanChiShe');
      // 判断当前是否已经是夜间模式
      if (html.getAttribute('data-theme') === 'Dark') {
        // 如果是，切换回白天模式
        html.removeAttribute('data-theme');
        html.classList.remove('Dark');
        // 切换为白天模式图片
        if (tanChiSheImg) {
          tanChiSheImg.src = '../../static/svg/snake-Light.svg';
        }
      } else {
        // 如果不是，切换到夜间模式
        html.setAttribute('data-theme', 'Dark');
        html.classList.add('Dark');
        // 切换为夜间模式图片
        if (tanChiSheImg) {
          tanChiSheImg.src = '../../static/svg/snake-Dark.svg';
        }
      }
    },
    handleLogout() {
      // 确认是否退出登录
      if (confirm('确定要退出登录吗？')) {
        // 退出登录
        const userStore = useUserStore()
        userStore.logout()
        this.$router.push('/login')
      }
    }
  },
  mounted() {
    // 页面加载完成后执行的初始化操作
    // 可以在这里添加原script.js中的一些功能
  }
}
</script>

<style scoped>
/* 页面特定的样式可以在这里添加 */

/* 确保 header 能够作为定位基准 */
header {
  position: relative;
}

/* 退出登录按钮样式 - 红色调 */
.logout-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  background-color: rgba(255, 255, 255, 0.9);
  color: #dc3545; /* 红色主题 */
  border: 1px solid #dc3545;
  border-radius: 20px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  z-index: 10;
}

.logout-btn svg {
  fill: currentColor;
  margin-top: -2px;
}

.logout-btn:hover {
  background-color: #dc3545;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(220, 53, 69, 0.3);
}

.logout-btn:active {
  transform: translateY(0);
}

/* AI Literacy 大图标样式 - 与师小助标题风格一致 */
.ai-course-item {
  width: calc(100% - 15px) !important;
  display: flex !important;
  justify-content: center !important;
  align-items: center !important;
  text-decoration: none !important;
  height: 120px !important;
  border-radius: 12px !important;
  background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%) !important;
  border: 1px solid rgba(255,255,255,0.1) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1) !important;
  transition: all 0.4s ease !important;
  position: relative;
  overflow: hidden;
}

.ai-course-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
  transition: left 0.5s ease;
}

.ai-course-item:hover::before {
  left: 100%;
}

.ai-course-item:hover {
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15) !important;
  border-color: rgba(255,255,255,0.2) !important;
}

.ai-course-content {
  font-size: 42px;
  font-weight: 700;
  text-align: center;
  letter-spacing: 2px;
  font-family: "title", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  /* gradientText 样式由全局 CSS 提供 */
}

.ai-course-item:hover .ai-course-content {
  transform: scale(1.05);
  transition: transform 0.4s ease;
}

/* 响应式适配 */
@media (max-width: 768px) {
  .ai-course-content {
    font-size: 32px;
    letter-spacing: 1px;
  }
  
  .ai-course-item {
    height: 100px !important;
  }
}

@media (max-width: 480px) {
  .ai-course-content {
    font-size: 24px;
    letter-spacing: 0.5px;
  }
  
  .ai-course-item {
    height: 80px !important;
  }
}
</style>
