#Exercise 7

import os
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()

def test_prd():

    base_url = os.getenv("BASE_URL")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(base_url)
        print("BASE_URL:", base_url)
        print("Page Title:", page.title())
        browser.close()