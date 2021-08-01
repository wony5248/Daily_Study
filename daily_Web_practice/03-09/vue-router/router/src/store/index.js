import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  //데이터
  state: {
    name:"HELLO"
  },
  //데이터를 변경할 때 사용하는 함수
  mutations: {
    CHANGE_NAME(state,data){
      state.name = data
    }
  },
  // 비동기 처리 -> 변경된 데이터를 mutations에 보낼 때
  actions: {
  },
  //store의 분리, 라이브러리
  modules: {
  }
})
