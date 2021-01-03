# Gong
from appnium1.xueqiu.page.base_page import BasePage
from appnium1.xueqiu.page.market import Market


class Main(BasePage):

    def goto_market(self):
        # self.find(By.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']").click()
        self.setps('../page/main_interface.yaml')
        return Market(self._driver)



