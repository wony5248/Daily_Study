const AdmZip = require("adm-zip");
const express = require("express");
const app = express();
const multer = require("multer")
const path = require("path")
const PORT = 8080;
const fs = require("fs")
app.use(express.json());
app.use(express.urlencoded({
    extended: false
}));
app.set("view engine", "ejs")

const upload = multer({
    storage: multer.diskStorage({
        destination: (req, file, done) => {
            done(null, "uploads/")
        },
        filename: (req, file, done) => {
            const ext = path.extname(file.originalname)
            done(null, path.basename(file.originalname, ext) + Date.now() + ext)
        }
    }),

    limits: {
        fileSize: 5 * 1024 * 1024
    }
})


app.get("/", (req, res) => {
    return res.render("index")
})

app.post("/upload", upload.single("userFile"), (req, res) => {
    console.log(req.file)
    return res.json({
        file: req.file
    })
})

app.post("/upload-multiple", upload.array("many"), (req, res) => {
    console.log(req.files)
    return res.json({
        files: req.files
    })
})


//download
app.get("/download", (req, res) => {
    // stream 방법
    // 스트림이란 배열이나 문자열 같은 데이터 컬렉션
    // 큰데이터를 가져올 때 나 외부소스로부터 분할해서 나눠 가져올 때 유용하다
    // 일반적으로 readFile은 파일 전체를 메모리에 올려놓기 때문에 메모리 사용이 크다

    // 50메가의 이미지가 있습니다 
    // readFile로 읽어서 send로 보낸다 
    // readFile은 50메가를 통쨰로 읽어서 보낸다

    // pipe
    // 파일을 읽어서 데이터 입력 -> 입력 스트림 -> 출력 스트림 -> 출력 
    // 서버의 자원을 입력받아서 클라이언트로 연결된 출력 스트림으로 내보낸다.

    const file = fs.readFileSync(`${__dirname}/uploads/baloon1.jpg`);
    res.send(file);

    // AWS S3
    // 대용량업로드할때 Lamda

    // res.set('Content-Disposition', 'attachment; filename=aaa.png');
    // res.set('Content-Type', 'application/octet-stream');
    // const file = fs.createReadStream(`${__dirname}/uploads/balloon1.jpg`);
    // file.on('data', function(data){
    //     console.log(data);
    // })
    // file.on('end', function(){
    //     console.log("읽기 종료");
    // })
    // return file.pipe(res);

    // 쉬운 방법 

    // 저장후 서버 재기동
    // 캐시 날리는법 -> 컨트롤 쉬프트 R 
    return res.download('uploads/baloon1.jpg', "테스트.jpg");
})
//zip 파일 다운로드
app.get("/download-zip", (rez, res) => {
    try {
        const zip = new AdmZip()

        zip.addLocalFile("./uploads/baloon1.jpg")
        zip.addLocalFile("./uploads/baloon1.jpg")
        zip.addLocalFile("./uploads/baloon1.jpg")

        const willSendThis = zip.toBuffer()

        zip.writeZip("uploads/test.zip")
        res.download("uploads/test.zip")

    } catch (error) {
        console.log(error)
    }
})


app.listen(PORT, () => console.log(`this server listening on ${PORT}`))