const puppeteer = require("puppeteer")
const fs = require("fs").promises

const main = async() => {
    //default는 headless 상태
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage()
    
    await page.goto("https://www.naver.com")

    await page.waitForTimeout(6000);

    const html = await page.content()

    await fs.writeFile("example.html", html)
    await browser.close()
}

main()