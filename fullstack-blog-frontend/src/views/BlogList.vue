<template>
  <div class="blog">
    <!-- 上方搜索栏 -->
    <div class="ssl">
      <input type="text" class="search" placeholder="请输入内容……"
        @input="handleSearch"
        @focus="handleSearch"
        @blur="handleBlur">
      <!-- 搜索下拉列表框（大长方形），默认隐藏 -->
      <div 
        class="search-dropdown" 
        v-show="showDropdown && searchResultList.length > 0"
        @mousedown="handleDropdownMouseDown" 
      >
        <!-- 小长方形选项，循环渲染匹配到的文章标题 -->
        <div 
          class="search-item"
          v-for="item in searchResultList"
          :key="item.id"
          @click="selectItem(item)"
        >
          {{ item.title }}
        </div>
      </div>
    </div>
    <!-- 下方展示文章区域和发布文章区域 -->
    <div class="xmnr">
      <!-- 左边展示文章区域 -->
      <div class="sywz">
        <div class="fk" v-for="article in articleList" :key="article.id">
          <div class="a-card">
            <h3 class="a-title" @click="open(article)">{{ article.title }}</h3>
            <div class="a-meta">
              <div><span>作者：{{ article.author }}</span></div>
              <div><span>发布于：{{ article.publishTime }}</span></div>
            </div>
          </div>
        </div>
      </div>
      <!-- 中间间隔线 -->
      <div class="gk"></div>   
      <!-- 右边发布文章区域 -->
      <div class="fbwz">
        <div class="xfk2">
          <input type="text" id="title" placeholder="请输入文章标题">
          <input type="text" id="username" placeholder="用户名">    <!--  placeholder是提示文字 -->
          <textarea id="message" placeholder="留言内容……"></textarea>
          <button id="sub" @click="handlePublish">发布</button>
        </div>
      </div>
    </div>

    <!-- 文章内容弹窗（默认隐藏） -->
    <div class="m-over" v-if="MOpen" @click="close">
      <div class="m-content" @click.stop>
        <div class="m-body">
          <h3>{{currentArticle.title}}</h3>
          <p class="m-content-text">{{ currentArticle.content}}</p>
        </div>
        <div class="m-footer">
          <button class="m-close" @click="close">退出</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* 上方搜索栏容器 */
.ssl {
  position: relative;
  display: flex;
  justify-content: center;
  width: 100%;
  box-sizing: border-box;
  background-color: transparent; /* 背景透明，让里面的输入框更突出 */
}
.ssl .search {
  width: 80%; 
  max-width: 600px; 
  padding: 10px 16px; 
  background-color: #ffffff; 
  border: 1px solid #666666; 
  border-radius: 8px; 
  font-size: 14px;
  color: #333;
}
/* 激活状态的搜索栏 */
.ssl .search:focus {
  outline: none;
  border-color: #333;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.5);
}
.ssl .search::placeholder{
  color: #747373;
  opacity: 1;
}
.search-dropdown {
  position: absolute;
  top: 40px;
  left: 0;
  width: 300px; 
  max-height: 200px; 
  border: 1px solid #eee;
  background: #fff;
  overflow-y: auto;
  z-index: 999; 
  left: 50%;
  transform: translateX(-50%);
  margin-top: 10px;
}
.search-item {
  padding: 10px;
  border-bottom: 1px solid #f5f5f5;
  cursor: pointer;
}
.search-item:hover {
  background-color: #f5f5f5; /* 鼠标悬浮高亮 */
}

/* 下方主内容区 */
.xmnr {
  display: flex;
  align-items: flex-start;       /* 子元素顶部对齐 */
  padding: 20px;
  width: 100%;
  box-sizing: border-box;
  margin-top: 100px;
  margin-bottom: 100px;
}

/* 左边展示文章区域 */
.sywz {
  flex: 1;          /* 平分可用空间，与右边发布区等宽 */
  padding-right: 20px;
  box-sizing: border-box;
}
.a-card {
  width: 550px;
  background-color: #e2eff9;
  padding: 16px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
  margin-bottom: 0;
  cursor: pointer;           /* 鼠标悬浮时显示手型，暗示可点击 */
  margin-top: 50px;
  margin-left: 120px;
}
.a-title {
  font-size: 18px;
  font-weight: 600;
  margin: 0 0 8px 0;
  color: #212121;
  cursor: pointer;
}
.a-title:hover {
  color: #70b4f7;
}
.a-meta{
  display: flex;
  justify-content: space-between;
  font-size: 12px;
}


/* 中间分隔线 */
.gk {
  margin-top: 50px;
  width: 3px;
  background-color: #535f6c;
  height: 710px;
  flex-shrink: 0;            /* 防止被 flex 布局压缩，保持 1px 宽度 */
  margin-right: 128px;
}

/* 右边发布文章区域 */
.xfk2 {
  margin-top: 50px;
  margin-right: 120px;
  width: 550px;
  height: 700px;
  background-color: #e2eff9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: column;
  gap: 50px;

}
.xfk2 input:focus,
.xfk2 textarea:focus{
    outline: none;      /* 输入框/文本域取得焦点时，去除浏览器默认的外轮廓线 */
    border-color: #000;
    box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.5);
}
.xfk2 input,.xfk2 textarea{
  width: 85%;
  padding: 10px;
  border: 1px solid #4c5052;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}
.xfk2 #message{
  resize: none;             /* 禁止手动拉伸 */
  height: 180px;
}
.xfk2 #sub {
  align-self: flex-end;             
  margin-right: 7.5%;
  padding: 10px;
  background-color: #8ebee5;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  color: #30404f;
  width: 70px;
  height: 35px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #4c5052;
}
.xfk2 #sub:hover {
  background-color: #b2effd;
  box-shadow: 0 0 0 2px rgba(0, 0, 0, 0.5);
}

/* 文章内容弹窗 */
.m-over {
  position: fixed;    /* 固定定位，覆盖整个屏幕，无论页面怎么滚动都在最上层 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;            /* 使用 flex 布局，让弹窗内容水平垂直居中 */
  justify-content: center;
  align-items: center;
  z-index: 999;
}
.m-content {
  background-color: #c0dbec;
  padding: 24px;
  border-radius: 8px;
  max-width: 500px;
  width: 90%;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  gap: 20px;       /* 子元素之间的间距 20px */
}
.m-content-text {
  line-height: 1.8;
  color: #333333;
  word-wrap: break-word;        /* 长句自动换行，防止内容溢出弹窗 */
  white-space: pre-line;         /* 保留换行符，让内容格式更友好，支持多行文本 */
}
.m-footer {
  display: flex;       /* 使用 flex 布局，让退出按钮居右显示 */
  justify-content: flex-end;
  margin-top: 10px;
}
.m-close {
  padding: 8px 16px;
  background-color: #8ebee5;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  color: #30404f;
}
.m-close:hover {
  background-color: #b2effd;
}
</style>

<script>
export default {
  name: 'BlogList',
  data() {
    return {
      MOpen: false,
      currentArticle: { title: '', content: '' }, //  修复：初始化为对象，避免undefined
      showDropdown: false,
      searchResultList: [],
      isDropdownMouseDown: false, // 修复：标记下拉框是否被按下
      articleList: [
        {
          id: 1,
          title: '欢迎来到我的博客',
          author: 'Panda涵',
          publishTime: '2026/3/1 00:00:00',
          content: '你好呀~' 
        },
      ]
    }
  },
  methods: {
    handleSearch(e) {
      const keyword = e.target.value.trim()
      this.showDropdown = true

      if (!keyword) {
        this.searchResultList = []
        return
      }

      // 修复：匹配文章标题（包含关键词即匹配）
      this.searchResultList = this.articleList.filter(item => 
        item.title.includes(keyword)
      )
    },

    handleBlur() {
      // 修复：如果下拉框正在被按下，不隐藏
      if (this.isDropdownMouseDown) return
      setTimeout(() => {
        this.showDropdown = false
      }, 200)
    },

    // 修复：下拉框鼠标按下时标记，防止blur提前隐藏
    handleDropdownMouseDown() {
      this.isDropdownMouseDown = true
      setTimeout(() => {
        this.isDropdownMouseDown = false
      }, 300)
    },

    selectItem(article) {
      this.open(article)
      this.showDropdown = false
    },

    open(article) {
      //  修复：完整赋值当前文章
      this.currentArticle = { ...article }
      this.MOpen = true
    },

    close() {
      // 修复：确保关闭弹窗
      this.MOpen = false
    },

    handlePublish() {
      const titleInput = document.getElementById('title')
      const usernameInput = document.getElementById('username')
      const messageInput = document.getElementById('message')

      const title = titleInput.value.trim()
      const author = usernameInput.value.trim()
      const content = messageInput.value.trim()

      if (!title || !author) {
        alert('请输入文章标题和用户名！')
        return
      }

      const newArticle = {
        id: Date.now(),
        title: title,
        author: author,
        publishTime: new Date().toLocaleString(),
        content: content || '暂无内容'
      }

      this.articleList.unshift(newArticle)

      titleInput.value = ''
      usernameInput.value = ''
      messageInput.value = ''

      alert('文章发布成功！')
    }
  }
}
</script>