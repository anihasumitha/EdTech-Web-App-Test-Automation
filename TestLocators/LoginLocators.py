from selenium.webdriver.common.by import By

class LoginLocators:
        username_locator = (By.ID,"email")
        password_locator = (By.ID,"password")
        login_button_locator = (By.ID,"login-btn")
        sign_up_button_locator=(By.XPATH,"//a[contains(text(),'Sign up')]")
        nav_elements_locator = (By.XPATH,"//div[@class='navbarlinks']//a | //div[@class='navbarlinks']//div[@id]")
        dobby_button_locator = (By.XPATH, "//button[@id='ymDivBar']")
        dropdown_locator=(By.XPATH,"//div[@id='dropdown_title']")
        logout_button_locator = (By.XPATH,"//div[@id='dropdown_contents' and contains(text(),'Sign Out')]")
        course_locator=(By.XPATH,"//a[@href = '/courses/']")
        live_class_locator = (By.XPATH,"//p[@id = 'liveclasseslink']")
        practice_locator=(By.XPATH,'//p[@id="practiceslink"]')

