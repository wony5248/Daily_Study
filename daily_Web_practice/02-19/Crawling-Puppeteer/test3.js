const puppeteer = require("puppeteer");

(async function () {
    const browser = await puppeteer.launch({
        headless: false,
        args: ["--window-size=1920, 1080"]
    })

    const page = await browser.newPage()
    page.setViewport({
        width:1920,
        height:1080
    })

    await page.goto("https://www.naver.com")

    await page.evaluate(() => {
        document.querySelector("#query").value = "치킨"
        document.querySelector("#search_btn").click()
    })

    await page.waitForTimeout(6000)
    await page.screenshot({path: 'chicken.jpg', fullPage:true})
    await browser.close()
})();