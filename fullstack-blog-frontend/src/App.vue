<template>
  <div id="app">
    <nav>
      <router-link to="/">首页</router-link> |
      <router-link to="/about">关于我</router-link> |
      <router-link to="/blog">博客</router-link>
    </nav>
    <router-view/> <!-- 页面内容渲染出口 -->
  </div>
</template>