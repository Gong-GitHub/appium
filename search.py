# Gong
from appnium1.xueqiu.page.base_page import BasePage


class Search(BasePage):

    def search(self, name):
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys('alibaba')
        # self.find(By.XPATH, '//*[@text="BABA"]').click()
        # self.find(By.XPATH,
        #           f"//*[@resource-id='com.xueqiu.android:id/stock_layout']//*[@text='{name}']/../..//*[@text='加自选']").click()

        # 把变量的值存到“_params”
        self._params["name"] = name
        self.setps('../page/search.yaml')

    # 点击加自选
    def add(self, name):
        self._params["name"] = name
        return self.setps('../page/search.yaml')

    def is_choose(self, name):
        # ele = self.finds(By.XPATH,
        #                  f"//*[@resource-id='com.xueqiu.android:id/stock_layout']//*[@text='{name}']/../..//*[@text='已添加']")
        self._params["name"] = name
        return self.setps('../page/search.yaml')

    # 取消已添加
    def reset(self, name):
        self._params["name"] = name
        return self.setps('../page/search.yaml')

