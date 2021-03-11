<template>
  <!-- 필요한 부분 -->
  <!-- 평수 -->
  <!-- 제목 -->
  <!-- 내용 -->
  <!-- 옵션 -->
  <!-- 주소 -->
  <el-form class="post-form main-container" @submit.prevent="posting">
    <el-form-item label="평수" style="width:160px;">
      <el-input type="text" v-model="form.size" autocomplete="off"></el-input>
    </el-form-item>
 
    <Option></Option>
   
    <!-- 주소 업로드  -->
    <Map></Map>
    
    <!-- 이미지 업로드, Upload 하단 라이브러리 활용  -->
    <Upload></Upload>

     <el-form-item label="제목" style="width:600px;">
      <el-input type="text" v-model="form.title" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item label="내용">
      <el-input
        type="text"
        v-model="form.content"
        autocomplete="off"
      ></el-input>
    </el-form-item>
    
    <el-button type="primary" @click="posting">글 쓰기</el-button>
  </el-form>
</template>

<script>
import {mapState} from 'vuex'
import Option from "../components/Option";
import Upload from "../components/Upload";
import Map from "../components/Map";
import { roomAPI } from '../utils/axios';
export default {
  components: {
    Upload,
    Map,
    Option
  },
  data() {
    return {
      form: {
        title: "",
        content: "",
        size: "",
      },
    };
  },
computed:{
  ...mapState(['options','location','fileList'])
},
  methods: {
    async posting() {
      try {
              // 가져와야하는 값 
      // title, content, size
      const {title, content, size} = this.form;
      // vuex로 부터 가져와야 하는값
      // option, 위도 경도 값, 파일 정보
      const {options, location, fileList} = this;
      console.log(this.form);
      console.log(options);
      console.log(location);
      console.log(fileList);
      const formData = new FormData();
      formData.append("title", title);
      formData.append("content", content);
      formData.append("room_size", size);
      formData.append("location", location.address);
      formData.append("latitude", location.latitude);
      formData.append("longitude", location.longitude);

      if(options.length){
        options.forEach(option => {
        formData.append("item", option)
      });
      }
      
      if(fileList.length){
        fileList.forEach(list => {
        console.log(list);
        formData.append("room_image", list.file);
      });
      }
      
      const result = await roomAPI.post(formData);
      console.log(result);
      if(result.data.status === "OK"){
        alert("게시글 작성이 완료되었습니다");
        this.$router.push("/room")
      }else{
        alert("게시글 작성에 실패하였습니다.")
      }

      } catch (error) {
        console.log(error);
      }
      
    },
    // 주소를 가져오는 method 배포할것

  },
};
</script>

<style>
.main-container {
  width: 1200px;
  
  margin: 50px auto;
}

</style>
