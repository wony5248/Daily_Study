<template>
  <div>
    <Form></Form>
    <bar-chart
      style="width:30vw"
      v-if="chartData"
      :chart-data="chartData"
    ></bar-chart>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import BarChart from "../components/ReactiveBarChart";
import Form from "../components/Form";
export default {
  components: {
    BarChart,
    Form,
  },
  data() {
    return {
      //   chartData: null,
    };
  },
  computed: {
    ...mapState(["chartData"]),
  },
  methods: {
    //mapActions 넣기
    //actions가 아닌 방식의 action 호출
    //this.$store.dispatch
    ...mapActions(["generateChartData"]),
    generateData() {
      let newArray = [];
      let newArray2 = [];

      for (let i = 0; i < 10; i++) {
        let randomValue = Math.floor(Math.random() * 10);
        newArray.push(randomValue);
      }

      for (let i = 0; i < 10; i++) {
        let randomValue = Math.floor(Math.random() * 10);
        newArray2.push(randomValue);
      }

      this.chartData = {
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#f87979",
            data: newArray,
            fill: false,
          },
          {
            label: "Data Two",
            backgroundColor: "black",
            data: newArray2,
            fill: false,
          },
        ],
      };
    },
  },
  mounted() {
    // this.generateData();
    // setInterval(this.generateData, 2000);
    this.generateChartData();
  },
};
</script>

<style>
.main-container{
    display: flex;
    padding:20px
}
.main-container > * {
    flex:1
}
</style>
