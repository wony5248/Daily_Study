<template>
  <div class="main-search">
    <div class="main-text-wrapper">
      <p><span>어떤동네, 어떤방</span>에서</p>
      <p>살고 싶으신가요?</p>
    </div>
    <input
      class="main-search-input"
      placeholder="찾을 방의 위치를 입력해주세요 "
      v-model="input"
      @keyup.enter="search"
    >
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: "",
    };
  },
  methods:{
    search(){
        this.$router.push(`/room?search=${this.input}`)
    }
  }
};
</script>

<style>
.main-search {
  width: 70%;
  margin: 0 auto;
  padding-top: 115px;
  padding-bottom: 113px;
  text-align: center;
}
.main-text-wrapper {
  font-size: 47px;
  text-align: center;
}
.main-text-wrapper p {
  margin: 0;
}
.main-text-wrapper span {
  color: #409eff;
}

.main-search-input {
  margin-top: 50px;
  width: 70% !important;
  border: 1px solid #dddddddd;
  padding:15px 10px;
  border-radius: 5px;
  
}
</style>
