const express = require("express")
const router = express.Router()
const {
    hashPassword,
    comparePassword
} = require("../utils/bcrypt")
const db = require("../models/index")
const {
    verifyToken
} = require("../utils/jwt")
const jwt = require("jsonwebtoken")
const {
    upload
} = require("../utils/multer")
const fs = require("fs")
//기능 정의

//get post patch delete
//3차 라우터
///api/user

//회원가입 post
router.post("/", async (req, res) => {
    try {
        const {
            name,
            email,
            password,
            type
        } = req.body
        const hashedPassword = await hashPassword(password);
        console.log(hashedPassword)
        const result = await db["user"].create({
            name: name,
            email,
            password: hashedPassword,
            type,
        })
        return res.json({
            status: "OK"
        })
    } catch (error) {
        console.log(error)
        return res.json({
            status: "ERROR"
        })
    }
})

//로그인 post
router.post("/login", async (req, res) => {
    try {
        const {
            email,
            password
        } = req.body
        console.log(email, password)
        const userData = await db["user"].findOne({
            attributes: ["id", "password", "name"],
            where: {
                email
            }
        })
        console.log(userData)
        const compareResult = await comparePassword(password, userData.dataValues.password)
        console.log(compareResult)
        if (compareResult) {
            const token = jwt.sign({
                id: userData.dataValues.id
            }, "ssafy", {
                expiresIn: "24h"
            })

            return res.json({
                resultCode: 200,
                token: token,
                id: userData.dataValues.id,
                name: userData.dataValues.name
            })
        }
        // return res.json({
        //     hello: "world"
        // })
    } catch (error) {
        console.log(error)
        return res.json({
            status: "error"
        })
    }
})

//프로필 업로드 post
router.post("/:id/profile", verifyToken, upload.single("profile"), async (req, res) => {
    try {
        console.log(req.params)
        const userInformation = await db["user"].findOne({
            where: {
                id: req.decoded.id
            }
        })
        console.log(userInformation.dataValues)
        if (userInformation.dataValues && userInformation.dataValues.profile) {
            fs.unlink(`uploads/${userInformation.dataValues.profile}`, function (error) {
                if (error) {
                    console.log(error)
                }
            })
        }

        await db["user"].update({
            profile: req.file.filename
        }, {
            where: {
                id: req.decoded.id
            }
        })
        return res.json({
            status: "OK"
        })
    } catch (error) {
        console.log(error)
        return res.json({
            status: "ERROR"
        })
    }
})

//회원 전체의 정보 가져오기 get
router.get("/", async (req, res) => {
    try {
        return res.json({
            hello: "world"
        })
    } catch (error) {
        console.log(error)
        return res.json({
            hello: "error"
        })
    }
})

//회원 하나의 정보 get
router.get("/:id",async (req, res) => {
    console.log("test", req.body)
    try {
        const userInformation = await db["user"].findOne({
            attributes:["id", "name", "email"],
            where: {
                id: req.params.id
            }
            
        });
        // console.log(roomImage);
        // console.log(userInformation)
        return res.json(userInformation);
        
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
})

//프로필 이미지 가져오기 get
router.get("/:id/profile", verifyToken,async (req, res) => {
    try {
        const userInformation = await db["user"].findOne({
            attributes: ["id", "profile"],
            where: {
                id: req.params.id
            }
        })
        if (userInformation.dataValues && userInformation.dataValues.profile) {
            res.set("Content-Disposition", "inline; filename=profile.png")
            const file = fs.createReadStream(`uploads/${userInformation.dataValues.profile}`)

            return file.pipe(res)
        }
        return res.json({
            hello: "world"
        })
    } catch (error) {
        console.log(error)
        return res.json({
            hello: "error"
        })
    }
})

// router.get("/image/:id", async (req, res) => {
//     try {
//       const roomImage = await db["room_image"].findOne({
//           where:{
//               id: req.params.id
//           }
//       });
//       if(roomImage.dataValues && roomImage.dataValues["file_name"]){
//           res.set('Content-Disposition', `inline; filename=room.png`);
//           const file = fs.createReadStream(`uploads/${roomImage.dataValues["file_name"]}`);
//           return file.pipe(res);
//       }
//       // console.log(roomImage);
//       return res.json({ hello: "world" });
//     } catch (error) {
//       console.log(error);
//       return res.json({ hello: "Error" });
//     }
//   });


//유저 정보 업데이트 patch
router.patch("/:id", async (req, res) => {
    try {
        const {name, password} = req.body
        const hashedPassword = await hashPassword(password)
        const result = await db["user"].update({
            name: req.body.name,
            password: hashedPassword
        },{
            where: {
                id:req.params.id
            }
        })
        return res.json({
            status: "변경이 완료되었습니다."
        })
    } catch (error) {
        console.log(error)
        return res.json({
            hello: "error"
        })
    }
})





//탈퇴 delete
router.delete("/:id", verifyToken,async (req, res) => {
    try {
        //paranoid true시 실제 삭제되지는 않고 deletedAt에 표시
        const result = await db["user"].destroy({
            where:{
                id: req.params.id
            }
        })
        return res.json({
            hello: "world"
        })
    } catch (error) {
        console.log(error)
        return res.json({
            hello: "error"
        })
    }
})


module.exports = router