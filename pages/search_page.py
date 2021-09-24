from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class SearchPage(BasePage):
    #locators
    _advanced_search = By.XPATH, "//a[contains(text(),'Advanced search')]"

    
    def go_to_advanced_search(self):
        self.click_on(self._advanced_search)