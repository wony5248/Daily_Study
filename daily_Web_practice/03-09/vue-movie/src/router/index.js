import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from "../views/Main.vue"
import MovieDetail from "../views/MovieDetail.vue"
import Search from "../views/Search.vue"
import Home from "../views/Home.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/movie',
    name: 'Main',
    component: Main
  },
  {
    path: '/movie/:id',
    name: 'Detail',
    component: MovieDetail
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router