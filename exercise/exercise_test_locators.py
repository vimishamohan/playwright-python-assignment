import os

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright


load_dotenv()


def test_google_search():

    base_url = os.getenv("BASE_URL")

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(base_url)

        page.locator("textarea[name='q']").click()

        page.locator("textarea[name='q']").fill("Akbartravels.com")

        page.locator("textarea[name='q']").press("Enter")

        print("Page Title:", page.title())

        browser.close()