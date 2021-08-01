import Vue from 'vue'
import VueRouter from 'vue-router'
// import Home from '../views/Home.vue'
import Main from "../views/Main.vue"
import Post from "../views/Post.vue"
import Room from "../views/Room.vue"
import Profile from "../views/Profile.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/profile',
    name:'Profile',
    component: Profile
  },
  {
    path: '/',
    name:'Main',
    component: Main
  },
  {
    path: '/room',
    name: 'Room',
    component: Room
  },
  {
    path: '/post',
    name: 'Post',
    component: Post
  }
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
