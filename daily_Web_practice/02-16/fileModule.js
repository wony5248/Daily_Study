const fs = require("fs").promises
module.exports = {
    hello: fs.readFile("./nameList.txt").then(data => {
        console.log(data.toString())
    }).catch(err => console.log(err))
}
