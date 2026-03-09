<template>
  <div class="ddbt">
    <div class="HPbt">
      <h1>欢迎来到我的博客</h1>
    </div>
  </div>
</template>

<style>
.ddbt{
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: -1;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.HPbt{
  width: 100%;
  height: 100%;
  background-image: url(../assets/1351260.png);
  background-size: cover;           /* 完全覆盖容器 */
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  justify-content: center;
  align-items: center;
}
h1{
  color: #fff;
  text-align: center;
  font-size: 60px;
}
</style>

<script>
export default {
  name: "HomePage"
}
</script>