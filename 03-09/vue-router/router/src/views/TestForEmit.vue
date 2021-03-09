<template>
  <div>
      TestForEmit
      <Emit @check="showAlert"></Emit>
  </div>
</template>

<script>
import Emit from "../components/Emit"
export default {
    components:{
        Emit,
    },
    methods:{
        showAlert(number){
            alert("$emit을 통해 부모쪽에 전달 되었습니다.")
            alert(number)
        }
    }
}
</script>

<style>

</style>