const express = require("express");
const app = express();
const PORT = 8080;
const axios = require("axios")

app.use(express.json())
app.use(express.urlencoded({
    extended: true
}))
app.set("view engine", "ejs")

app.get("/:page?", async (req, res) => {
    try {
        const allPosts = await axios.get("https://jsonplaceholder.typicode.com/albums/");
        const count = allPosts.data.length;
        console.log(count)

        const page = req.query.page
        console.log(page)
        const response = await axios.get("https://jsonplaceholder.typicode.com/albums/", {
            params: {
                _start: page && page > 0 ? 9 * (page - 1) : 0,
                _limit: 9
            }
        })
        // console.log(response.data)
        res.render("index", {
            data: response.data,
            count: count,
            page: page ? page : 1
        })
    } catch (error) {
        res.render("error")
    }
})
app.listen(PORT, () => console.log(`this server listening on ${PORT}`))