const express = require("express");
const app = express();
const PORT = 8080;
const db = require("./models/index")

app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));

app.get("/book", async (req, res) => {
    try {
        const data = await db["book"].findAll()
        return res.json(data)
    } catch (error) {
        return res.json(error)
    }
})
app.get("/book/:id", async (req, res) => {
    try {
        const data = await db["book"].findOne({
            where: {
                id: req.params.id
            }
        })
        return res.json(data)
    } catch (error) {
        return res.json(error)
    }
})
app.post("/book", async (req, res) => {
    try {
        // const{firstName, lastName} = req.body // 아래 방식이랑 같음
        // const data = await db["user"].create({
        //     firstName,
        //     lastName,
        // })
           const data = await db["book"].create({
            id: req.body.id,
            title: req.body.title,
            author: req.body.author,
        })
        return res.json(data)
    } catch (error) {
        console.log(error)
        return res.json(error)
    }
})
app.patch("/book/:id", async (req,  res) => {
    try {
        const {id} = req.params
        const {author, title} = req.body
        const data = await db["book"].update({
            title:title,
            author:author
        }, {
            where:{
                id:id
            }
        })
        return res.json(data)
    } catch (error) {
        console.log(error)
        return res.json(error)
    }
})

app.delete("/book/:id" , async(req, res) =>{
    try {
        const {id} = req.params
        const data = db["book"].destroy({
            where: {
                id:id
            }
        })
        return res.json(data)
    } catch (error) {
        console.log(error)
        return res.json(error)
    }
})
app.listen(PORT, () => console.log(`this server listening on ${PORT}`))