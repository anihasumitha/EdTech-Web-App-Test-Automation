from TestData.data import TestData
from PageObjects.LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC

class TestLoginFunctionality():

    def test_valid_url(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        assert TestData.expected_url == driver.current_url

    def test_valid_title(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        assert driver.title == TestData.expected_title

    def test_login_button_displayed_and_enabled(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page=LoginPage(driver,wait)
        assert login_page.is_login_button_visible(), "Login button is not visible"
        login_page.click_login_button()
        assert driver.current_url == TestData.expected_login_url, f"Expected URL: {TestData.expected_login_url}, but got: {driver.current_url}"

    def test_signup_button_displayed(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        assert login_page.is_signup_button_visible(), "Sign up button is not visible"

    def test_signup_button_enabled(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        login_page.click_signup_button()
        assert driver.current_url == TestData.expected_signup_url, f"Expected URL: {TestData.expected_signup_url}, but got: {driver.current_url}"

    def test_login_with_valid_credentials(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        login_page.login(TestData.valid_username,TestData.valid_password)
        assert driver.current_url == TestData.after_login_url

    def test_login_with_invalid_credentials(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        login_page.invalid_login(TestData.invalid_username,TestData.invalid_password)
        assert TestData.expected_login_url == driver.current_url

    def test_navbar_elements_displayed(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        assert login_page.are_nav_elements_displayed() is True

    def test_dobby_assistant_displayed(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        assert login_page.is_dobby_present() is True

    def test_logout_functionality(self,setup):
        driver, wait = setup
        driver.get(TestData.expected_url)
        login_page = LoginPage(driver, wait)
        login_page.login(TestData.valid_username,TestData.valid_password)
        assert login_page.logout() is True

