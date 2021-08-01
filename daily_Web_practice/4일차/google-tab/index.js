const bodyBackground = document.querySelector(".body-background");
const toggleButton = document.querySelector(".toggle-button");
const headerNav = document.querySelector(".header-nav-list-wrapper");
const bookmarWrapper = document.querySelector(".bookmark-wrapper");
const searchInput = document.querySelector("#search-input");



const imgIconWrappers = document.querySelectorAll(".img-icon-wrapper");
const bookmarkTexts = document.querySelectorAll(".bookmark-text");

toggleButton.addEventListener("click", function(){
    toggleButton.textContent ="다크 모드";
    toggleButton.classList.toggle("toggle-button-darkmode");
    bodyBackground.classList.toggle("body-background-darkmode");

    if(toggleButton.classList.contains("toggle-button-darkmode")){
        toggleButton.textContent = "일반 모드";
    }
    for(let i=0; i<imgIconWrappers.length; i++){
        imgIconWrappers[i].classList.toggle("img-icon-wrapper-darkmode");
    }
    for(let i=0; i<bookmarkTexts.length; i++){
        bookmarkTexts[i].classList.toggle("text-darkmode")
    }
})

searchInput.addEventListener("keyup", function(e){
    if(e.code ===  "Enter"){
        console.log(e.target.value);
        if(!e.target.value){
            alert("검색어를 입력하시지 않았습니다.");
            return;
        }
        location.href=`https://www.google.com/search?q=${e.target.value}`;
        // window.open(`https://www.google.com/search?q=${e.target.value}`)
    }
})