from page.page import Page
from base.base_driver import init_driver
import allure, pytest


class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="放大镜-输入-返回")
    def test_search(self):
        self.page.setting.click_search()
        self.page.search.input_search("hello")
        self.page.search.click_back()

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="放大镜-返回")
    def test_search1(self):
        self.page.setting.click_search()
        self.page.search.click_back()

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    def test_search2(self):
        assert 0

    def teardown(self):
        self.driver.quit()