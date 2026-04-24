from UI_Automation.pages.login_page import LoginPage
from UI_Automation.pages.dashboard_page import DashboardPage
from UI_Automation.utils import test_data
from UI_Automation.utils.config import USERNAME, PASSWORD
from UI_Automation.utils.logger import get_logger

EXPECTED_NAME = test_data.EXPECTED_NAME
EXPECTED_EMAIL = test_data.EXPECTED_EMAIL

logger = get_logger(__name__)

def test_dashboard(logged_in_page):
    try:
        logger.info("Test started: Dashboard validation")

        dashboard_page = DashboardPage(logged_in_page)

        #Validate if there are 6 categories available (All, New, In-progress, Cancelled, Won,Deferred)
        logger.info("Validating dashboard categories")
        dashboard_page.validate_categories()

        #Validate if the card count is displayed and print them to the terminal along with the category
        logger.info("Logging category counts")
        dashboard_page.print_category_counts()

        #Validate if the List of pursuits option is displayed in the demand pursuits dashboard
        logger.info("Validating List of Pursuits option")
        dashboard_page.validate_list_of_pursuits_option()

        #Validate the username and email displayed in the profile section is correct
        logger.info("Validating profile details")
        dashboard_page.validate_profile_details(EXPECTED_NAME, EXPECTED_EMAIL)

        #Validate if the applications option is available and click on it
        logger.info("Clicking Applications icon")
        dashboard_page.click_applications()

        #Validate if the notification option is available and click on it
        logger.info("Clicking Notifications icon")
        dashboard_page.click_notifications()

        #Click on the left side pane and validate the 3 options available (Collapse, Demand Pursuits, Create Pursuit)
        logger.info("Opening left pane")
        dashboard_page.open_left_pane()
        logger.info("Validating left pane options")
        dashboard_page.validate_left_pane_options()

        logger.info("Test passed: Dashboard validation completed successfully")

    except Exception as e:
        logger.exception(f"Test failed: Dashboard validation failed due to: {e}")
        raise