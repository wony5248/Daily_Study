const express = require("express");
const app = express();
const PORT = 8080;

app.use(express.json())

app.use(express.urlencoded({extended:false}))




app.get("/", (req, res) => {
    res.sendFile(`${__dirname}`)
})

app.listen(PORT, () => console.log(`this server listening on ${PORT}`))