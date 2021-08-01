
// const express = require("express");
// const app = express();
// const PORT = 8080;

// app.use(express.json())
// app.use(express.urlencoded({extendedL: false}))
// app.use((req, res, next) => {
//     console.log("동작 합니다.")
//     next()
// })
// const textMiddleware2 = (req, res, next) => {
//     req.b = 15
//     next()
// }
// const textMiddleware = (req, res, next) => {
//     req.a = 30
//     next()
// }
// app.get("/", (req, res) => {
//     res.send("hello")
// })
// app.get("/add", textMiddleware, (req, res) => {
//     console.log(req.a + req.a)

// })
// app.get("/other", textMiddleware,textMiddleware2, (req, res) => {
//     console.log(req.a + req.b)

// })
// app.get("/multi", textMiddleware, (req, res) => {
//     console.log((req.a) * (req.a))

// })
// app.get("/sub", textMiddleware, (req, res) => {
//     console.log(req.a -1)

// })
// app.listen(PORT, () => console.log(`this server listening on ${PORT}`))

const express = require('express');
const app = express();
const PORT = 8080;
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.use((req, res, next) => {
    req.a = 30;
    next();
} )
const otherMiddleware = (req, res, next) => {
    req.b = 15;
    next();
}
app.get("/", (req, res) => {
    console.log("hello");
    console.log(req.a);
    return res.json({a:req.a})
});
app.get("/sub", (req, res) => {
    const a = req.a -1;
    console.log(a);
    return res.json({a:a});
})
app.get("/multi", (req, res, next) => {
    const a = req.a * req.a;
    return res.json({a:a});
})
app.get("/other",otherMiddleware, (req, res) => {
    const sum = req.a + req.b;
    return res.json({sum:sum})
})
app.listen(PORT, () => console.log(`this server listening on ${PORT}`));