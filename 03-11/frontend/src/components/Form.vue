<template>
  <el-form ref="form" :model="form" label-width="120px">
    <!-- group name, keyword 생성해야한다. -->
    <div class="groups-wrapper">
      <!--키워드 추가 -->
      <el-form-item style="width:500px;" label="키워드">
        <el-input v-model="form.keyword"
          ><el-button @click="saveKeyword" slot="append"
            >키워드 추가</el-button
          ></el-input
        >
      </el-form-item>

      <div v-if="keywords" class="tag-wrapper">
        <el-tag
          @click="removeKeyword(keyword)"
          v-for="keyword in keywords"
          :key="keyword"
          class="group-tag"
        >
          {{ keyword }}
        </el-tag>
      </div>
      <el-form-item style="width:500px;" label="주제">
        <el-input v-model="form.groupName"></el-input>
      </el-form-item>

      <div v-if="keywordGroups" class="tag-wrapper">
        <el-tag
          @click="removeGroup(group.groupName)"
          v-for="(group, index) in keywordGroups"
          :key="index"
          type="success"
          class="group-tag createtag"
          >{{ group.groupName }}</el-tag
        >
      </div>

      <el-button @click="saveGroup" class="create-button" type="primary"
        >주제 생성하기</el-button
      >
    </div>
    <!-- 주제를 보여주는 부분 -->

    {{ form.name }}

    <div class="groups-wrapper">
      <!-- 기간 -->
      <el-form-item label="시간대별 설정">
        <el-col :span="11">
          <el-date-picker
            type="date"
            placeholder="Pick a date"
            v-model="form.startDate"
            style="width: 100%;"
          ></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-date-picker
            type="date"
            placeholder="Pick a date"
            v-model="form.endDate"
            style="width: 100%;"
          ></el-date-picker>
        </el-col>
      </el-form-item>

      <!-- 구간 단위 설정 date 일간, week 주간, month 월간 -->
      <el-form-item label="구간 단위">
        <el-radio-group v-model="form.timeUnit">
          <el-radio label="date"></el-radio>
          <el-radio label="week"></el-radio>
          <el-radio label="month"></el-radio>
        </el-radio-group>
      </el-form-item>

      <!-- 디바이스 전체, pc, mobile -->
      <el-form-item label="디바이스">
        <el-radio-group v-model="form.device">
          <el-radio label="all"></el-radio>
          <el-radio label="pc">pc</el-radio>
          <el-radio label="mo">모바일</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="성별">
        <el-radio-group v-model="form.gender">
          <el-radio label="all">모두</el-radio>
          <el-radio label="m">남</el-radio>
          <el-radio label="f">녀</el-radio>
        </el-radio-group>
      </el-form-item>

      <el-checkbox-group v-model="form.ages">
          <el-checkbox label="1" name="type">0∼12세</el-checkbox>
          <el-checkbox label="2" name="type">13∼18세</el-checkbox>
          <el-checkbox label="3" name="type">19∼24세</el-checkbox>
          <el-checkbox label="4" name="type">25∼29세</el-checkbox>
          <el-checkbox label="5" name="type">30∼34세</el-checkbox>
          <el-checkbox label="6" name="type">35∼39세</el-checkbox>
          <el-checkbox label="7" name="type">40∼44세</el-checkbox>
          <el-checkbox label="8" name="type">45∼49세</el-checkbox>
          <el-checkbox label="9" name="type">50∼54세</el-checkbox>
          <el-checkbox label="10" name="type">55∼59세</el-checkbox>
          <el-checkbox label="11" name="type">60세 이상</el-checkbox>
        </el-checkbox-group>
    </div>

    <el-form-item>
      <el-button type="primary" @click="onSubmit">Create</el-button>
      <el-button>Cancel</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import moment from "moment";
import { mapActions } from "vuex";
import { dataLap } from "../utils/axios";
export default {
  data() {
    return {
      form: {
        // https://developers.naver.com/docs/datalab/search/#%EA%B0%9C%EC%9A%94 참고
        // 시작날짜
        startDate: null,
        // 종료 날짜
        endDate: null,
        // 구간 단위, date, week, month
        timeUnit: "month",
        // [{ groupName: "iPhone_4", keywords: ["아이폰4", "iphone4"] },]

        groupName: "",
        // v-model용
        keyword: "",
        // 보관용
        // 설정안함: 모두, m,f
        device: "all",
        // m 남성 f 여성
        gender: "all",
        ages: []
      },
      // 배열로 관리할 데이터 두가지 keywords array
      // keywordGroups array
      
      keywordGroups: [],
      keywords: [],
    };
  },
  methods: {
    ...mapActions(["generateChartData"]),
    // 키워드 생성하기
    saveKeyword() {
      console.log("test");
      if (this.form.keyword) {
        this.keywords.push(this.form.keyword);
      }
      this.form.keyword = "";
    },
    // 주제 생성하기
    saveGroup() {
      if (this.form.groupName) {
        this.keywordGroups.push({
          groupName: this.form.groupName,
          keywords: this.keywords,
        });
        this.form.groupName = "";
        this.keywords = [];
      }
    },
    removeGroup(groupName) {
      this.keywordGroups = this.keywordGroups.filter(
        (li) => li.groupName !== groupName
      );
    },
    removeKeyword(keyword) {
      this.keywords = this.keywords.filter((li) => li !== keyword);
    },
    async onSubmit() {
      console.log(this.keywordGroups);
      console.log(this.form.startDate);
      console.log(this.form.endDate);
      console.log(this.form.timeUnit);
      console.log(this.form.device);
      console.log(this.form.gender);
      console.log(this.form.ages);
      this.form.ages = this.form.ages.reduce((acc, cur) => {
        acc.push(cur);
        return acc;
      }, []);
      console.log(this.form.ages);
      const { startDate, endDate, timeUnit, device, gender, ages } = this.form;
      console.dir(startDate);
      if (
        this.keywordGroups.length &&
        startDate &&
        endDate &&
        timeUnit &&
        device &&
        gender &&
        ages
      ) {
        const data = {
          keywordGroups: this.keywordGroups,
          startDate: moment(startDate).format("YYYY-MM-DD"),
          endDate: moment(endDate).format("YYYY-MM-DD"),
          timeUnit,
          device,
          gender,
          ages
        };
        const result = await dataLap.post(data);
        console.log(result);
        if(result.data.status ==="OK"){
            this.generateChartData()
        }
      } else {
        alert("빈 값들을 입력해 주세요 ");
      }
    },
  },
};
</script>

<style>
.groups-wrapper {
  display: flex;
  flex-direction: column;
  border: 1px solid #dddddddd;
  padding: 30px;
  /* margin:20px; /
  margin-bottom: 30px;
  / justify-content: center; */
  align-items: stretch;
}
.create-button {
  width: 31%;
  margin-top: 30px !important;
  margin-left: 120px !important;
}

.tag-wrapper {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  margin-bottom: 12px;
}

.group-tag {
  width: 80px;
  font-size: 11px !important;
  margin: 3px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  cursor: pointer;
}
</style>
