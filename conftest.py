from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.firefox import GeckoDrivermanager
import pytest
from config.config import TestData
from pages.login_page import LoginPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    # Pytest uses request.param to pass a single parameter value from the params list. Using request.params will raise an AttributeError.
    if request.param=='chrome':
        # service = ChromeService(ChromeDriverManager().install())
        # web_driver = webdriver.Chrome(service=service)
        options = Options()
        options.add_argument("--headless=new")  # Run headlessly for CI/CD
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        
    # elif request.param=='firefox':
        # web_driver = webdriver.Firefox(executable_path=GeckoDriverManager.install())
    
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    web_driver.get(TestData.BASE_URL)

    # Attach driver to the test class
    request.cls.driver = web_driver

    yield
    request.cls.driver.quit()



@pytest.fixture(scope="function")
def logged_in_user(init_driver, request):
    """Fixture that automatically logs into the application before the test runs."""
    driver = request.instance.driver  # Accesses the driver attached to the test class
    # driver.get(TestData.BASE_URL)
    
    # Use your Page Object Model login actions
    login_page = LoginPage(driver)
    login_page.login_to_application()
    yield driver


