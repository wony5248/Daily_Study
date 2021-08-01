<template>
  <div id="app">
    <div id="nav">
      <router-link to="/movie">Movie</router-link> |
      <router-link to="/search">Search</router-link> |
      <router-link to="/">Home</router-link>
    </div>
    <b-spinner v-if="loading" class="d-block ml-auto mr-auto" label="Spinning"></b-spinner>
    <router-view/>
  </div>
</template>
<script>
import {mapState} from "vuex"
export default {
  computed:{
    ...mapState( ["loading","visible"])
  }
}
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400&display=swap");
* {
  color: #ffffff;
}
body {
  font-family: "Noto Sans KR", sans-serif;
}
#app {
  background-color: rgb(20, 20, 20);
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  min-height: 100vh;
}
#nav {
  text-align: center;
  padding: 20px;
  position: relative;
  z-index: 99;
  background-color: black;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
.router-link-exact-active {
  color: white !important;
}
</style>
