<template>
  <div>
    <p>옵션</p>
    <el-checkbox-group v-model="selectedOptions" >
      <el-checkbox-button @change="changeCheckbox" v-for="option in options" :label="option" :key="option">{{option}}</el-checkbox-button>
    </el-checkbox-group>
  </div>
</template>
<script>
import { mapMutations} from 'vuex';
  export default {
    data () {
      return {
        selectedOptions: [],
        options: ['세탁기', '냉장고', '침대', '에어컨', "TV", "책상"]
      };
    },
    methods:{
        ...mapMutations(['SET_OPTION']),
        changeCheckbox(){
            // vuex에 옵션값 바꿔서 등록하기
            this.SET_OPTION(this.selectedOptions);
        }
    }
  }
</script>