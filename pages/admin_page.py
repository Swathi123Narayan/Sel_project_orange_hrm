from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdminPage:
    adminpage_module=(By.XPATH,'//a[@class="oxd-main-menu-item"]')
    admin_page_header = (By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']")

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_admin_section(self):
        self.wait.until(EC.element_to_be_clickable(self.adminpage_module)).click()
        header_element = self.wait.until(EC.presence_of_element_located(self.admin_page_header))
        assert "Admin" in header_element.text