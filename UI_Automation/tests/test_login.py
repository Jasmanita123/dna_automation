from UI_Automation.pages.login_page import LoginPage
from UI_Automation.utils.config import PASSWORD, USERNAME
from UI_Automation.utils.logger import get_logger

logger = get_logger(__name__)


def test_login(page):
    try:
        logger.info("Test started: Login validation")

        login = LoginPage(page)

        logger.info("Launching DNA Pursuit application")
        #Launch the URL for DNA Pursuit application
        login.navigate()

        #Click on Login using SSO option
        logger.info("Clicking Login using SSO")
        login.click_sso()

        #Provide the username and password and select sign in
        logger.info("Performing login with username and password")
        login.login(USERNAME, PASSWORD)

        #Validate if the user has logged in successfully
        logger.info("Validating successful login")
        login.is_logged_in()

        logger.info("Waiting for pursuits page URL")
        page.wait_for_url("**/pursuits**", timeout=60000)
        assert "/pursuits" in page.url

        logger.info("Test passed: User logged in successfully and landed on pursuits page")

    except Exception as e:
        logger.exception(f"Test failed: {e}")
        raise



