import os
from collections.abc import Iterator
from urllib.parse import urljoin

import pytest
from playwright.sync_api import Browser as PlaywrightBrowser
from playwright.sync_api import BrowserContext, Page, sync_playwright
from widgetastic.browser import Browser

TESTING_PAGES = {
    "v6": "https://www.patternfly.org",
    "v5": "https://v5-archive.patternfly.org",
}


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chromium",
        choices=["chromium", "firefox"],
        help="Browser to run tests with: chromium, firefox (default: chromium)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode (no browser window) default its run in headed mode.",
    )
    parser.addoption(
        "--slowmo",
        action="store",
        type=int,
        default=0,
        help="Slow down Playwright operations by specified milliseconds (default: 0, no slowdown)",
    )
    parser.addoption(
        "--pf-version",
        help="Patternfly Version",
        choices=("v6", "v5"),
        default="v6",
    )
    parser.addoption("--force-host", default=None, help="force a selenium hostname")


@pytest.fixture(scope="session")
def browser_name(pytestconfig):
    return os.environ.get("BROWSER") or pytestconfig.getoption("--browser")


@pytest.fixture(scope="session")
def pf_version(pytestconfig) -> str:
    return os.environ.get("PF-VERSION") or pytestconfig.getoption("--pf-version")


def pytest_report_header(config):
    """Add browser configuration info to pytest report header."""
    browser_name = os.environ.get("BROWSER") or config.getoption("--browser")
    pf_version = os.environ.get("PF-VERSION") or config.getoption("--pf-version")
    headless_mode = config.getoption("--headless")
    slowmo_delay = config.getoption("--slowmo")

    mode = "headless" if headless_mode else "headed"
    slowmo_info = f" with {slowmo_delay}ms slowmo" if slowmo_delay > 0 else ""

    return [
        f"Browser: {browser_name} ({mode} mode){slowmo_info}",
        f"PatternFly Version: {pf_version}",
        f"Testing Page: {TESTING_PAGES.get(pf_version)}",
    ]


@pytest.fixture(scope="session")
def playwright_browser_instance(request, browser_name: str) -> PlaywrightBrowser:
    """Launches a Playwright browser instance."""
    with sync_playwright() as p:
        # Select browser based on command line argument (default to chromium)
        headless_mode = request.config.getoption("--headless")
        slowmo_delay = request.config.getoption("--slowmo")

        if browser_name == "firefox":
            py_browser = p.firefox.launch(headless=headless_mode, slow_mo=slowmo_delay)
        else:
            py_browser = p.chromium.launch(headless=headless_mode, slow_mo=slowmo_delay)

        yield py_browser
        py_browser.close()


@pytest.fixture(scope="session")
def browser_context(playwright_browser_instance: PlaywrightBrowser) -> BrowserContext:
    """Creates a browser context for the entire test session."""
    context = playwright_browser_instance.new_context(viewport={"width": 1920, "height": 1080})
    yield context
    context.close()


@pytest.fixture(scope="session")
def page(browser_context: BrowserContext) -> Iterator[Page]:
    """Creates the initial page within the session context."""
    page = browser_context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="module")
def browser(page: Page, pf_version: str, request):
    testing_page_url = urljoin(TESTING_PAGES.get(pf_version), request.module.TESTING_PAGE_COMPONENT)
    page.goto(testing_page_url)
    print(f"Testing page: {testing_page_url}")
    browser = Browser(page)
    if browser.elements(".//button[@aria-label='Close banner']"):
        browser.click(".//button[@aria-label='Close banner']")
    yield browser
    browser.refresh()


# Registering custom markers
def pytest_configure(config):
    config.addinivalue_line("markers", "skip_if_pf5: Skip test for PF5.")
    config.addinivalue_line("markers", "skip_if_pf6: Skip test for PF6.")


# Hook to modify the test collection and apply the skipping logic based on user-selected PF version
def pytest_collection_modifyitems(config, items):
    pf_version = config.getoption("--pf-version")
    for item in items:
        # Check if the test has the 'skip_if_pf5' marker
        if "skip_if_pf5" in item.keywords and pf_version == "v5":
            item.add_marker(pytest.mark.skip(reason="Skipping test for PF5"))

        # Optionally, you can add the logic to skip tests for PF6 if needed:
        elif "skip_if_pf6" in item.keywords and pf_version == "v6":
            item.add_marker(pytest.mark.skip(reason="Skipping test for PF6"))
