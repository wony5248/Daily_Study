const express = require("express");
const{pool} = require("./mysql");
const app = express();
const PORT= 8080;

app.use(express.json());
app.use(express.urlencoded({extended: false}));

app.get("/", async(req, res) => {
    const response = await pool.query("selet * from user")
    console.log(response)
    return res.json(response[0])
})

app.post("/", async(req, res) => {
    try{
        console.log(req.body.name)
        const data = await pool.query("insert into user set ?" ,{name:req.body.name})
        return res.json({hello: "hello"})
    }
    catch (error) {
        console.log(error)
    }
})

app.listen(PORT, () => console.log(`this server listening on ${PORT}`))