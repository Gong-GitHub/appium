# Gong
import inspect
import json
import yaml

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from appnium1.xueqiu.page.wrapper import handle_black


class BasePage:
    # “_params”:定义一个公共的变量区域，用来存字典
    _params={}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 截图
    def screenshot(self, name):
        self._driver.save_screenshot(name)

    def finds(self, locator, value: str = None):
        elements: list  # 会找到一组元素
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        element: WebElement
        # 对元素进行判断
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        return element

    # 使用yaml来进行测试步骤的数据驱动,"name":方法名
    def setps(self, path):
        # "encoding='utf-8'": 编码，防止中文报错
        with open(path, encoding='utf-8') as f:
            # "inspect.stack()",[0]:代表自己 | [1]:代表直接调用我的, 以此类推;"function":取出函数名
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        # 把变量加载到json中，把python对象变成streaming
        raw = json.dumps(steps)
        # 对所有的变量进行遍历替换
        for key, value in self._params.items():
            # ${name} | name:12345
            # 12345
            raw = raw.replace('${'+key+'}', value)
        steps = json.loads(raw)
        # 当yaml文件中有多个数时，对它进行遍历
        for step in steps:
            if "action" in step.keys():
                action = step["action"]
                if 'click' == action:
                    self.find(step["by"], step["locator"]).click()
                if 'send' == action:
                    self.find(step["by"], step["locator"]).send_keys(step["value"])
                if 'len > 0' == action:
                    ele = self.finds(step["by"], step["locator"])
                    # 当ele长度大于0时查找成功
                    return len(ele) > 0