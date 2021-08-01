import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    loading: true,
    visible:false
  },
  mutations: {
    SET_LOADING(state, data){
      state.loading = data
    },
    SET_VISIBLE(state, data){
      state.visible = data
    }
  },
  actions: {
  },
  modules: {
  }
})
