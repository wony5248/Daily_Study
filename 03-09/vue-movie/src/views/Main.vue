<template>
  <div class="d-flex flex-wrap" v-if="nowPlaying.length">
    <movie-text text="Now Playing"></movie-text>
    <movie-lists :movieList="nowPlaying"></movie-lists>
    <movie-text text="Popular"></movie-text>
    <movie-lists :movieList="popular"></movie-lists>
    <movie-text text="Coming Soon"></movie-text>
    <movie-lists :movieList="upComing"></movie-lists>
  </div>
</template>

<script>
import MovieLists from "../components/MovieLists";
import MovieText from "../components/MovieText";
import { mapMutations } from "vuex";
import { movieApi } from "../utils/axios";
export default {
  components: {
    MovieLists,
    MovieText,
  },
  data() {
    return {
      nowPlaying: [],
      popular: [],
      upComing: [],
    };
  },
  created() {
    this.SET_LOADING(true);
  },
  async mounted() {
    try {
      const { nowPlaying, popular, upComing } = movieApi;
      const nowPlayingResult = await nowPlaying();
      const popularResult = await popular();
      const upComingResult = await upComing();
      this.nowPlaying = nowPlayingResult.data.results;
      this.popular = popularResult.data.results;
      this.upComing = upComingResult.data.results;
      this.SET_LOADING(false);
      // const data = await movieApi.nowPlaying();
      // console.log(data);
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    ...mapMutations(["SET_LOADING"]),
  },
};
</script>
<style></style>
