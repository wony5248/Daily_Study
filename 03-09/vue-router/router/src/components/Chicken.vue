<template>
  <div>
    <button @click="alarm">소금</button>
    <button @click="sendMessage">치킨은 맛있다.</button>
  </div>
</template>

<script>
import SubMenu from "./SubMenu";
export default {
  components: {
    SubMenu,
  },
  props: ["name", "name2", "name3"],
  methods: {
    alarm() {
      alert(this.name);
    },
    sendMessage(){
        this.$emit("message", "치킨은 맛있다.")
    }
  },
};
</script>

<style></style>
