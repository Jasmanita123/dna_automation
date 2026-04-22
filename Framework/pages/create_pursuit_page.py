
from Framework.locators.add_client_locators import AddClientLocators
from Framework.locators.create_locators import CreatePursuitLocators
from playwright.sync_api import expect

from Framework.locators.dashboard_locators import DashboardLocators


class CreatePursuitPage:
    def __init__(self, page):
        self.page = page

    def click_create_pursuit(self):
        create_pursuit = self.page.locator(DashboardLocators.CREATE_PURSUIT_OPTION).first
        expect(create_pursuit).to_be_visible(timeout=10000)
        create_pursuit.click()

#Add a new client using the + icon available

    def get_modal(self):
        modal = self.page.locator(".ant-modal-content").last
        expect(modal).to_be_visible(timeout=10000)
        return modal

    def select_dropdown_option(self, label, value):
        modal = self.get_modal()

        field = modal.locator(
            f"xpath=.//*[normalize-space(text())='{label}']/ancestor::div[contains(@class,'ant-form-item')][1]"
        ).first
        expect(field).to_be_visible(timeout=10000)

        selector = field.locator(".ant-select-selector").first
        selector.scroll_into_view_if_needed()
        selector.click(force=True)

        dropdown = self.page.locator(
            ".ant-select-dropdown:not(.ant-select-dropdown-hidden)"
        ).last
        expect(dropdown).to_be_visible(timeout=10000)

        option = dropdown.locator(f".ant-select-item-option[title='{value}']").first
        expect(option).to_be_visible(timeout=10000)
        option.click(force=True)

    def add_new_client(self, client_name, industry, sector):
        modal = self.get_modal()

        modal.locator("input").first.fill(client_name)

        self.select_dropdown_option("Industry", industry)
        self.select_dropdown_option("Sector", sector)

        modal.locator("button:has-text('Save')").first.click()
        expect(modal).to_be_hidden(timeout=15000)

    def fill_pursuit_details(
        self,
        pursuit_name,
        client_name,
        proposal_type,
        project_type,
        country,
        billing_arrangement,
        start_date,
        end_date,
        jupiter_id,
    ):
        self._select_dropdown(CreatePursuitLocators.CLIENT_DROPDOWN, client_name)
        self._fill_input(CreatePursuitLocators.PURSUIT_NAME, pursuit_name)
        self._select_dropdown(CreatePursuitLocators.PROPOSAL_TYPE_DROPDOWN, proposal_type)
        self._select_dropdown(CreatePursuitLocators.PROJECT_TYPE_DROPDOWN, project_type)
        self._select_dropdown(CreatePursuitLocators.COUNTRY_DROPDOWN, country)
        self._select_dropdown(CreatePursuitLocators.BILLING_ARRANGEMENT_DROPDOWN, billing_arrangement)
        self._select_date_range(CreatePursuitLocators.PROJECT_DURATION, start_date, end_date)
        self._fill_input(CreatePursuitLocators.JUPITER_ID, jupiter_id)

    def submit_pursuit(self):
        self.page.locator(CreatePursuitLocators.SUBMIT_BUTTON).click()
        
    def click_create_without_data(self):
        self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first.click()

    def validate_required_errors(self, error_messages):
        for error in error_messages:
            expect(self.page.get_by_text(error, exact=False)).to_be_visible(timeout=10000)

    def validate_footer_buttons(self):
        expect(self.page.locator(CreatePursuitLocators.CANCEL_BUTTON).first).to_be_visible(timeout=10000)
        expect(self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first).to_be_visible(timeout=10000)

    def click_add_client_icon(self):
        add_icon = self.page.get_by_role("button", name=CreatePursuitLocators.ADD_CLIENT_BUTTON_TEXT)
        expect(add_icon).to_be_visible(timeout=10000)
        add_icon.click()

   

    

    def click_create(self):
        self.page.locator(CreatePursuitLocators.CREATE_BUTTON).first.click()

    def validate_success_message(self):
        expect(self.page.locator(CreatePursuitLocators.SUCCESS_MESSAGE).first).to_be_visible(timeout=10000)