# Gong
from selenium.webdriver.common.by import By

from appnium1.xueqiu.page.base_page import BasePage
from appnium1.xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        # 注释掉用于验证装饰器
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self._driver)
