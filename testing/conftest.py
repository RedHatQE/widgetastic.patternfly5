import os
import subprocess
from urllib.parse import urljoin
from urllib.request import urlopen

import pytest
from selenium import webdriver
from wait_for import wait_for
from widgetastic.browser import Browser

OPTIONS = {"firefox": webdriver.FirefoxOptions(), "chrome": webdriver.ChromeOptions()}
TESTING_PAGES = {
    "v6": "https://www.patternfly.org",
    "v5": "https://v5-archive.patternfly.org",
}


def pytest_addoption(parser):
    parser.addoption(
        "--browser-name",
        help="name of the browser",
        choices=("firefox", "chrome"),
        default="firefox",
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
    return os.environ.get("BROWSER") or pytestconfig.getoption("--browser-name")


@pytest.fixture(scope="session")
def pf_version(pytestconfig):
    return os.environ.get("PF-VERSION") or pytestconfig.getoption("--pf-version")


@pytest.fixture(scope="session")
def selenium_url(pytestconfig, browser_name, worker_id):
    forced_host = pytestconfig.getoption("--force-host")
    if forced_host is None:
        oktet = 1 if worker_id == "master" else int(worker_id.lstrip("gw")) + 1
        host = f"127.0.0.{oktet}"
        ps = subprocess.run(
            [
                "podman",
                "run",
                "--rm",
                "-d",
                "-p",
                f"{host}:4444:4444",
                "-p",
                f"{host}:7900:7900",
                "-e",
                "SE_VNC_NO_PASSWORD=1",
                "-e",
                "SE_SCREEN_HEIGHT=1080",
                "-e",
                "SE_SCREEN_WIDTH=1920",
                "--shm-size=2g",
                f"docker.io/selenium/standalone-{browser_name}:latest",
            ],
            stdout=subprocess.PIPE,
            check=False,
        )
        print(f"VNC url: http://{host}:7900")

        yield f"http://{host}:4444"
        container_id = ps.stdout.decode("utf-8").strip()
        subprocess.run(["podman", "kill", container_id], stdout=subprocess.DEVNULL, check=False)
    else:
        print(f"VNC url: http://{forced_host}:7900")
        yield f"http://{forced_host}:4444"


@pytest.fixture(scope="session")
def wait_for_selenium(selenium_url):
    wait_for(lambda: urlopen(selenium_url), timeout=180, handle_exception=True)


@pytest.fixture(scope="session")
def selenium(browser_name, wait_for_selenium, selenium_url):
    driver = webdriver.Remote(command_executor=selenium_url, options=OPTIONS[browser_name.lower()])
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def browser(selenium, pf_version, request):
    testing_page_url = urljoin(TESTING_PAGES.get(pf_version), request.module.TESTING_PAGE_COMPONENT)
    selenium.get(testing_page_url)
    print(f"Testing page: {testing_page_url}")
    browser = Browser(selenium)
    if browser.elements(".//button[@aria-label='Close banner']"):
        browser.click(".//button[@aria-label='Close banner']")
    yield browser
    selenium.refresh()
