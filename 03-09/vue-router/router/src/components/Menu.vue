<template>
  <div>
      menu
      {{name}}
      {{name2}}
      {{name3}}
      <sub-menu :name="name" :name2="name2"></sub-menu>
      <SubMenu :name3="name3"></SubMenu>
  </div>
</template>

<script>
import SubMenu from"./SubMenu"
export default {
    components:{
        SubMenu
    },
    props:['name',"name2","name3"]
}
</script>

<style>

</style>