import pytest
from selenium import webdriver

# Import browser-specific options classes
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

# Import WebDriverWait for explicit waits
from selenium.webdriver.support.ui import WebDriverWait

# Import webdriver-manager classes for automatic driver management
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Import service classes to specify driver executables and manage service lifecycle
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser to run tests on: chrome, firefox, safari")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope='function')
def setup(request):
    browser = request.config.getoption("--browser").lower()
    headless = request.config.getoption("--headless")

    driver = None

    # Setup Browser options and enable headless if requested

    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")  # modern headless
            options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)

    elif browser == "edge":
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)

    elif browser == "safari":
        if headless:
            raise ValueError("Safari does NOT support headless mode")
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    yield driver, wait
    driver.quit()



