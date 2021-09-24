import pytest
from pages.home_page import HomePage
from pages.advanced_search_page import AdvancedSearchPage
from pages.advanced_search_result_page import AdvancedSearchResultPage
from pages.search_page import SearchPage
from pages.repo_page import RepoPage
import unittest
import time
from ddt import data, ddt, unpack
from utils.read_data import getCsvData


@pytest.mark.usefixtures("BrowserSetUp")
@ddt
class CheckCart(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def ClassSetup(self, BrowserSetUp):
        self.home_page = HomePage(self.driver)
        self.advanced_search_page = AdvancedSearchPage(self.driver)
        self.advanced_result_search_page = AdvancedSearchResultPage(self.driver)
        self.search_page = SearchPage(self.driver)
        self.repo_page = RepoPage(self.driver)
        self.home_page.go_to_test_url()

        yield

        self.driver.quit()

    @data(*getCsvData('data/search_repo.csv'))
    @unpack
    def test_search_product(self, framework, language, stars, followers, license, number, repo_name):              
        self.home_page.do_search(framework)
        self.search_page.go_to_advanced_search()
        self.advanced_search_page.do_advanced_search(language, stars, followers, license)

        assert self.advanced_result_search_page.is_only_one_repo(number)
        assert self.advanced_result_search_page.is_the_repo_name(repo_name)
        
        self.advanced_result_search_page.go_to_repo_page(repo_name)
        self.repo_page.go_to_readme()
        self.repo_page.print_readme()