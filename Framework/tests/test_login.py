from Framework.pages.login_page import LoginPage
from Framework.utils.config import PASSWORD, USERNAME


def test_login(page):
    login = LoginPage(page)

    login.navigate()
    login.click_sso()
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/pursuits**", timeout=60000)
    assert "/pursuits" in page.url
