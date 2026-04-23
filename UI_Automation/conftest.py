
import logging
import re
import shutil
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from UI_Automation.utils.config import USERNAME, PASSWORD

LATEST_DIR = Path("artifacts/latest")
SCREENSHOTS_DIR = LATEST_DIR / "screenshots"
PASS_DIR = SCREENSHOTS_DIR / "passed"
FAIL_DIR = SCREENSHOTS_DIR / "failed"
LOGS_DIR = LATEST_DIR / "logs"


def _safe_name(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", name)


def _close_all_loggers():
    root = logging.getLogger()
    for handler in root.handlers[:]:
        handler.close()
        root.removeHandler(handler)

    for logger_obj in list(logging.Logger.manager.loggerDict.values()):
        if isinstance(logger_obj, logging.Logger):
            for handler in logger_obj.handlers[:]:
                handler.close()
                logger_obj.removeHandler(handler)


def pytest_configure(config):
    _close_all_loggers()

    if LATEST_DIR.exists():
        shutil.rmtree(LATEST_DIR)

    PASS_DIR.mkdir(parents=True, exist_ok=True)
    FAIL_DIR.mkdir(parents=True, exist_ok=True)
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    if config.pluginmanager.hasplugin("html"):
        config.option.htmlpath = str(LATEST_DIR / "report.html")
        config.option.self_contained_html = True


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
            test_name = _safe_name(request.node.nodeid)

            if request.node.rep_call.passed:
                file_path = PASS_DIR / f"{test_name}.png"
                page.screenshot(path=str(file_path), full_page=True)
                print(f"\nPass screenshot saved: {file_path}")

            elif request.node.rep_call.failed:
                file_path = FAIL_DIR / f"{test_name}.png"
                page.screenshot(path=str(file_path), full_page=True)
                print(f"\nFail screenshot saved: {file_path}")

        context.close()
        browser.close()


@pytest.fixture(scope="function")
def logged_in_page(page):
    from UI_Automation.pages.login_page import LoginPage

    login = LoginPage(page)
    login.navigate()
    login.click_sso()
    login.login(USERNAME, PASSWORD)

    page.wait_for_url("**/pursuits**", timeout=60000)
    assert "/pursuits" in page.url

    yield page