//json web token
const jwt = require("jsonwebtoken")


const verifyToken = (req, res, next) => {
    try {
        req.decoded = jwt.verify(req.headers.authorization, "ssafy")
        console.log(req.decoded)
        return next()
    } catch (error) {
        return res.json(error)
    }
}

module.exports = {verifyToken}