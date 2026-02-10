import re
import pytest
import time
from playwright.sync_api import Page, expect


def test_example(page: Page):
    page.goto("https://qat-scdashboard.sureprep.com/")
    page.get_by_role("link", name="CONTINUE").click()
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("tejas.kadam@thomsonreuters.com")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_role("textbox", name="ex. 6036943, C603694, X696046").click()
    page.get_by_role("textbox", name="ex. 6036943, C603694, X696046").fill("6124436")
    page.locator("#password").click()
    page.locator("#password").fill("zzz")
    page.locator("label div").filter(has_text="Remember my username").locator("div").click()
    page.get_by_text("Sign On").click()
    '''page.goto("https://qat-scdashboard.sureprep.com/SSO/Location")
    page.locator(".k-select").click()
    page.get_by_role("option", name="Test").click()
    page.locator(".mdl-button__ripple-container").click()
    page.wait_for_timeout(5000)
    page.goto("https://qat-scdashboard.sureprep.com/dashboard/home")
    page.get_by_role("button", name="Toggle navigation").click()
    page.get_by_role("link", name="Test Verification").click()
    page.get_by_role("link", name="Manager Assignment Queue").click()
    page.get_by_role("button", name="Settings").click()
    page.get_by_role("button", name="Logout").click()'''
