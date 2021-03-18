# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 9:58
# @Author  : Zoey
# @File    : base_page.py
# @describe:

import yaml
import json
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from Practice4.conftest import get_log


class BasePage:

    # 定义一个字典，用来处理yaml中替换值
    _params = dict()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.log = get_log()

    def __find_element(self, by, locator):
        """
        定位元素方法
        :param by:
        :param locator:
        :return: element
        """
        try:
            element = self.driver.find_element(by, locator)
            self.log.info(f"定位元素中：by={by}, locator={locator}")
        except Exception as e:
            self.log.error("元素定位错误")
            raise Exception(e)
        else:
            return element
        finally:
            pass

    # 点击元素
    def click_element(self, by, locator):
        ele = self.__find_element(by, locator)
        ele.click()
        self.log.info("执行了元素点击操作")

    # 输入值
    def send_element(self, by, locator, text):
        ele = self.__find_element(by, locator)
        ele.send_keys(text)
        self.log.info("执行了输入text操作")

    # 滑动操作
    def swip(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        """
        关键字驱动
        :param path:
        :param fun_name:
        :return:
        """
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps = function[fun_name]
            # json.doumps() 将python对象转换成字符串
            raw = json.dumps(steps)
            for key, value in self._params.items():
                # 替换yaml中的value
                raw = raw.replace("${" + key + "}", value)
            print(raw)
            steps = json.loads(raw)
            print(steps)
            for step in steps:
                if step["action"] == "find_click":
                    self.click_element(step["by"], step["locator"])
                elif step["action"] == "send_keys":
                    self.send_element(step["by"], step["locator"])
                elif step["action"] == "swip":
                    print(step["text"])
                    self.swip(step["text"])
