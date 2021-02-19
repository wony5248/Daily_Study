const puppeteer = require("puppeteer")


const main = async() => {
    //pdf 생성때는 headless 여야 함
    const browser = await puppeteer.launch()
    const page = await browser.newPage()
    await page.goto("https://google.com", {waitUntil : "networkidle2"})
    await page.pdf({path: "test.pdf", format:"A4"})
    await browser.close()
}


main()