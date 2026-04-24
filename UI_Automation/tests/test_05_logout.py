from UI_Automation.pages.logout_page import LogoutPage


def test_logout(logged_in_page):
    logout_page = LogoutPage(logged_in_page)
    logout_page.logout()
    logout_page.validate_logged_out()