from playwright.sync_api import sync_playwright

def test_google_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://www.google.com")
        print("Title: ",page.title())
        print("URL: ",page.url)
        page.screenshot(path="screenshots/google.png")
        browser.close()
        