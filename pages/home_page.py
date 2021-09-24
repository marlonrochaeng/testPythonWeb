from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class HomePage(BasePage):
    #locators
    _search_bar = By.NAME, "q"

    
    def do_search(self, search):
        self.send_keys(self._search_bar, search)
        self.send_keys(self._search_bar, Keys.ENTER)