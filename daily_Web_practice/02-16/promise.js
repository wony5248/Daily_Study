//기다려 -> 먹어 -> 잘 했어
//callback
function eatSetTime() {
    console.log("기다려");
    setTimeout(function(){
        console.log("먹어");
        console.log("잘했어");
    },2000)
}


//promise
function eat(){
    return new Promise(function(resolve, reject){
        setTimeout(function(){
            resolve("먹어")
        }, 2000)
    })
}

// console.log("기다려")
// eat().then(data => console.log(data)).then(()=> {
//     console.log("잘했어")
// })

//async
async function wait(){
    console.log("기다려");
    const data = await eat();
    console.log(data);
    console.log("잘했어")
}
wait()
