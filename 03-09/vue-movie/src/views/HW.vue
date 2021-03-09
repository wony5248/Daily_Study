<template>
  <div class="wrapper">
    <div v-if="visible">
      착한 사람에게만 보이는 글입니다.
    </div>
    <button @click="setVisible" style="background-color: gray;">클릭</button>
  </div>
</template>

<script>
import {mapMutations} from "vuex"
import {mapState} from "vuex"
export default {
  computed: {
    ...mapState(['visible'])
  },
  created(){
    this.SET_VISIBLE(false);
  },
  methods:{
    ...mapMutations([ 'SET_VISIBLE' ]),
    setVisible(){
      this.SET_VISIBLE(true);
    }
  }
}
</script>

<style>
.wrapper {
  margin: auto;
  border: solid 1px black;
  width: 500px;
  height: 800px;
  display: flex;
  /* background-color: white; */
  flex-direction: column;
  justify-content: space-around;
  align-items: center;
}
</style>
