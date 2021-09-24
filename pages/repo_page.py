from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class RepoPage(BasePage):
    #locators
    _readme = By.XPATH, "//a[contains(text(),'README.md')]"
    _readme_content = By.ID, "readme"
    _raw = By.ID, "raw-url"

    
    def go_to_readme(self):
        self.click_on(self._readme)
    
    def print_readme(self):
        self.click_on(self._raw)
        print(self.driver.page_source[:300].encode('utf-8'))