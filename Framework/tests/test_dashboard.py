from Framework.pages.login_page import LoginPage
from Framework.pages.dashboard_page import DashboardPage
from Framework.utils.config import USERNAME, PASSWORD

EXPECTED_NAME = "hashedintestuser109LastN, hashedintestuser109FirstN"
EXPECTED_EMAIL = "hashedintestuser109@deloitte.com"


def test_dashboard(logged_in_page):
    #login_page = LoginPage(page)
    #login_page.navigate()
    #login_page.click_sso()
    #login_page.login(USERNAME, PASSWORD)

    #login_page.page.wait_for_timeout(30000)

    dashboard_page = DashboardPage(logged_in_page)

    dashboard_page.validate_categories()
    dashboard_page.print_category_counts()
    dashboard_page.validate_list_of_pursuits_option()
    dashboard_page.validate_profile_details(EXPECTED_NAME, EXPECTED_EMAIL)
    dashboard_page.click_applications()
    dashboard_page.click_notifications()
    dashboard_page.open_left_pane()
    dashboard_page.validate_left_pane_options()