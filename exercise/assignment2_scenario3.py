# Scenario 3: Transfer Funds & Verify Transaction


import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_transfer_funds(async_page):

    username = "test"
    password = "test123"
    transfer_amount = "10"

    await async_page.goto("https://parabank.parasoft.com/parabank/index.htm")

    await async_page.get_by_label("Username").fill(username)

    await async_page.get_by_label("Password").fill(password)

    await async_page.get_by_role("button", name="Log In").click()

    await expect(async_page.get_by_role("link", name="Accounts Overview")).to_be_visible()

    await async_page.get_by_role("link", name="Accounts Overview").click()

    await expect(async_page.get_by_role("heading", name="Accounts Overview")).to_be_visible()

    account_links = async_page.locator("#accountTable tbody tr td a")

    account_count = await account_links.count()

    assert account_count >= 2, (f"At least two accounts are required "f"for fund transfer. Found: {account_count}")

    from_account = await account_links.nth(0).inner_text()
    to_account = await account_links.nth(1).inner_text()

    from_account = from_account.strip()
    to_account = to_account.strip()

    print(f"From Account: {from_account}")
    print(f"To Account: {to_account}")

    await async_page.get_by_role("link", name="Transfer Funds").click()

    await expect(async_page.get_by_role("heading", name="Transfer Funds")).to_be_visible()

    await async_page.get_by_label("Amount").fill(transfer_amount)

    await async_page.locator("#fromAccountId").select_option(label=from_account)

    await async_page.locator("#toAccountId").select_option(label=to_account)

    await async_page.get_by_role("button", name="Transfer").click()

    await expect(async_page.get_by_text("Transfer Complete!")).to_be_visible()

    await expect(async_page.get_by_text(f"${transfer_amount}.00")).to_be_visible()

    print(f"Transfer of ${transfer_amount}.00 "f"completed successfully.")

    await async_page.get_by_role("link", name=to_account).click()

    await expect(async_page.get_by_role("heading", name="Account Details")).to_be_visible()

    transaction_table = async_page.locator("#transactionTable")

    await expect(transaction_table).to_be_visible()

    await expect(transaction_table).to_contain_text(f"${transfer_amount}.00")

    transaction_text = await transaction_table.inner_text()

    assert f"${transfer_amount}.00" in transaction_text, (f"Transferred amount ${transfer_amount}.00 ""was not found in transaction history.")

    print(
        f"Verified ${transfer_amount}.00 "
        f"transaction in account {to_account}."
    )