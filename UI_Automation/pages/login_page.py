from playwright.sync_api import Page, expect
from UI_Automation.locators.login_locators import LoginLocators
from UI_Automation.pages.dashboard_page import DashboardPage
from UI_Automation.utils.config import Base_URL
from UI_Automation.utils.logger import get_logger


logger = get_logger(__name__)


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    #Launch the URL for DNA Pursuit application
    def navigate(self):
        logger.info(f"Navigating to URL: {Base_URL}")
        self.page.goto(Base_URL)
        self.page.bring_to_front();
        logger.info("Navigation completed successfully")

    #Click on Login using SSO option
    def click_sso(self):
        logger.info("Clicking on 'Login using SSO'")
        self.page.get_by_text("Login using SSO").click()
        logger.info("'Login using SSO' clicked successfully")

    #Provide the username and password and select sign in
    def login(self, username, password):
        try:
            logger.info("Login started")

            logger.info(f"Entering username: {username}")
            self.page.locator(LoginLocators.Username).nth(1).fill(username)

            logger.info("Entering password")
            self.page.locator(LoginLocators.Password).nth(1).fill(password)

            logger.info("Clicking Sign In button")
            self.page.locator(LoginLocators.Sigin_Btn).nth(1).click()

            self.page.bring_to_front()
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(2000)

            logger.info("Checking for close popup")
            close_button = self.page.locator('[aria-label="Close"]')
            if close_button.is_visible():
                close_button.click()
                logger.info("Popup closed successfully")
            else:
                logger.info("No popup displayed after login")

            logger.info("Login completed successfully")

        except Exception as e:
            logger.exception(f"Login failed due to: {e}")
            raise
        
    #Validate if the user has logged in successfully
    def is_logged_in(self):
        try:
            logger.info("Validating whether user is logged in")
            expect(self.page.locator(LoginLocators.Dasboard_Name)).to_be_visible()
            logger.info("Login validation successful, dashboard is visible")
            return DashboardPage(self.page)

        except Exception as e:
            logger.exception(f"Login validation failed: {e}")
            raise