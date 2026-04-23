
from playwright.sync_api import expect
from UI_Automation.locators.dashboard_locators import DashboardLocators
from UI_Automation.utils.logger import get_logger

logger = get_logger(__name__)
class DashboardPage:
    def __init__(self, page):
        self.page = page


    #Get the Categories if there are 6 categories available (All, New, In-progress, Cancelled, Won,Deferred)
    def get_categories(self):
        try:
            logger.info("Getting dashboard categories")
            items = self.page.locator(DashboardLocators.CATEGORY_ITEMS)
            expect(items.first).to_be_visible(timeout=10000)
            texts = items.all_text_contents()
            categories = [text.strip() for text in texts if text.strip()]
            logger.info(f"Categories found: {categories}")
            return categories
        except Exception as e:
            logger.exception(f"Failed to get categories: {e}")
            raise

    #Validate if there are 6 categories available (All, New, In-progress, Cancelled, Won,Deferred)
    def validate_categories(self):
        try:
            logger.info("Validating dashboard categories")
            actual = [x.lower() for x in self.get_categories()]
            expected = ["all", "new", "in progress", "cancelled", "won", "deferred"]

            assert len(actual) >= 6, f"Expected at least 6 categories, but found {len(actual)}: {actual}"

            for category in expected:
                assert any(category in item.lower() for item in actual), f"{category} not found in {actual}"

            logger.info("Dashboard categories validated successfully")
        except Exception as e:
            logger.exception(f"Category validation failed: {e}")
            raise
    
    #Validate if the card count is displayed and print them to the terminal along with the category
    def print_category_counts(self):
        try:
            logger.info("Printing category counts")
            categories = self.get_categories()
            for item in categories:
                logger.info(f"Category/Card Count -> {item}")
        except Exception as e:
            logger.exception(f"Failed while printing category counts: {e}")
            raise

    #Validate if the List of pursuits option is displayed in the demand pursuits dashboard
    def validate_list_of_pursuits_option(self):
        try:
            logger.info("Validating List of Pursuits option")
            expect(self.page.locator(DashboardLocators.PURSUIT_LIST_OPTION)).to_be_visible()
            logger.info("List of Pursuits option is visible")
        except Exception as e:
            logger.exception(f"List of Pursuits validation failed: {e}")
            raise

    #Validate the username and email displayed in the profile section is correct
    def validate_profile_details(self, expected_name, expected_email):
        try:
            logger.info("Validating profile details")
            profile_container = self.page.locator(DashboardLocators.PROFILE_CONTAINER).first
            profile_name = self.page.locator(DashboardLocators.PROFILE_NAME).first

            expect(profile_container).to_be_visible(timeout=10000)
            logger.info("Profile container is visible")

            expect(profile_name).to_contain_text(expected_name)
            logger.info(f"Profile name validated: {expected_name}")

            self.page.locator(DashboardLocators.PROFILE_TRIGGER).first.click()
            logger.info("Clicked profile trigger")

            expect(self.page.get_by_text(expected_email, exact=False).first).to_be_visible(timeout=10000)
            logger.info(f"Profile email validated: {expected_email}")
        except Exception as e:
            logger.exception(f"Profile validation failed: {e}")
            raise

    #Validate if the applications option is available and click on it
    def click_applications(self):
        try:
            logger.info("Clicking Applications icon")
            applications = self.page.locator(DashboardLocators.APPLICATIONS_ICON).first
            expect(applications).to_be_visible(timeout=10000)
            applications.click()
            logger.info("Applications icon clicked successfully")
        except Exception as e:
            logger.exception(f"Failed to click Applications icon: {e}")
            raise
    
    #Validate if the notification option is available and click on it
    def click_notifications(self):
        try:
            logger.info("Clicking Notifications icon")
            notifications = self.page.locator(DashboardLocators.NOTIFICATIONS_ICON)
            expect(notifications).to_be_visible(timeout=10000)
            notifications.click()
            logger.info("Notifications icon clicked successfully")
        except Exception as e:
            logger.exception(f"Failed to click Notifications icon: {e}")
            raise
    
    #Click on the left side pane and validate the 3 options available (Collapse, Demand Pursuits, Create Pursuit)
    def open_left_pane(self):
        try:
            logger.info("Opening left pane")
            pane = self.page.locator(DashboardLocators.LEFT_PANE)
            expect(pane).to_be_visible(timeout=10000)
            pane.click()
            logger.info("Left pane opened successfully")
        except Exception as e:
            logger.exception(f"Failed to open left pane: {e}")
            raise
    #For Validation of left pane option
    def validate_left_pane_options(self):
        try:
            logger.info("Validating left pane options")

            toggle_icon = self.page.locator(DashboardLocators.COLLAPSE_BUTTON).first
            expect(toggle_icon).to_be_visible(timeout=10000)
            logger.info("Collapse button is visible")

            expect(self.page.locator(DashboardLocators.DEMAND_PURSUITS_OPTION)).to_be_visible(timeout=10000)
            logger.info("Demand Pursuits option is visible")

            expect(self.page.locator(DashboardLocators.CREATE_PURSUIT_OPTION)).to_be_visible(timeout=10000)
            logger.info("Create Pursuit option is visible")

            logger.info("Left pane options validated successfully")
        except Exception as e:
            logger.exception(f"Left pane validation failed: {e}")
            raise