from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class AdvancedSearchPage(BasePage):
    #locators
    _select_language = By.ID, "search_language"
    _stars = By.ID, "search_stars"
    _followers = By.ID, "search_followers"
    _select_license = By.ID, "search_license"
    _search_button = By.XPATH, "(//button[contains(text(),'Search')])[2]"


    
    def do_advanced_search(self, language, stars, followers, license):
        self.select_element_by_text(self._select_language, language)
        self.send_keys(self._stars, stars)
        self.send_keys(self._followers, followers)
        self.select_element_by_text(self._select_license, license)
        self.click_on(self._search_button)
