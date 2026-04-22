from playwright.sync_api import Page, expect
from Framework.locators.login_locators import LoginLocators
from Framework.pages.dashboard_page import DashboardPage
from Framework.utils.config import Base_URL

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        self.page.goto(Base_URL)
        self.page.bring_to_front();

    def click_sso(self):
        self.page.get_by_text("Login using SSO").click()

    def login(self,username,password):
        self.page.locator(LoginLocators.Username).nth(1).fill(username)
        self.page.locator(LoginLocators.Password).nth(1).fill(password)
        self.page.locator(LoginLocators.Sigin_Btn).nth(1).click()

        self.page.bring_to_front()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        self.page.locator('[aria-label="Close"]').click()

    def is_logged_in(self):
        self.page.locator('[class="sc-fqkvVO jxIJWU"]')

        return DashboardPage(self.page)  #connection with dashboard