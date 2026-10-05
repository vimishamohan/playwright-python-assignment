#Scenario 1: User Registration & Account Verification

import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_parabank_user_registration(async_page):

    username = "TestUser123"
    password = "Test@12345"

    customer_data = {
        "first_name": "Test",
        "last_name": "User",
        "address": "123 Test Street",
        "city": "Kochi",
        "state": "Kerala",
        "zip_code": "682001",
        "phone": "9876543210",
        "ssn": "123456789"
    }

    await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")

    await expect(async_page).to_have_title("ParaBank | Welcome | Online Banking")

    await async_page.get_by_role("link", name="Register").click()

    await expect(async_page.get_by_role("heading", name="Signing up is easy!")).to_be_visible()

    await async_page.locator("#customer\\.firstName").fill(customer_data["first_name"])

    await async_page.locator("#customer\\.lastName").fill(customer_data["last_name"])

    await async_page.locator("#customer\\.address\\.street").fill(customer_data["address"])

    await async_page.locator("#customer\\.address\\.city").fill(customer_data["city"])

    await async_page.locator("#customer\\.address\\.state").fill(customer_data["state"])

    await async_page.locator("#customer\\.address\\.zipCode").fill(customer_data["zip_code"])

    await async_page.locator("#customer\\.phoneNumber").fill(customer_data["phone"])

    await async_page.locator("#customer\\.ssn").fill(customer_data["ssn"])

    await async_page.locator("#customer\\.username").fill(username)

    await async_page.locator("#customer\\.password").fill(password)

    await async_page.locator("#repeatedPassword").fill(password)

    await async_page.get_by_role("button", name="Register").click()


    await expect(async_page.get_by_text(f"Welcome {username}")).to_be_visible()

    await expect(async_page.get_by_role("link", name="Log Out")).to_be_visible()

    await expect(async_page.get_by_text(f"Welcome {username}")).to_be_visible()

    await async_page.get_by_role("link", name="Accounts Overview").click()

    await expect(async_page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

    account_links = async_page.locator("table#accountTable tbody tr td a")

    await expect(account_links.first).to_be_visible()

    account_count = await account_links.count()

    assert account_count >= 1, (f"Expected at least one account, "f"but found {account_count}")

    print(f"Account count: {account_count}")

    await async_page.get_by_role("link", name="Log Out").click()

    await expect(async_page.get_by_role("link", name="Log In")).to_be_visible()