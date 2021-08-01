<template>
  <div>
      Main
      <Menu :name="test" :name2="test2" name3="카테고리"></Menu>
  </div>
</template>

<script>
import Menu from "../components/Menu"
export default {
  components:{
    Menu
  },
  data(){
    return{
      test:"AA",
      test2:"BB"
    }
  }
}
</script>

<style>

</style>