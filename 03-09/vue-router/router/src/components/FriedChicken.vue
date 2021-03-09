<template>
  <div>
      <Fry @message="showMessage"></Fry>
  </div>
</template>

<script>
import Fry from"./Fry"
export default {
    components:{
        Fry
    },
    methods:{
        showMessage(message){
            alert("2단계를 거쳐 도착했습니다.")
            alert(message)
        }
    },
    props:['name',"name2","name3"]
}
</script>

<style>

</style>