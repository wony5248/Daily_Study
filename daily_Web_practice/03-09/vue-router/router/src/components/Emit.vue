<template>
  <div>
    <button @click="serverToParent">전송</button>
    <Emit2 @hello="test"></Emit2>
  </div>
</template>

<script>
import Emit2 from "./Emit2"
export default {
  components: {
    Emit2,
  },
  methods: {
    serverToParent() {
      this.$emit("check", 5);
    },
    test(){
        alert("Emit2로부터 잘 들어옵니다")
    }
  },
};
</script>

<style></style>
