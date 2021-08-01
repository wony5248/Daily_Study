<template>
  <!-- element tag nav 부분 복사하기  -->
  <!-- router true옵션  -->
  <el-menu
    :default-active="activeIndex"
    text-color="black"
    class="el-menu-demo nav-menu"
    mode="horizontal"
    @select="handleSelect"
  >
    <el-menu-item @click="$router.push('/')" index="/"
      >BBANG(빵)</el-menu-item
    >
    <el-menu-item @click="$router.push('/room')">방찾기</el-menu-item>
    <el-menu-item  v-if="user.id" @click="$router.push('/post')">방 팔기</el-menu-item>

    <!-- 로그인 후  -->
    <el-submenu v-if="user.id" index="3" class="login-menu">
      <template slot="title">{{user.name}} 님 환영합니다</template>
      <el-menu-item index="3-1" @click="$router.push(`/profile`)">내 프로필</el-menu-item>
      <el-menu-item index="3-2">내가 올린 방 </el-menu-item>
      <el-menu-item index="3-2" @click="SET_LOGOUT()">로그아웃</el-menu-item>
    </el-submenu>
    <!-- 로그인 전  -->
    <el-submenu v-else index="3" class="login-menu">
      <template slot="title">회원가입/로그인</template>
      <el-menu-item index="3-1" @click="SET_REGISTER_MODAL(true)"
        >회원가입</el-menu-item
      >
      <el-menu-item index="3-2" @click="SET_LOGIN_MODAL(true)"
        >로그인</el-menu-item
      >
    </el-submenu>
    <Login></Login>
    <Register></Register>
  </el-menu>
</template>


<script>
import Login from "./Login";
import Register from "./Register.vue";
import { mapMutations, mapState } from "vuex";
export default {
  components: {
    Login,
    Register,
  },
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
    };
  },
  computed: {
    ...mapState(["user"]),
  },
  methods: {
    ...mapMutations(["SET_REGISTER_MODAL", "SET_LOGOUT","SET_LOGIN_MODAL"]),
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    test() {
      console.log("hello");
    },
  
  },
};
</script>


<style>
.nav-menu {
  display: flex;
}
.login-menu {
  margin-left: auto !important;
}
</style>