from playwright.sync_api import Page, expect
import pytest
import allure
from pingid_automation import automate_pingid_mfa
from config import SSO_CREDENTIALS

@pytest.mark.smoke
@allure.feature('Authentication')
@allure.story('SCD Dashboard Login')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Verify successful login to SCD Dashboard application')
@allure.description('Test validates the complete login flow for SCD Dashboard including SSO authentication and location selection')
@allure.tag('smoke', 'authentication', 'scd')
def test_scd_dashboard_login(page: Page):
    """Test SCD Dashboard login functionality with SSO and MFA"""

    with allure.step("Navigate to SCD Dashboard QAT URL"):
        page.goto("https://qat-scdashboard.sureprep.com/")
        allure.attach(page.url, name="Initial URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Click Continue button"):
        page.get_by_role("link", name="CONTINUE").click()

    with allure.step("Enter email for SSO authentication"):
        page.get_by_role("textbox", name="Email").fill(SSO_CREDENTIALS["email"])
        allure.attach(SSO_CREDENTIALS["email"],
                     name="Email Entered",
                     attachment_type=allure.attachment_type.TEXT)

    with allure.step("Submit email and proceed to credentials page"):
        page.get_by_role("button", name="Sign in").click()

    with allure.step("Enter employee ID"):
        page.get_by_role("textbox", name="ex. 6036943, C603694, X696046").fill(SSO_CREDENTIALS["employee_id"])
        allure.attach(SSO_CREDENTIALS["employee_id"], name="Employee ID", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Enter password"):
        page.locator("#password").fill(SSO_CREDENTIALS["password"])

    with allure.step("Check 'Remember my username' option"):
        page.locator("label div").filter(has_text="Remember my username").locator("div").click()

    with allure.step("Click Sign On button"):
        page.wait_for_timeout(1000)  # Wait 1 second
        page.locator("#signOnButton").click(force=True)

    with allure.step("Handle PingID MFA authentication"):
        # Launch PingID.exe and get MFA code
        allure.attach("Launching PingID application",
                     name="PingID Status",
                     attachment_type=allure.attachment_type.TEXT)

        mfa_code = automate_pingid_mfa()

        if mfa_code:
            allure.attach(f"Retrieved MFA code: {mfa_code}",
                         name="MFA Code Retrieved",
                         attachment_type=allure.attachment_type.TEXT)

            # Wait for passcode input to be visible
            page.locator(".passcode-input").wait_for(state="visible", timeout=30000)

            # Paste the MFA code in the browser
            page.locator(".passcode-input").fill(mfa_code)
            allure.attach("MFA code entered in browser",
                         name="Browser Input",
                         attachment_type=allure.attachment_type.TEXT)

            # Click Sign On button
            page.locator("body").click()
            page.locator("input[value='Sign On']").click()
            #page.locator("#signOn").click(force=True)
            allure.attach("Clicked Sign On button after MFA",
                         name="Sign On Action",
                         attachment_type=allure.attachment_type.TEXT)
            
        else:
            raise Exception("Failed to retrieve MFA code from PingID")

    with allure.step("Select location: Test"):
        page.locator(".k-select").click()
        page.get_by_role("option", name="Test").click()
        allure.attach("Test", name="Selected Location", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Submit location selection"):
        page.locator(".mdl-button__ripple-container").click()
        page.wait_for_timeout(5000)

    with allure.step("Navigate to dashboard home"):
        page.goto("https://qat-scdashboard.sureprep.com/dashboard/home")
        allure.attach(page.url, name="Dashboard URL", attachment_type=allure.attachment_type.TEXT)

    with allure.step("Toggle navigation menu"):
        page.get_by_role("button", name="Toggle navigation").click()

    with allure.step("Navigate to Test Verification"):
        page.get_by_role("link", name="Test Verification").click()

    with allure.step("Navigate to Manager Assignment Queue"):
        page.get_by_role("link", name="Manager Assignment Queue").click()

    with allure.step("Open Settings menu"):
        page.get_by_role("button", name="Settings").click()

    with allure.step("Logout from application"):
        page.get_by_role("button", name="Logout").click()

        # Take final screenshot
        screenshot = page.screenshot()
        allure.attach(screenshot,
                     name="After Logout",
                     attachment_type=allure.attachment_type.PNG)