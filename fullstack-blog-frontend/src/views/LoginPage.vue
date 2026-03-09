<template>
    <!-- 登录/注册容器 -->
    <div class="container">
        <div class="form-box">
            <div class="register-box hidden">
                <!-- 注册 -->
                <h1>register</h1>
                <input type="text" placeholder="用户名">
                <input type="email" placeholder="邮箱">
                <input type="password" placeholder="密码">
                <input type="password" placeholder="确认密码">
                <button @click="show('注册成功')">注册</button>      <!-- @click 绑定语法，点按钮触发函数 -->
            </div>
            <div class="login-box">
                <!-- 登录 -->
                <h1>login</h1>
                <input type="text" placeholder="用户名">
                <input type="password" placeholder="密码">
                <button @click="show('登录成功')">登录</button>
            </div>
        </div>
        <div class="con-box left">
            <h2>欢迎来到<span>我的博客</span></h2>
            <p>快来看看啪</p>
            <img src="../assets/微信图片_20260103133039_212_3.jpg">
            <p>已有账号</p>
            <button id="login">去登录</button>
        </div>
        <div class="con-box right">
            <h2>欢迎来到<span>我的博客</span></h2>
            <p>快来看看啪</p>
            <img src="../assets/173320F42A43377CA6D2328FE595967B.png">
            <p>没有账号？</p>
            <button id="register">去注册</button>
        </div>
    </div>

    <!-- 消息提示框 -->
    <div class="m" v-if="message">       <!-- v-if：这是 Vue 的条件渲染指令 -->
        {{ message }}
    </div>
</template>

<style>
body{
    background-color: #fff;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative;
}
.container{
    background-color: #fff;
    width: 650px;
    height: 415px;
    border-radius: 5px;
    box-shadow: 5px 5px 5px rgba(0,0,0,0.1);
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
}
.form-box{
    position: absolute;
    top: -10%;
    left: 5%;
    background-color: #8abbd7;
    width: 320px;
    height: 500px;
    border-radius: 5px;
    box-shadow: 2px 0 10px rgba(0,0,0,0.1);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 2;
    transition: 0.5s ease-in-out;
}
.register-box,.login-box{
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
}
.hidden{
    display: none;
    transition: 0.5s;
}
h1{
    text-align: center;
    margin-bottom: 25px;
    text-transform: uppercase;            /* 将所有文字转化为大写形式 */
    color: #fff;
    letter-spacing: 5px;           /* 字间距 */
}
input{
    background-color: transparent;
    width: 70%;
    color: #fff;
    border: none;
    border-bottom: 1px solid rgba(255,255,255,0.4);
    padding: 10px 0;
    text-indent: 10px;             /* 文本缩进属性，专门用于设置块级元素第一行文本的缩进距离 */
    margin: 8px 0;
    font-size: 14px;
    letter-spacing: 2px;
}
input::placeholder{
    color: #fff;
}
input:focus{
    color: #6290ad;
    outline: none;
    border-bottom: 1px solid #34455080;
    transition: 0.5s;
}
input:focus::placeholder{
    opacity: 0;
}
.form-box button{
    width: 70%;
    margin-top: 35px;
    background-color: #f6f6f6;
    outline: none;
    border-radius: 8px;
    padding: 13px;
    color: #3495da;
    letter-spacing: 2px;
    border: none;
    cursor: pointer;
}
.form-box button:hover{
    background-color: #c6c6c6;
    color: #f6f6f6;
    transition: background-color 0.5s ease;
}
.con-box{
    width: 50%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
}
.con-box.left{
    left: -2%;
}
.con-box.right{
    right: -2%;
}
.con-box h2{
    color: #8e9aaf;
    font-size: 25px;
    font-weight: bold;
    letter-spacing: 3px;
    text-align: center;
    margin-bottom: 4px;
}
.con-box p{
    font-size: 12px;
    letter-spacing: 2px;
    color: #8e9aaf;
    text-align: center;
}
.con-box span{
    color: #97c4f1;
}
.con-box img{
    width: 150px;
    height: 150px;
    opacity: 0.9;
    margin: 40px 0;
}
.con-box button{
    margin-top: 3%;
    background-color: #fff;
    color: #718b97;
    border: 1px solid #abd3e0;
    padding: 6px 10px;
    border-radius: 5px;
    letter-spacing: 1px;
    outline: none;
    cursor: pointer;
}
.con-box button:hover{
    background-color: #d4f5fa;
    color: #fff;
}

.m{
    position: absolute;
    bottom: 100px; /* 距离底部1000像素 */
    left: 47%;
    transform: translateX(-50%);
    background-color: #4c91af; /* 绿色背景 */
    color: white; /* 白色文字 */
    padding: 15px 30px;
    border-radius: 10px;
    font-size: 16px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    animation: fade 3s forwards;       /* 动画效果：淡入淡出(在动画结束后保持最后一帧的状态) */
}
/* 动画关键帧 */
@keyframes fade {
  0% { opacity: 0; transform: translateY(20px); }
  20% { opacity: 1; transform: translateY(0); }
  80% { opacity: 1; transform: translateY(0); }
  100% { opacity: 0; transform: translateY(20px); }
}
</style>

<script>
import { ref } from 'vue'         //ref函数 是用来创建响应式数据的，当数据变化时，页面会自动更新。

export default {
  name: "LoginPage",

  setup(){         //在 setup() 函数里定义响应式数据和方法
    const message = ref('')             // 初始值是空字符串
    const show = (text) => {             //  定义一个方法，用来修改这个响应式数据
      message.value = text               //  因为是 ref 包装的，所以要用 .value 来修改
      setTimeout(() => {                 //  定时器函数
        message.value = ''
      }, 3000)
    }
    return {            // 把创建好的数据和方法“返回”出去，让模板可以使用
      message,
      show
    }
  },

  mounted(){       //组件挂载到DOM后执行
    let login=document.getElementById('login')      
    let register=document.getElementById('register')
    let form_box=document.getElementsByClassName('form-box')[0]
    let register_box=document.getElementsByClassName('register-box')[0]
    let login_box=document.getElementsByClassName('login-box')[0]

    //去注册按钮点击事件
    if(register){
        register.addEventListener('click',() => {
        form_box.style.transform='translateX(80%)'
        login_box.classList.add('hidden')
        register_box.classList.remove('hidden')
    })
    }

    //去登录按钮点击事件
    if(login){
        login.addEventListener('click',() => {
        form_box.style.transform='translateX(0%)'
        register_box.classList.add('hidden')
        login_box.classList.remove('hidden')
    })
    }
  }
}

</script>