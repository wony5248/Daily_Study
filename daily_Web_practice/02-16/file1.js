//callback file 읽기
// const fs = require("fs");

// fs.readFile("./contents.txt", (err, data) => {
//     if(err){
//         throw err;
//     }
//     console.log(data.toString())
// })


//promise 방식

// const fs = require("fs").promises;

// fs.readFile("./contents.txt").then(data => {
//     console.log(data.toString())
// }).catch(err => console.log(err))

// async
(async function() {
    try{
        const data = await fs.readFile("./contents.txt");
        console.log(data.toString())
    }
    catch{
        console.log(err)
    }
})