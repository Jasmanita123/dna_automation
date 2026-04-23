from playwright.sync_api import expect
from datetime import datetime

from UI_Automation.locators.add_client_locators import AddClientLocators
from UI_Automation.locators.create_locators import CreatePursuitLocators
from UI_Automation.locators.dashboard_locators import DashboardLocators
from UI_Automation.utils.logger import get_logger


logger = get_logger(__name__)


class CreatePursuitPage:
    def __init__(self, page):
        self.page = page

    # Create a pursuit by clicking on the create pursuit option available in the side pane
    def click_create_pursuit(self):
        try:
            logger.info("Clicking Create Pursuit option")
            create_pursuit = self.page.locator(DashboardLocators.CREATE_PURSUIT_OPTION).first
            expect(create_pursuit).to_be_visible(timeout=10000)
            create_pursuit.click()
            logger.info("Create Pursuit option clicked successfully")
        except Exception as e:
            logger.exception(f"Failed to click Create Pursuit option: {e}")
            raise

    # Click on the create button without providing any details and validate
    def click_create_without_data(self):
        logger.info("Clicking Create button without entering data")
        self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first.click()

    # if the error messages are displayed for all the required fields that are not provided.
    def validate_required_errors(self, error_messages):
        try:
            logger.info("Validating required field error messages")
            for error in error_messages:
                logger.info(f"Checking error message: {error}")
                expect(self.page.get_by_text(error, exact=False)).to_be_visible(timeout=10000)

            logger.info("All required field errors are visible")

            demand_pursuit = self.page.locator(DashboardLocators.DEMAND_PURSUITS_OPTION).first
            expect(demand_pursuit).to_be_visible(timeout=10000)
            demand_pursuit.click()
            self.page.wait_for_timeout(2000)
            logger.info("Navigated back to Demand Pursuits")
        except Exception as e:
            logger.exception(f"Required error validation failed: {e}")
            raise

    # Validate if 2 buttons are displayed at the bottom (Cancel and Create)
    def validate_footer_buttons(self):
        logger.info("Validating footer buttons")
        expect(self.page.locator(CreatePursuitLocators.CANCEL_BUTTON).first).to_be_visible(timeout=10000)
        expect(self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first).to_be_visible(timeout=10000)
        logger.info("Footer buttons are visible")

    # Add a new client using the + icon available
    def click_add_client_icon(self):
        try:
            logger.info("Clicking Add Client icon")
            add_icon = self.page.get_by_role("button", name=CreatePursuitLocators.ADD_CLIENT_BUTTON_TEXT)
            expect(add_icon).to_be_visible(timeout=10000)
            add_icon.click()
            logger.info("Add Client icon clicked successfully")
        except Exception as e:
            logger.exception(f"Failed to click Add Client icon: {e}")
            raise

    def get_modal(self):
        logger.info("Getting modal dialog")
        modal = self.page.locator(".ant-modal-content").last
        expect(modal).to_be_visible(timeout=10000)
        return modal

    def _select_visible_option(self, value):
        logger.info(f"Selecting visible option: {value}")
        dropdown = self.page.locator(CreatePursuitLocators.VISIBLE_DROPDOWN).last
        expect(dropdown).to_be_visible(timeout=10000)

        option = dropdown.locator(
            f"{CreatePursuitLocators.OPTION_BY_TITLE.format(value=value)}, "
            f"{CreatePursuitLocators.OPTION_BY_TEXT.format(value=value)}"
        ).first
        expect(option).to_be_attached(timeout=10000)

        try:
            option.scroll_into_view_if_needed()
            expect(option).to_be_visible(timeout=10000)
            option.click(timeout=5000)
        except Exception:
            logger.info(f"Normal click failed for option '{value}', using JS fallback")
            option.evaluate("el => el.scrollIntoView({block: 'center', inline: 'nearest'})")
            option.evaluate("el => el.click()")

    def select_dropdown_option(self, label, value):
        logger.info(f"Selecting dropdown option for {label}: {value}")
        modal = self.get_modal()

        field = modal.locator(
            AddClientLocators.FORM_ITEM_BY_LABEL.format(label=label)
        ).first
        expect(field).to_be_visible(timeout=10000)

        selector = field.locator(AddClientLocators.SELECTOR_IN_FORM_ITEM).first
        selector.scroll_into_view_if_needed()
        selector.click(force=True)

        self._select_visible_option(value)

    def add_new_client(self, client_name, industry, sector):
        try:
            logger.info(f"Adding new client: {client_name}")
            modal = self.get_modal()

            modal.locator(AddClientLocators.FIRST_INPUT).first.fill(client_name)
            self.select_dropdown_option("Industry", industry)
            self.select_dropdown_option("Sector", sector)

            modal.locator(AddClientLocators.SAVE_BUTTON).first.click()
            expect(modal).to_be_hidden(timeout=15000)
            logger.info("New client added successfully")
        except Exception as e:
            logger.exception(f"Failed to add new client '{client_name}': {e}")
            raise

    # For dropdown
    def _select_dropdown(self, label, value):
        logger.info(f"Selecting dropdown {label}: {value}")
        field_drop = self.page.locator(
            AddClientLocators.FORM_ITEM_BY_LABEL.format(label=label)
        ).first
        expect(field_drop).to_be_visible(timeout=10000)

        selector = field_drop.locator(AddClientLocators.SELECTOR_IN_FORM_ITEM).first
        selector.scroll_into_view_if_needed()
        selector.click(force=True)

        self._select_visible_option(value)

    def _fill_input(self, locator, value):
        logger.info(f"Filling input field: {locator}")
        element = self.page.locator(locator).first
        expect(element).to_be_visible(timeout=10000)
        element.fill(str(value))

    def _select_date_range(self, field_locator, start_date, end_date):
        logger.info(f"Selecting date range from {start_date} to {end_date}")
        start_iso = datetime.strptime(start_date, "%d/%m/%Y").strftime("%Y-%m-%d")
        end_iso = datetime.strptime(end_date, "%d/%m/%Y").strftime("%Y-%m-%d")

        field = self.page.locator(field_locator).first
        expect(field).to_be_visible(timeout=15000)
        field.click()

        self.page.locator(CreatePursuitLocators.PROJECT_DURATION).click()
        popup = self.page.locator(CreatePursuitLocators.DATE_PICKER_POPUP).last
        expect(popup).to_be_visible(timeout=10000)

        start_cell = popup.locator(CreatePursuitLocators.date_cell(start_iso)).first
        end_cell = popup.locator(CreatePursuitLocators.date_cell(end_iso)).first

        expect(start_cell).to_be_visible(timeout=10000)
        start_cell.click()

        expect(end_cell).to_be_visible(timeout=10000)
        end_cell.click()

        done_button = self.page.locator(CreatePursuitLocators.DATE_DONE_BUTTON).last
        expect(done_button).to_be_visible(timeout=10000)
        done_button.click()

    def fill_pursuit_details(
        self,
        pursuit_name,
        proposal_type,
        project_type,
        country,
        billing_arrangement,
        start_date,
        end_date,
        jupiter_id,
    ):
        try:
            logger.info(f"Filling pursuit details for: {pursuit_name}")
            self._fill_input(CreatePursuitLocators.PURSUIT_NAME, pursuit_name)
            self._select_dropdown("Proposal Type", proposal_type)
            self._select_dropdown("Type of Project", project_type)
            self._select_dropdown("Country", country)
            self._select_dropdown("Billing Arrangement", billing_arrangement)
            self._select_date_range(CreatePursuitLocators.PROJECT_DURATION, start_date, end_date)
            self._fill_input(CreatePursuitLocators.JUPITER_ID, jupiter_id)
            logger.info("Pursuit details filled successfully")
        except Exception as e:
            logger.exception(f"Failed to fill pursuit details for '{pursuit_name}': {e}")
            raise

    def click_create(self):
        try:
            logger.info("Clicking Create button")
            self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first.click()
            self.page.wait_for_timeout(2000)
            logger.info("Create button clicked successfully")
        except Exception as e:
            logger.exception(f"Failed to click Create button: {e}")
            raise

    # Validate the message displayed after creating a pursuit successfully
    def validate_success_message(self):
        try:
            logger.info("Validating success message after pursuit creation")
            expect(self.page.locator(CreatePursuitLocators.SUCCESS_MESSAGE).first).to_be_visible(timeout=10000)
            logger.info("Success message is visible")
        except Exception as e:
            logger.exception(f"Success message validation failed: {e}")
            raise
