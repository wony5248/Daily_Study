<template>
  <div>
    <el-row class="rowflex  justify-content-center">
      <el-col
        class="colmargin"
        :span="8"
        :key="o"
        :offset="index > 0 ? 2 : 0"
      >
        <el-card :body-style="{ padding: '0px' }">
          <img
            src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
            class="image"
          />
          <div style="padding: 14px;">
            <span>이름: {{name}}</span>
            <div class="bottom clearfix">
              <time class="time">email: {{ email }}</time>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>


<style>
.time {
  font-size: 13px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}
.rowflex{
  display: flex;
  justify-content: center;
}
.image {
  width: 100%;
  display: block;
}
.colmargin{
  margin-top: 60px;
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>

<script>
import { userAPI } from "../utils/axios";
export default {
  data() {
    return {
      name: "",
      email: "",
      currentDate: new Date(),
    };
  },
  async mounted() {
    console.log(this.$route);
    const result = await userAPI.profile(8);
    console.log(result);
    if (result.data) {
      this.name = result.data.name;
      this.email = result.data.email;
    }
  },
};
</script>
