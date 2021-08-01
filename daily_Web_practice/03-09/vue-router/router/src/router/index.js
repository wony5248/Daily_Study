import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Main from "../views/Main.vue"
import Intro from "../views/Intro.vue"
import Chicken1 from "../views/Chicken1.vue"
import TestForEmit from "../views/TestForEmit.vue"
import VuexTest from "../views/VuexTest.vue"
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/vuex-test',
    name: 'Vuex',
    component: VuexTest
  },
  {
    path: '/intro',
    name: 'Intro',
    component: Intro
  },
  {
    path: '/test',
    name: 'Test',
    component: TestForEmit
  },
  {
    path: '/main',
    name: 'Main',
    component: Main
  },
  {
    path: '/chicken',
    name: 'Chicken',
    component: Chicken1
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
