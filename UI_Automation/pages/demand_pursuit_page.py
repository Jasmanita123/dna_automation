from UI_Automation.locators.demand_pursuit_locators import DemandPursuitLocators as L


class DemandPursuitPage:
    def __init__(self, page, logger):
        self.page = page
        self.logger = logger

    def navigate_to_demand_pursuit_page(self):
        self.logger.info("Navigating to Demand Pursuit page")
        self.page.locator(L.DEMAND_PURSUIT_MENU).click()
        #self.page.wait_for_load_state("networkidle")

    def open_all_category(self):
        self.logger.info("Opening All category")
        self.page.locator(L.ALL_CATEGORY_TAB).click()
        self.page.wait_for_timeout(1000)

    def search_pursuit(self, value):
        self.logger.info("Clicking search icon")
        self.page.locator(L.SEARCH_ICON).click()

        self.logger.info("Waiting for search input")
        search_input = self.page.locator(L.SEARCH_INPUT).last
        search_input.wait_for(state="visible", timeout=10000)

        self.logger.info(f"Filling search with value: {value}")
        search_input.fill(value)
        #search_input.press("Enter")

        self.logger.info("Waiting for search results to load")
        self.page.wait_for_timeout(2000)
        #self.page.locator(L.CLIENT_NAME_CELL).click()

    def validate_pursuit_details(self, expected_name):
        #assert self.page.locator(L.PURSUIT_NAME).text_content().strip() == expected_name
        assert self.page.locator(L.CLIENT_NAME_CELL).text_content().strip() == expected_name
        self.page.wait_for_timeout(2000)
        self.page.locator(L.CLIENT_NAME_CELL).click()
        self.page.wait_for_timeout(2000)
        self.page.wait_for_load_state("networkidle")
        
    def validate_pursuit_details_page(self, expected_name):
        self.logger.info("Validating pursuit details page")
        actual_title = self.page.locator(L.PURSUIT_TITLE).inner_text().strip()
        assert expected_name in actual_title, (
            f"Expected pursuit title to contain '{expected_name}', got '{actual_title}'"
        )

    