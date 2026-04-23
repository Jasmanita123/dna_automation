import re

from playwright.sync_api import Page, expect
from UI_Automation.locators.dashboard_locators import DashboardLocators
from UI_Automation.locators.login_locators import LoginLocators
from UI_Automation.locators.logout_locators import LogoutLocators


class LogoutPage:
    def __init__(self, page: Page):
        self.page = page

    def logout(self):
        profile_button = self.page.locator(DashboardLocators.PROFILE_TRIGGER).first
        expect(profile_button).to_be_visible(timeout=10000)
        profile_button.click()

        logout_option = self.page.locator(LogoutLocators.LOGOUT_OPTION).first
        expect(logout_option).to_be_visible(timeout=10000)
        logout_option.click()


    def validate_logged_out(self):
        self.page.wait_for_timeout(2000)
        self.page.reload()

        login_sso = self.page.locator(LoginLocators.LOGIN_SSO)
        

        expect(login_sso.first).to_be_visible(timeout=15000)