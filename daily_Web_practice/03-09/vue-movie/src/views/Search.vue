<template>
  <div>
    <b-form @submit.prevent="onSearch">
      <b-form-input
        class="border-black"
        v-model="keyword"
        placeholer="영화 제목을 입력하세요"
      >
      </b-form-input>
    </b-form>
    <movie-text v-if="movieList.length" text="Search Result"></movie-text>
    <movie-lists :movieList="movieList"></movie-lists>
  </div>
</template>

<script>
import { movieApi } from "../utils/axios";
import { mapMutations } from "vuex";
import MovieLists from "../components/MovieLists"
import MovieText from "../components/MovieText"
export default {
  components:{
    MovieLists,
    MovieText
  },
  data() {
    return {
      keyword: "",
      movieList: {},
    };
  },
  created() {
    this.SET_LOADING(false);
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
    async onSearch() {
      if (!this.keyword) {
        alert("영화 제목을 입력하세요");
        return;
      }
      this.SET_LOADING(true);
      const result = await movieApi.search(this.keyword);
      console.log(result)
      this.movieList = result.data.results
      this.SET_LOADING(false)
      this.keyword("")
    },
  },
};
</script>

<style>
.search-input {
  color: black;
}
</style>
