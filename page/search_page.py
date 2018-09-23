import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SearchPage(BaseAction):
    # 输入框
    search_edit_text = By.ID, "android:id/search_src_text"

    # 返回
    back_button = By.CLASS_NAME, "android.widget.ImageButton"

    @allure.step(title="输入关键字")
    def input_search(self, text):
        allure.attach('在输入框中输入', text)
        # allure.attach('在输入框中输入' + text, "")
        self.input(self.search_edit_text, text)

        time.sleep(1)
        self.driver.get_screenshot_as_file("./screen/xxx.png")
        time.sleep(1)
        # with open("./screen/xxx.png", 'rb') as f:
        #     allure.attach('描述', f.read(), allure.attach_type.PNG)

        allure.attach("xxxx", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)


    @allure.step(title="点击返回")
    def click_back(self):
        self.click(self.back_button)

