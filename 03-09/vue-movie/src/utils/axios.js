import axios from "axios";
const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: "5a5bb0c210832571c685e0d62883e129",
    language: "ko-KR",
  },
});
export const movieApi = {
    nowPlaying: () => request.get("movie/now_playing"),
    popular: () => request.get("movie/popular"),
    upComing: () => request.get("movie/upcoming"),
    // append to response에 대한 설명 https://developers.themoviedb.org/3/get1ting-started/append-to-response
    movieDetail: (id) =>
      request.get(`movie/${id}`, {
        params: { append_to_response: "videos" },
      }),
    // 검색을 구현
    search: (keyword) =>
      request.get(`search/movie/`, {
        params: {
          query: keyword,
        },
      }),
  };