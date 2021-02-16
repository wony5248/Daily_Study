const modules = require("./module1")

console.log(modules)

//비구조화 할당
const {name1, name2, hello} = require("./module1")
console.log(name1)
console.log(name2)
hello()