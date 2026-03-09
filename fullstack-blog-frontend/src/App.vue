<template>
  <div id="app">

    <!-- 顶部：导航栏 -->
    <nav>   <!-- 导航的容器 -->
       <div class="zt">
        <router-link to="/">首页</router-link> 
        <span class="jgx">|</span>
        <router-link to="/about">关于我</router-link> 
        <span class="jgx">|</span>
        <router-link to="/blog">博客</router-link>
        <span class="jgx">|</span>
        <router-link to="/login">登录</router-link>
       </div>
    </nav>

     <!-- 中间：页面内容渲染出口 -->
  <div id="nr" >
    <router-view/> <!-- 显示当前页面内容 -->
  </div>

    <!-- 底部：页脚 -->
    <footer>   <!-- 专门放页面底部的信息 -->
      <div class="bq">
      <p>&copy;     2026     我的个人博客     |     Aria</p>
      </div>
    </footer>

  </div>
</template>

<style>
/* 全局重置 */
*{
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* 基础样式 */
body{
  font-family: "Microsoft Yahei", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  line-height: 1.6;   /* 行高：1.6倍 */
  color: #000; 
  background-color: #ffffff; 
}
html, body{
  height: 100%;
}

/* 应用容器 */
#app{
  width: 100%;
  margin: 0 auto;   /* 水平居中：上下外边距为0，左右自动 */
  min-height: 100vh;
  display: flex; 
  flex-direction: column; /* Flex主轴方向为垂直，让子元素（导航、内容、页脚）垂直排列 */
}

/* 导航栏样式 */
/* 导航栏外观 */
nav{
  padding: 20px 0;
  width: 100%;
  margin-bottom: 30px;
  border-bottom: 2px solid #99c4fc;
  background-color: #b0d0f9;
  border-radius: 0 0 8px 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  z-index: 999;
  position: sticky;
  top: 0;
}
/* 导航链接样式 */
nav a{
  text-decoration: none;   /* 文字装饰：去掉默认的下划线 */
  color: #3b475b; 
  margin-right: 30px; 
  margin-left: 30px;
  font-size: 16px; 
  font-weight: 500;   /* 字体粗细：500 */
  transition: color 0.3s ease;   /* 过渡效果：颜色变化在0.3秒内平滑过渡 */
}
nav a:hover{
  color: #308df1;
}
/* 控制当前所在页面对应的导航链接状态 */
nav a.router-link-active {
  color: #2466ac; /* 颜色：浅蓝 #2b6cb0，高亮显示当前页面 */
  font-weight: 600; /* 字体粗细：600，比普通链接更粗，更醒目 */
}
.zt{
  max-width: 1200px;
  margin: 0 auto;
  text-align: center;
}
.jgx{
  margin: 0 auto;
  color: #3b475b; 
}

/* 中间内容区 */
#nr{
  flex: 1;   /* 占据所有剩余空间，把页脚推到底部 */
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  margin-bottom: 30px; 
  margin-top: 550px;
}

/* 页脚样式 */
footer{
  margin-top: auto;
  width: 100%;
  padding: 20px 0;
  text-align: center;   /* 文字对齐：居中 */
  color: #455060;
  background-color: #b0d0f9;
  font-size: 16px;
  border-top: 2px solid #99c4fc;
  border-radius: 8px 8px 0 0;
}
.bq{
  margin: 0 auto;
  max-width: 1200px;
}
</style>