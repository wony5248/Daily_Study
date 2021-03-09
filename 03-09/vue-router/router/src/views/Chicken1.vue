<template>
  <div>
      Main
      <fried-chicken :name="test" :name2="test2" ></fried-chicken>
  </div>
</template>

<script>
import FriedChicken from "../components/FriedChicken"
export default {
  components:{
    FriedChicken
  },
  data(){
    return{
      test:"300",
      test2:"40"
    }
  }
}
</script>

<style>

</style>