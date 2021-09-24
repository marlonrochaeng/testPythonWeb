from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.common.keys import Keys

class AdvancedSearchResultPage(BasePage):
    #locators
    _repos = By.CLASS_NAME, 'v-align-middle'

    def get_repo(self, repo):
        return By.XPATH, f"//a[@href='/{repo}']"
    
    def get_result_number(self, number):
        return By.XPATH, f"//h3[contains(text(),'{number} repository result')]"
    

    def is_only_one_repo(self, number):
        return self.is_element_present(self.get_result_number(number))
        
    def is_the_repo_name(self, repo_name):
        return repo_name in self.driver.page_source
    
    def go_to_repo_page(self,repo):
        self.js_click(self.get_repo(repo))
