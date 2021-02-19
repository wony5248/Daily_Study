const puppeteer = require("puppeteer");

(async function () {
    const browser = await puppeteer.launch({
        headless: false,
        args: ["--window-size=1920,1080"]
    })
    const page = await browser.newPage()
    page.setViewport({
        width: 1920,
        height: 1080
    })
    await page.goto("https://www.google.com", {waitUntil : "networkidle2"})
    await page.evaluate(() => {
        document.querySelector(".gLFyf").value = "치킨"

    })
    await page.keyboard.press("Enter")
})
