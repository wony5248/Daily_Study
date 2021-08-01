//배경 변경 함수
async function setRenderBackground() {
    const result = await axios.get("https://picsum.photos/1280/720", {
        responseType: "blob"
    })
    // console.log(result.data)
    const data = URL.createObjectURL(result.data)
    // console.log(data)
    document.querySelector("body").style.backgroundImage = `url(${data})`
    //img 에 url로
}
//시계 설정 함수
function setTime() {
    const timer = document.querySelector(".timer")
    const text = document.querySelector(".timer-content")
    setInterval(() => {

        const date = new Date()

        timer.textContent = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`
        if(date.getHours() < 12){
            text.textContent = "Good morning Beomjin"
        }
        else{
            text.textContent = "Good evening Beomjin"
        }
    }, 1000)

}

//메모 불러오기
function getMemo() {
    const memo = document.querySelector(".memo")
    const memoValue = localStorage.getItem("todo")
    memo.textContent = memoValue
}

//메모 저장
function setMemo() {
    const memoInput = document.querySelector(".memo-input")
    memoInput.addEventListener("keyup", function (e) {
        console.log(e.code)
        console.log(e.target.value)
        if ((e.code === "Enter" || e.code === "NumpadEnter") && e.target.value) {
            localStorage.setItem("todo", e.target.value)
            getMemo()
            memoInput.value = ""
        }
    })
}

//메모 삭제
function deleteMemo() {
    document.addEventListener("click", function (e) {
        if (e.target.classList.contains("memo")) {
            localStorage.removeItem("todo")
            e.target.textContent = ""
        }
    })
}


//위도 경도  가져오기 -> promise
function getPosition(options) {
    return new Promise(function (resolve, reject) {
        navigator.geolocation.getCurrentPosition(resolve, reject, options)
    })
}

//날씨가져오기
async function getWeather(latitude, longitude) {
    //위도와 경도가 있는 경우
    if (latitude && longitude) {
        const data = await axios.get(`http://api.openweathermap.org/data/2.5/forecast?lat=${latitude}&lon=${longitude}&appid=3cda30c79e3072e132c06c73f451245f`)
        return data
    }
    //위도와 경도 없는 경우
    const data = axios.get(`http://api.openweathermap.org/data/2.5/forecast?q=Seoul&appid=3cda30c79e3072e132c06c73f451245f`)
    return data
}
// getWeather("", "").then(li => console.log(li))


function matchIcon(weatherData) {
    if (weatherData === "Clear") return "./images/039-sun.png";
    if (weatherData === "Clouds") return "./images/001-cloud.png";
    if (weatherData === "Rain") return "./images/003-rainy.png";
    if (weatherData === "Snow") return "./images/006-snowy.png";
    if (weatherData === "Thunderstorm") return "./images/008-storm.png";
    if (weatherData === "Drizzle") return "./images/031-snowflake.png";
    if (weatherData === "Atmosphere") return "./images/033-hurricane.png";
}

function getTodayLabel() {

    var week = new Array('일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일');

    var today = new Date().getDay();
    var todayLabel = week[today];

    return todayLabel;
}



//modal 부분 컴포넌트
function weatherWrapperComponent(li) {
    console.log(li)
    var day = new Date(`${li.dt_txt.split(" ")[0]}`).getDay()
    // var test =new Date(`${li.dt_txt.split(" ")[0]}`)
    // console.log(test)
    var week = new Array('일', '월', '화', '수', '목', '금', '토');
    //tofixed 소수점 고정
    // console.log(li)
   
    const changeToCelsius = temp => (temp - 273.15).toFixed(1)
    return `<div class="card shadow-sm bg-transparent mb-3 m-2 flex-grow-1">
    <div class="card-header text-white text-center">
        ${li.dt_txt.split(" ")[0]} ${week[day]}
    </div>
    <div class="card-body d-flex">
      <div
        class="flex-grow-1 d-flex flex-column justify-content-center align-items-center"
      >
        <h5 class="card-title">${li.weather[0].main}</h5>
        <img
          src = ${matchIcon(li.weather[0].main)}
          width="60px"
          height="60px"
        />
        <p class="card-text">${changeToCelsius(li.main.temp)}</p>
      </div>
    </div>
  </div>`
}


//위도와  경도를  받아서 데이터를 받아오기
async function renderWeather() {
    let latitude = ""
    let longitude = ""
    try {
        const position = await getPosition()
        latitude = position.coords.latitude
        longitude = position.coords.longitude
        return

    } catch (error) {
        console.log(error)
    } finally {
        console.log("test")
        const {
            data
        } = await getWeather(latitude, longitude)
        // console.log(data)
        const weatherList = data.list.reduce((acc, cur) => {
            if (cur.dt_txt.indexOf("18:00:00") > 0) {
                acc.push(cur)
            }
            return acc
        }, [])
        console.log(weatherList[0].weather[0])
        document.querySelector(".modal-button").style.backgroundImage = `url(${matchIcon(weatherList[0].weather[0].main)})`
        const modalBody = document.querySelector(".modal-body")
        modalBody.innerHTML = weatherList.reduce((acc, cur) => {
            //컴포넌트 제작 예정
            acc += weatherWrapperComponent(cur)
            return acc
        }, "")

    }
}

(function () {
    setRenderBackground();
    setInterval(() => {
        setRenderBackground();
    }, 5000);
    setTime()
    setMemo()
    getMemo()
    deleteMemo()
    renderWeather()
})();