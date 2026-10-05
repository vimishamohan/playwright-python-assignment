#Scenario 2: Open New Account & Verify Account

import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_open_new_account(async_page):

    username = "test"
    password = "test123"


    await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")

    await async_page.get_by_label("Username").fill(username)

    await async_page.get_by_label("Password").fill(password)

    await async_page.get_by_role("button", name="Log In").click()

    await expect(async_page.get_by_role("link", name="Accounts Overview")).to_be_visible()

    await async_page.get_by_role("link", name="Open New Account").click()

    await expect(async_page.get_by_role("heading", name="Open New Account")).to_be_visible()

    account_type = async_page.locator("#type")

    await account_type.select_option(label="SAVINGS")

    from_account = async_page.locator("#fromAccountId")

    account_options = from_account.locator("option")

    option_count = await account_options.count()

    assert option_count > 0, ("No existing account is available to create ""the new account.")

    first_account_value = await account_options.nth(0).get_attribute("value")

    await from_account.select_option(first_account_value)

    await async_page.get_by_role("button", name="Open New Account").click()

    await expect(async_page.get_by_text("Account Opened!")).to_be_visible()

    new_account_link = async_page.locator("#newAccountId")

    await expect(new_account_link).to_be_visible()

    new_account_number = (await new_account_link.inner_text())

    print(f"Newly created account number: "f"{new_account_number}")

    assert new_account_number.strip() != "", ("New account number was not generated.")

    await async_page.get_by_role("link", name="Accounts Overview").click()

    await expect(async_page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

    account_overview = async_page.locator("#accountTable")

    await expect(account_overview).to_contain_text(new_account_number)

    assert new_account_number in (await account_overview.inner_text())

    print(f"Verified account {new_account_number} "f"in Accounts Overview.")