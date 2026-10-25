from selenium.webdriver.common.by import By
from config.config import TestData
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    username_input = (By.NAME,"username")
    password_input= (By.NAME, "password")
    login_btn = (By.CSS_SELECTOR,".orangehrm-login-button")
   
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # self.username_input = self.driver.find_element(*self.username_input)
        # self.password_input = self.driver.find_element(*self.password_input)
        # self.login_btn = self.driver.find_element(*self.login_btn)

    def verify_login_page_usernam(self):
        username = self.wait.until(EC.presence_of_element_located(self.username_input))
        assert True == username.is_displayed()

    def verify_login_page_password(self):
        password = self.wait.until(EC.presence_of_element_located(self.password_input))
        assert True == password.is_displayed()

    def verify_login_button_visibility(self):
        loginbtn = self.wait.until(EC.presence_of_element_located(self.login_btn))
        assert True == loginbtn.is_displayed()

    def login_to_application(self):
        self.wait.until(EC.presence_of_element_located(self.username_input)).send_keys(TestData.USERNAME)
        self.wait.until(EC.presence_of_element_located(self.password_input)).send_keys(TestData.PASSWORD)
        self.wait.until(EC.presence_of_element_located(self.login_btn)).click()

    def verify_the_application_url_after_logging(self):
        self.wait.until(EC.url_contains('/dashboard/index'))
        assert '/dashboard/index' in self.driver.current_url



    


    