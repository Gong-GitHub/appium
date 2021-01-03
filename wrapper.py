# Gong
# 装饰器
import logging

import allure
from selenium.webdriver.common.by import By


def handle_black(func):
    # 设置日志的等级为INFO
    logging.basicConfig(level=logging.INFO)

    def wrapper(*args, **kwargs):
        # 局部导入，防止循环导入
        from appnium1.xueqiu.page.base_page import BasePage
        # 弹框处理的名单列表
        _black_list = [
            (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/action_search']"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        # 设置查找异常的次数
        _max_num = 3
        _error_num = 0
        # “: BasePage”: python 3.6以后的新特性,注解,提示它是什么类型;"args[0]":相当于取出self
        instance: BasePage = args[0]
        try:
            # 生成日志
            logging.info("run "+func.__name__+"\n agrs: \n"+repr(args)+"\n"+repr(kwargs))
            element = func(*args, **kwargs)
            # 查找之前_error_num 归 0
            _error_num = 0
            # 隐式等待恢复原来的等待
            instance._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 发生异常时截图
            instance.screenshot("tmp.png")
            # 把图片以二进制加载进来
            with open("tmp.png", "rb") as f:
                content = f.read()
            # 把截图插到allure报告中
            allure.attach(content, attachment_type=allure.attachment_type.PNG)
            # 生成错误信息日志
            logging.error("element not found,handle black list")
            # 出现异常，将隐式等待设置小一点，快速处理弹框
            instance._driver.implicitly_wait(10)
            # 判断查找次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再去查找目标元素
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper