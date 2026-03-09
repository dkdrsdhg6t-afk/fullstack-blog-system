import { createRouter, createWebHistory } from 'vue-router'

// 改成新的文件名
import HomePage from '../views/HomePage.vue'
import AboutPage from '../views/AboutPage.vue'
import BlogList from '../views/BlogList.vue'
import LoginPage from '../views/LoginPage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage // 这里也要对应
  },
  {
    path: '/about',
    name: 'About',
    component: AboutPage
  },
  {
    path: '/blog',
    name: 'Blog',
    component: BlogList
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router