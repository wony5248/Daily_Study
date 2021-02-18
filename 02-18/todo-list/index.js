const express = require("express");
const {
    pool
} = require("./mysql");
const app = express();
const PORT = 8080;

app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));
app.set("view engine", "ejs")


// 기본 html 구성
// form 태그에서 data를 서버에 전송
// form 태그에서 받은 data db에 넣기
// db에 넣은 데이터를 가져오기
// 수정 및 삭제하기

app.get("/", async (req, res) => {
    try {
        const data = await pool.query("select * from todo");
        return res.render("index", {
            data: data[0]
        })
    } catch (error) {
        console.log(error)
        res.render("error", {
            title: "ERROR",
            data: error
        })
    }
})

app.post("/add", async (req, res) => {
    console.log("잘 들어옵니다.")
    console.log(req.body.todo);
    try {
        const data = await pool.query("insert into todo SET ?", [{
            todo: req.body.todo,
            checked: false
        }])
        res.redirect("/")
    } catch (error) {
        console.log(error)
        res.render("error", {
            title: "ERROR",
            data: error
        })
    }
})


app.get("/delete/todo/:id", async (req, res) => {
    try {
        //req.params.id
        const {
            id
        } = req.params
        const data = await pool.query("delete from todo where ?", [{
            id: id
        }]) // 두개가 같을때에는 {id} 로 해줘도 됨
        res.redirect("/")
    } catch (error) {
        console.log(error)
        res.render("error", {
            title: "ERROR",
            data: error
        })
    }
})

app.get("/update/todo/check/:id", async (req, res) => {
    try {
        console.log(req.params)
        console.log(req.query)
        const data = await pool.query("update todo set checked = ? where id = ?", [req.query.checked, req.params.id])
        res.redirect("/")
    } catch (error) {
        console.log(error)
        res.render("error", {
            title: "ERROR",
            data: error
        })
    }
})

app.listen(PORT, () => console.log(`this server listening on ${PORT}`))