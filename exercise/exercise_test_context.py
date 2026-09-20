#Exercise 6

from playwright.sync_api import sync_playwright


def test_two_contexts():

    with sync_playwright() as p:

        browser1 = p.chromium.launch(headless=False)
        browser2 = p.firefox.launch(headless=False)

        context1 = browser1.new_context()
        context2 = browser2.new_context()

        page1 = context1.new_page()
        page2 = context2.new_page()

        page1.goto("https://www.google.com")
        page2.goto("https://www.youtube.com")

        print("Context 1 title:", page1.title())
        print("Context 2 title:", page2.title())

        context1.close()
        context2.close()

        browser1.close()
        browser2.close()