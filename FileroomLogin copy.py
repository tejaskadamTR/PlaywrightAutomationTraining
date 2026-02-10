from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_fileroomLogin(page : Page):
    page.goto("https://production.sureprep.com/")
    page.locator(".Cont-Btn").click()
    page.locator("#username").fill("tejas.kadam@thomsonreuters.com")
    page.locator("._button-login-id").click()
    page.locator("#username").fill("6124436")
    page.locator("#password").fill("NA")
    page.locator(".remember-username").check()
 
    page.locator("#signOnButton").click()
    #expect(page.locator(".ping-error")).to_have_text("We didn't recognize the username or password you entered. Please try again.")
    #expect(page.get_by_text("We didn't recognize the username or password you entered")).to_be_visible
    
    page.select_option("#SelectedDomainID", value="Automation-01")
    page.locator("#btnSubmit").click()
    
    expect(page).to_have_url("https://production.sureprep.com/Fileroom/Fileroom/Listing")
