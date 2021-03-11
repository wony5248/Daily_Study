<template>
  <div>
    <p>이름 : {{ name }}</p>
    <p>E-mail: {{ email }}</p>
  </div>
</template>

<script>
import { userAPI } from "../utils/axios";
export default {
  data() {
    return {
      name: "",
      email: "",
    };
  },
  async mounted() {
    console.log(this.$route.query);
    const result = await userAPI.profile(this.$route.query);
    console.log(result);
    if (result.data) {
      this.name = result.data.name;
      this.email = result.data.email;
    }
  },
};
</script>

<style></style>
