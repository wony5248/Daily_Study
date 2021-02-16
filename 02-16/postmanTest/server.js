const express = require('express');
const app = express();
const PORT = 8080;
const morgan = require('morgan');
const dotenv = require('dotenv');
dotenv.config();
app.use(morgan("dev"));
app.use(express.json());
app.use(express.urlencoded({extended: false}));
app.get("/",(req, res) => {
    console.log("test");
    console.log(process.env.TEST)
    return res.json({hello:"get hello"})
});
app.get("/:id",(req, res) => {
    console.log(req.params);
    console.log(req.query);
    return res.json({hello:"get hello"})
})
app.post("/", (req, res) => {
    console.log(req.body);
    return res.json({hello:"post hello"})
})
app.patch("/", (req, res) => {
    return res.json({hello:"patch hello"})
})
app.delete("/", (req, res) => {
    return res.json({hello:"delete hello"})
})
app.listen(PORT, () => console.log(`this server listening on ${PORT}`));