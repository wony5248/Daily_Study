const http = require("http")
const fs = require("fs").promises
const PORT = 8080

const server = http.createServer(async (req, res) => {
    try{
        console.log(req.method)
        console.log(req.url)
        if(req.method === "GET"){
            if(req.url === "/"){
                res.writeHead(200, {"Contente-Type": "text.html; charset=utf-8"})
                const data = await fs.readFile("index.html")
                return res.end(data)
            }
            else if(req.url === "/a"){
                res.writeHead(200, {"Contente-Type": "text.html; charset=utf-8"})
                const data = await fs.readFile("a.html")
                return res.end(data)
            }
            else if(req.url === "/b"){
                res.writeHead(200, {"Contente-Type": "text.html; charset=utf-8"})
                const data = await fs.readFile("b.html")
                return res.end(data)
            }
        }
    }catch(error){

    }
})

server.listen(PORT,() =>console.log(`this server listening on ${PORT}`))