<template>
  <div>
      <Chicken @message="receiveMessage"></Chicken>
  </div>
</template>

<script>
import Chicken from"./Chicken"
export default {
    components:{
        Chicken
    },
    methods:{
        receiveMessage(message){
            alert(message)
            this.$emit("message", message);
        }
    },
    props:['name',"name2","name3"]
}
</script>

<style>

</style>