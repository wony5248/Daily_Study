<template>
  <div>
      emit2
      <button @click="serveToEmit">Hello</button>
  </div>
</template>

<script>
export default {
    methods:{
        serveToEmit(){
            this.$emit("hello", "world")
        }
    }
}
</script>

<style>

</style>