<template>
  <div>
    
    <div v-if="visible">
      착한 사람에게만 보이는 글씨 입니다.
      <b-button @click="toggle">클릭</b-button>
    </div>
    <div v-else>
        <b-button @click="toggle1">클릭</b-button>
    </div>
  </div>
</template>

<script>

import { mapMutations} from "vuex";
import {mapState} from "vuex"
export default {
  computed: {
    ...mapState(["visible"]),
  },
  created() {
    this.SET_VISIBLE(false);
  },
  methods: {
    ...mapMutations(["SET_VISIBLE"]),
    toggle() {
      this.SET_VISIBLE(false)
    },
    toggle1() {
        this.SET_VISIBLE(true)
    }
  },
};
</script>

<style></style>
