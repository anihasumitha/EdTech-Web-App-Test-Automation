from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self,driver,wait):
        self.driver=driver
        self.wait=wait

    def enter_text(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()




