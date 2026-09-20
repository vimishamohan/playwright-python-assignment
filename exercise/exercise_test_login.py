from playwright.sync_api import sync_playwright


def test_login():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto("https://demowebshop.tricentis.com")
        page.get_by_role("link", name="Log in").click()
        page.get_by_role("textbox", name="Email").fill("abc@gmail.com")
        page.get_by_role("textbox", name="Password").fill("123456")
        page.get_by_role("button", name="Log In").click()

        browser.close()