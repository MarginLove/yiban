import pyppeteer
import asyncio


async def main():
    browser = await pyppeteer.launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')
    await page.goto('https://www.baidu.com')
    await browser.close()  # 关闭

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
