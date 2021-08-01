import Vue from 'vue'
import Vuex from 'vuex'
import {
  dataLap
} from "../utils/axios"

Vue.use(Vuex)

function makeColor() {
  return "#" + Math.round(Math.random() * 0xffffff).toString(16)
}

export default new Vuex.Store({
  state: {
    chartData: ""
  },
  mutations: {
    CHANGE_CHART_DATA(state, data) {
      state.chartData = data
    }
  },
  //비동기 처리 할때 actions에서 처리하고 commit을 통해 mutation에 보내서 state 변경

  actions: {
    async generateChartData({
      commit
    }) {
      const result = await dataLap.get();
      console.log("get",result)
      const chartData = {
        labels: result.data[0].data.map(li => li.period),
        datasets: result.data.reduce((acc, cur) => {
          let label = cur.title;
          let data = cur.data.map(li => li.ratio)
          let borderColor = makeColor()
          let backgroundColor = makeColor()
          acc.push({
            label: label,
            data,
            borderColor,
            backgroundColor,
            fill: false
          })
          return acc
        }, [])

      }

      commit("CHANGE_CHART_DATA", chartData)
    }
  },
  modules: {}
})