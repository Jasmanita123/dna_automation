
import os
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

from Framework.pages.login_page import LoginPage
from Framework.utils.config import USERNAME, PASSWORD

REPORT_DIR = "reports"
PASS_DIR = os.path.join(REPORT_DIR, "screenshots", "passed")
FAIL_DIR = os.path.join(REPORT_DIR, "screenshots", "failed")


def pytest_configure(config):
    os.makedirs(PASS_DIR, exist_ok=True)
    os.makedirs(FAIL_DIR, exist_ok=True)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        if hasattr(request.node, "rep_call"):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name.replace("/", "_").replace("\\", "_")

            if request.node.rep_call.passed:
                file_path = os.path.join(PASS_DIR, f"{test_name}_{timestamp}.png")
                page.screenshot(path=file_path, full_page=True)
                print(f"\nPass screenshot saved: {file_path}")

            elif request.node.rep_call.failed:
                file_path = os.path.join(FAIL_DIR, f"{test_name}_{timestamp}.png")
                page.screenshot(path=file_path, full_page=True)
                print(f"\nFail screenshot saved: {file_path}")

        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    login = LoginPage(page)
    login.navigate()
    login.click_sso()
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/pursuits**", timeout=60000)
    assert "/pursuits" in page.url

    #return page
    yield page

