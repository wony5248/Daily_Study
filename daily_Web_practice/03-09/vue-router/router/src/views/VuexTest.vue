<template>
  <div>

  </div>
</template>

<script>
//헬퍼 함수
import { mapState, mapMutations } from "vuex";
export default {
  //data는 유지 해야 하지만 data 변경해서 보여줄 경우
  computed: {
    ...mapState(["name"]),
  },
  methods: {
    ...mapMutations(["CHANGE_NAME"]),
  },
  mounted() {
    // console.log(this.$store.state.name);
    // this.$store.commit("CHANGE_NAME", "치킨");
    // console.log(this.$store.state.name);
    console.log(this.name)
    this.CHANGE_NAME("삼겹살")
    console.log(this.name)
  },
};
</script>

<style></style>
