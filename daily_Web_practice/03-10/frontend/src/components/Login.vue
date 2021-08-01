<template>
  <div class="about">
    <!-- vuex로 제어할 예정 -->
    <!-- <el-button type="text" @click="dialogFormVisible = true">open a Form nested Dialog</el-button> -->
    <!-- {{modal.login}} -->
    <el-dialog
      style="width:50%; margin:0 auto;"
      title="로그인"
      :visible.sync="modal.login"
    >
      <el-form :model="form">
        <el-form-item label="email" :label-width="formLabelWidth">
          <el-input v-model="form.email" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="password" :label-width="formLabelWidth">
          <el-input v-model="form.password" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="SET_LOGIN_MODAL(false)">Cancel</el-button>
        <el-button type="primary" @click="login">Confirm</el-button>
      </span>
      <span>{{ status }}</span>
    </el-dialog>
  </div>
</template>
<script>
import { mapState, mapMutations } from "vuex";
import { userAPI } from "../utils/axios";
export default {
  data() {
    return {
      dialogTableVisible: false,
      dialogFormVisible: false,
      form: {
        email: "",
        password: "",
      },
      status: "",
      formLabelWidth: "120px",
    };
  },
  computed: {
    ...mapState(["modal"]),
  },
  methods: {
    ...mapMutations(["SET_LOGIN_MODAL", "SET_USER"]),
    async login() {
      const { email, password } = this.form;
      if (!email || !password) {
        this.status = "이메일과 비밀번호를 입력해 주세요";
        return;
      }
      const result = await userAPI.login(email, password);
      console.log(result);
      if (result.data.token) {
        // 토큰을 저장
        // localStorage에 저장
        localStorage.setItem("token", result.data.token);
        this.SET_USER({ id: result.data.id, name: result.data.name });
        this.SET_LOGIN_MODAL(false);

        // 이제 로그인 정보를 vuex에 저장한다.
      } else if (result.data.status === "ERROR") {
        alert("이메일과 비밀번호를 다시 입력해주세요");
        this.form.email = "";
        this.form.password = "";
      }
    },
  },
};
</script>
