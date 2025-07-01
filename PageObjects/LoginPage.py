from logging import exception

from PageObjects.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from TestLocators.LoginLocators import LoginLocators
from selenium.common.exceptions import TimeoutException

class LoginPage(BasePage):

    # Constructor to initialize the driver using the parent class
    def __init__(self,driver,wait):
        super().__init__(driver,wait)

    # Check if login button is visible on the page
    def is_login_button_visible(self):
        return self.wait.until(EC.presence_of_element_located(LoginLocators.login_button_locator)).is_displayed()

    def click_login_button(self):
        self.click_element(LoginLocators.login_button_locator)

    # Check if signup button is visible
    def is_signup_button_visible(self):
        try:
            self.wait.until(EC.presence_of_element_located(LoginLocators.sign_up_button_locator)).is_displayed()
            return True
        except exception as e:
            print("Error:", e)

    def click_signup_button(self):
        self.click_element(LoginLocators.sign_up_button_locator)

    # Perform login with valid credentials and wait for dropdown to appear
    def login(self,username,password):
        self.click_element(LoginLocators.login_button_locator)
        self.enter_text(LoginLocators.username_locator,username)
        self.enter_text(LoginLocators.password_locator,password)
        self.click_element(LoginLocators.login_button_locator)
        self.wait.until(EC.visibility_of_element_located((LoginLocators.dropdown_locator)))
        return self.driver.current_url

    # Perform login with invalid credentials and return current URL
    def invalid_login(self,username,password):
        self.click_element(LoginLocators.login_button_locator)
        self.enter_text(LoginLocators.username_locator,username)
        self.enter_text(LoginLocators.password_locator,password)
        self.click_element(LoginLocators.login_button_locator)
        return self.driver.current_url

    # Verify key navigation elements are visible on the page
    def are_nav_elements_displayed(self):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.course_locator)).is_displayed()
        self.wait.until(EC.visibility_of_element_located(LoginLocators.live_class_locator)).is_displayed()
        self.wait.until(EC.visibility_of_element_located(LoginLocators.practice_locator)).is_displayed()
        return True

    # Check if the "Dobby" assistant element is present
    def is_dobby_present(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(LoginLocators.dobby_button_locator)).is_displayed()
        except TimeoutException:
            print("Dobby not present")
            return False

    # Logout by clicking dropdown and logout button
    def logout(self):
        self.click_element(LoginLocators.dropdown_locator)
        self.click_element(LoginLocators.logout_button_locator)
        return True


