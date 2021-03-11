const express = require("express");
const router = express.Router();

const {
    verifyToken
} = require("../utils/jwt");
const {
    sequelize
} = require("../models");
const db = require("../models");
const Seq = require("sequelize")
const {
    upload
} = require("../utils/multer");
const fs = require("fs");

// 전체 방 가져오기
router.get("/", async (req, res) => {
    try {
        const roomInformations = await db["room"].findAll({
            include: [{
                model: db["room_image"]
            }, {
                model: db["room_option"]
            }],
            where: {
                location: {
                    [Seq.Op.like]: req.query.search ? `%${req.query.search}%` : `%%`
                }
            }
        })
        const makeImageUrl = (id) => `${req.protocol}://${req.get("host")}/api/room/image/${id}`;
        const plainInformations = roomInformations.map(el => el.get({
            plain: true
        }))
        const result = plainInformations.map(li => {
            if (li["room_images"].length) {
                li["room_images"] = li["room_images"].map(image => {
                    return {
                        ...image,
                        url: makeImageUrl(image.id)
                    }
                })
            }
            return li
        })
        console.log(plainInformations)
        console.log(roomInformations)
        return res.json(result);
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
});

// 방 정보 받아오기

router.get("/:id", async (req, res) => {
    try {
        return res.json({
            hello: "world"
        });
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
});

// 이미지 받아오기

router.get("/image/:id", async (req, res) => {
    try {
        const roomImage = await db["room_image"].findOne({
            where: {
                id: req.params.id
            }
        });
        if (roomImage.dataValues && roomImage.dataValues["file_name"]) {
            res.set('Content-Disposition', `inline; filename=room.png`);
            const file = fs.createReadStream(`uploads/${roomImage.dataValues["file_name"]}`);
            return file.pipe(res);
        }
        // console.log(roomImage);
        return res.json({
            hello: "world"
        });
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
});



// rooms table

// price
// room_size
// title
// content
// location
// latitude
// longitude
// 작성자 id(decoded)

//room_images table

// room_id
// file_name
// original_file_name

//room_options table

//room_id
//item
// 방 정보 작성하기
router.post("/", verifyToken, upload.array("room_image"), async (req, res) => {
    const transaction = await sequelize.transaction();
    try {
        const {
            price,
            room_size,
            title,
            content,
            location,
            latitude,
            longitude,
            item,
        } = req.body;
        console.log(req.body);

        // room create로 db에 insert

        // 작성된 room의 id를 기반으로 room_image와 room_option을 넣어야한다
        // transaction을 활용해서 전부 성공적으로 업로드 되는 경우에만 commit을 진행한다

        // room을 작성
        const room = await db["room"].create({
            title,
            content,
            price,
            room_size,
            location,
            latitude,
            longitude,
            user_id: req.decoded.id,
        }, {
            transaction: transaction
        });

        // 옵션 올리기
        // item 이 string형으로 올 때와 배열로 올 때 가 있다.
        if (item) {
            //item이 하나만 넘어올 때는 일반 string으로 넘어오고
            // 여러개 일 때는 배열로 넘어온다. 
            if (typeof item === "string") {
                await db["room_option"].create({
                    item: item,
                    room_id: room.dataValues.id
                }, {
                    transaction: transaction
                })
            } else {
                // Promise.all
                // const arr = ["A", "B", "C", "D"]
                // await arr[0]
                // await arr[1]  
                await Promise.all(
                    item.map(async (li) => {
                        await db["room_option"].create({
                            item: li,
                            room_id: room.dataValues.id
                        }, {
                            transaction: transaction
                        })
                    })
                )
            }
            if (req.files) {
                await Promise.all(req.files.map(async (li) => {
                    await db["room_image"].create({
                        file_name: li.filename,
                        original_file_name: li.originalname,
                        room_id: room.dataValues.id
                    }, {
                        transaction: transaction
                    })
                }))
            }
        }

        // 모든 요청이 성공적으로 진행되면 commit 을통해 일괄 db데이터 삽입
        transaction.commit();

        return res.json({
            status: "OK"
        });
    } catch (error) {
        console.log(error);
        // db에 올라가지 않게 처리
        transaction.rollback();
        // 만약에 에러가 났는데 이미지가 올라가는 경우
        // 삭제처리를 해줘야한다.
        if (req.files) {
            req.files.forEach((li) => {
                console.log(li.path);
                fs.unlink(li.path, (err) => {
                    if (err) {
                        console.log(err);
                    }
                });
            });
        }
        return res.json({
            status: "ERROR"
        });
    }
});

// 방 정보 업데이트

router.patch("/:id", async (req, res) => {
    try {
        return res.json({
            hello: "world"
        });
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
});

// 방 삭제

router.delete("/:id", async (req, res) => {
    try {
        return res.json({
            hello: "world"
        });
    } catch (error) {
        console.log(error);
        return res.json({
            hello: "Error"
        });
    }
});

module.exports = router;