<template>
  <div class=".d">
    <div class="dhz">
    <div class="x1">
         <img src="../assets/xzj.png">
    </div>
    <div class="x2">
        <div class="bt"><h2><b><u>基本信息</u></b></h2></div>
        <div class="nr">
          <ul>
            <li>江苏镇江人</li>
            <li>目前就读于山东理工大学软件工程专业</li>
            <li> ^ U ^ </li>
          </ul>
        </div>
    </div>
  </div>
  <div class="dhz">
    <div class="x3">
        <div class="bt"><h2><b><u>个人博客</u></b></h2></div>
        <div class="nr">
          <p>我搭建这个个人博客，是希望用代码搭建
            一个属于自己的数字空间。它不仅是我学
            习与成长的见证，也是我分享知识、记录
            思考的自留地。在这里，我可以沉淀技术
            笔记，梳理项目经验，也能自由表达对编
            程的热爱与思考。目前它虽还不够完善，
            但我会不断打磨，让它成为我技术路上的
            忠实伙伴，见证我从青涩到成熟的每一步
            成长。</p>
        </div>
    </div>
    <div class="x4">
        <div class="bt"><h2><b><u>自我评价</u></b></h2></div>
        <div class="nr">
          <p>我始终以积极向上的心态面对学习与生活，
           坚信每一份努力都能浇灌出成长的果实。
           面对挑战时，我始终保持拼搏进取的姿态，
           敢于突破自我、迎难而上；日常中注重情
           绪的稳定管理，能以理性和耐心应对各类
           问题，在沉淀中稳步前行，在坚持中追求
           卓越。当然，目前我还没有达到这种程度，
           但是我会一直努力，向此靠近。</p>
        </div>
    </div>
  </div>
  </div>
</template>

<style>
ul {
    font-size: 30px;
}
h2{
    font-size: 30px;
}
.bt{
  margin-top: 50px;
  margin-bottom: 50px;
}
.nr{
  flex: 1;   /* 占据所有剩余空间，把页脚推到底部 */
  width: 100%;
  margin: 0 auto;
  padding: 20px;
  margin-bottom: 30px; 
}
.d{
  margin-bottom: 80px;
  margin-top: 80px;
}
.dhz{
    display: flex;
    justify-content: space-evenly;
    margin-bottom: 80px;         /* 排与排之间的间距 */
    margin-top: 100px;
}
        
.x1, .x2, .x3, .x4{
    background-color: rgba(177, 224, 234, 0.7);
    padding: 15px;
    border-radius: 10%;
    box-sizing: border-box;
    width: 45%;
    /* 让盒子内的内容居中 */
    display: flex;        
    align-items: center;          /* 内容水平居中 */
    flex-direction: column;       /* 内容垂直排列 */
    text-align: center;           /* 文字类内容水平居中 */
    justify-content: center;
    position: relative;
    z-index: 1;
    width: 400px;
    height: 500px;
}
.x1 img{
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 8px;
} 
p , ul{
  font-size: 16px;
  line-height: 2;
  padding: 0 20px;
}
</style>

<script>
export default {
  name: "AboutPage"
}
</script>