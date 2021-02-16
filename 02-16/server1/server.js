const http = require("http");
const PORT = 8080;
const fs = require("fs").promises

// const server = http.createServer((req,res) =>{

//     res.writeHead(200, "text/html: charset=utf8")

//     res.write("<h1>hello World</h1>")

//     res.end("<p>hello Server</p>")
// })

// server.listen(PORT,() =>console.log(`this server listening on ${PORT}`))



const server1 = http.createServer(async (req, res) => {
    try{
        const htmlData = await fs.readFile("index.html");
        res.writeHead(200, {"Content-Type": "text.html; charset=utf-8"})
        res.end(htmlData)
    }catch(error){
        console.log(error);
        res.writeHead(200, {"Content-Type": "text.html; charset=utf-8"})
        res.end(error)
    }
})

server1.listen(PORT,() =>console.log(`this server listening on ${PORT}`))