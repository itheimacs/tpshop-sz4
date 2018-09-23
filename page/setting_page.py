import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 放大镜
    search_button = By.ID, "com.android.settings:id/search"

    @allure.step(title="点击搜索按钮")
    def click_search(self):
        self.click(self.search_button)

