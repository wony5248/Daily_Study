	
<template>
  <div class="map-container">
    <div class="address-wrapper">
      <el-input v-model="address" />
      <el-button slot="append" icon="el-icon-search" @click="getAddress()">주소검색</el-button>
    </div>
    <div ref="map" class="map-main"></div>
  </div>
</template>


<script>
import { mapMutations } from "vuex";
export default {
  data() {
    return {
      address: "",
      latitude: "",
      longitude: "",
    };
  },
  created() {
    // vue단에서 kakao map을 위한 기초 셋팅
    const addressScript = document.createElement("script");
    addressScript.src =
      "https://t1.daumcdn.net/mapjsapi/bundle/postcode/prod/postcode.v2.js";
    document.head.appendChild(addressScript);
    const mapScript = document.createElement("script");
    mapScript.onload = () => kakao.maps.load();
    mapScript.src =
      "http://dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=0fe1d5fd101ab6d2078168510cdb7237&libraries=services";
    document.head.appendChild(mapScript);
  },
  mounted() {},
  methods: {
    ...mapMutations(["SET_LOCATION"]),
    getAddress() {
      new daum.Postcode({
        oncomplete: (data) => {
          let mapOption = {
            center: new daum.maps.LatLng(37.537187, 127.005476), // 지도의 중심좌표
            level: 6, // 지도의 확대 레벨
          };
          const mapContainer = this.$refs.map;
          const map = new daum.maps.Map(mapContainer, mapOption);
          //주소-좌표 변환 객체를 생성
          let geocoder = new daum.maps.services.Geocoder();
          geocoder.addressSearch(data.address, (results, status) => {
            // 정상적으로 검색이 완료됐으면
            if (status === daum.maps.services.Status.OK) {
              console.log(results);
              // let result = results[0]; //첫번째 결과의 값을 활용
              const { y, x, address_name } = results[0];
              console.log(y, x, address_name);
              // 해당 주소에 대한 좌표를 받아서
              this.address = address_name;
              console.log(this);
              let coords = new daum.maps.LatLng(y, x);
              this.latitude = y;
              this.longitude = x;
              // 지도를 보여준다.
              mapContainer.style.display = "block";
              map.relayout();
              map.setLevel(4);
              // 지도 중심을 변경한다.
              map.setCenter(coords);
              let marker = new daum.maps.Marker({
                position: new daum.maps.LatLng(y, x),
                map: map,
              });
              // vuex에도 값 저장하기
              this.SET_LOCATION({
                address: this.address,
                latitude: y,
                longitude: x,
              });
            }
          });
        },
      }).open({
        //검색어 넘기기
        popupName: "Room", //이름 설정시 여러개의 팝업 방지
        q: this.address,
      });
    },
  },
};
</script>


<style>
.map-container {
  margin:50px 0;
  display: flex;
  align-items: center;
  justify-content: center;
  border:1px solid #dddddd;
  padding:20px 40px;

}
.address-wrapper{
  display: flex;
  flex:1;
}
.map-main {
  height: 400px;
  /* width: 400px; */
  flex:2;
  margin-left:40px;
  margin-top: 30px;
}


</style>