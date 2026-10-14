import re
import asyncio 
# import pytest
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

url_list = ['https://example.com', 'https://httpbin.org/html', 'https://python.org']

async def test_main(url,browser):

        page = await browser.new_page()
        try:
            async with asyncio.timeout(5.0):
                await page.goto(url)
                title = await page.title()
                return {"URL": url, "Title": title}

        except asyncio.TimeoutError:
             print(f"[Timeout] Failed to load {url} within 5 seconds.")

        except PlaywrightTimeoutError  as e:
             print(f"[Playwright error ] as {e}")
             return {"URL": url, "Error": str(e), "status": "FAILED"}

        except Exception as e:
             print(f"[Error] An error occurred while loading {url}: {e}")
             return {"URL": url, "Error": str(e), "status": "FAILED"}       

        finally:
            await page.close()

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        tasks = [test_main(url, browser) for url in url_list]
        await asyncio.gather(*tasks)

        await browser.close()

asyncio.run(main())

