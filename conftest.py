from selenium import webdriver
import allure
import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
import os

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Browser: chrome or firefox or edge")
    parser.addoption("--incognito", action="store_true", help="Run browser in incognito/private mode")


@pytest.fixture
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name").lower()
    incognito = request.config.getoption("--incognito")

    if browser_name == "chrome":
        options = ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(service=ChromeService(), options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        if incognito:
            options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(service=FirefoxService(), options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        if incognito:
            options.add_argument("--inprivate")
        driver = webdriver.Edge(service=EdgeService(), options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            driver = getattr(item, "driver", None)
            if driver:
                reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
                os.makedirs(reports_dir, exist_ok=True)
                file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
                print("Saving screenshot to:", file_name)
                _capture_screenshot(driver, file_name)

                html = f'<div><img src="{file_name}" style="width:304px; height:228px;" ' \
                       f'onclick="window.open(this.src)" align="right"/></div>'
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(driver, file_name):
    driver.get_screenshot_as_file(file_name)