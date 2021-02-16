const e = require("express");
const express = require("express");
const app = express();
const PORT = 8080;

app.use(express.json())

app.use((req, res, next) => {
    console.log("동작 합니다.")
    next()
})

const textMiddleware = (req, res, next) => {
    console.log("특정 부분에서만 동작합니다")
    req.aa = "aa"
    next()
}
app.get("/", (req, res) => {
    res.send("hello")
})
app.get("/test", textMiddleware, (req, res) => {
    console.log(req.aa)
    res.send("test")
})

app.get("/test", textMiddleware, (req, res) => {
    console.log(req.aa)
    res.json({aa: req.aa})
})
app.listen(PORT, () => console.log(`this server listening on ${PORT}`))