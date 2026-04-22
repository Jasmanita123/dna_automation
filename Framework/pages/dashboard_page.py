
from playwright.sync_api import expect
from Framework.locators.dashboard_locators import DashboardLocators


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def get_categories(self):
        items = self.page.locator(DashboardLocators.CATEGORY_ITEMS)
        expect(items.first).to_be_visible(timeout=10000)
        texts = items.all_text_contents()
        return [text.strip() for text in texts if text.strip()]

    def validate_categories(self):
        actual = [x.lower() for x in self.get_categories()]
        expected = ["all", "new", "in progress", "cancelled", "won", "deferred"]
        assert len(actual) >= 6, f"Expected at least 6 categories, but found {len(actual)}: {actual}"
        for category in expected:
            assert any(category in item.lower() for item in actual), f"{category} not found in {actual}"

    def print_category_counts(self):
        categories = self.get_categories()
        for item in categories:
            print(f"Category/Card Count -> {item}")

    def validate_list_of_pursuits_option(self):
        expect(self.page.locator(DashboardLocators.PURSUIT_LIST_OPTION)).to_be_visible()

    def validate_profile_details(self, expected_name, expected_email):
        profile_container = self.page.locator(DashboardLocators.PROFILE_CONTAINER).first
        profile_name = self.page.locator(DashboardLocators.PROFILE_NAME).first
        
        expect(profile_container).to_be_visible(timeout=10000)
        
        expect(profile_name).to_contain_text(expected_name)
        
        self.page.locator(DashboardLocators.PROFILE_TRIGGER).first.click()
        expect(self.page.get_by_text(expected_email, exact=False).first).to_be_visible(timeout=10000)

    def click_applications(self):
        applications = self.page.locator(DashboardLocators.APPLICATIONS_ICON).first
        expect(applications).to_be_visible(timeout=10000)
        applications.click()
    

    def click_notifications(self):
        notifications = self.page.locator(DashboardLocators.NOTIFICATIONS_ICON)
        expect(notifications).to_be_visible(timeout=10000)
        notifications.click()

    def open_left_pane(self):
        pane = self.page.locator(DashboardLocators.LEFT_PANE)
        expect(pane).to_be_visible(timeout=10000)
        pane.click()

    def validate_left_pane_options(self):
        

        toggle_icon = self.page.locator(DashboardLocators.COLLAPSE_BUTTON).first
        expect(toggle_icon).to_be_visible(timeout=10000)

        expect(self.page.locator(DashboardLocators.DEMAND_PURSUITS_OPTION)).to_be_visible(timeout=10000)
        expect(self.page.locator(DashboardLocators.CREATE_PURSUIT_OPTION)).to_be_visible(timeout=10000)