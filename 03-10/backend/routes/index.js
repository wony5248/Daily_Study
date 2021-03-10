const express = require("express")
const userRouter = require("./user.js")
const roomRouter = require("./room.js")

const router = express.Router()
//2차 라우터
//http://localhost:8000/api/user라고 시작되면 모두 userRouter로 감
router.use("/api/user", userRouter)
router.use("/api/room", roomRouter)
module.exports = router