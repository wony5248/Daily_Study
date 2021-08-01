<template>
  <div>
    <div v-if="test.length">
      <ol>
        <li class="list" v-for="t in test" :key="t.id">
        {{t.title}}
      </li>
      </ol>
    </div>
  </div>
</template>
<style>
  .list{
    border: 1px solid skyblue;
    padding-top: 8px;
    padding-bottom: 8px;
    padding-left: 8px;
    border-radius: 16px;
    margin-bottom: 8px;
    text-align: left;
    

  }
</style>
<script>
import axios from "axios"
export default {
  data(){
    return {
      test: "aa"
    }
  },
  async mounted() {
    const result = await axios.get("https://koreanjson.com/todos")
    console.log(result)
    this.test = result.data
  }
}
</script>

<style>

</style>