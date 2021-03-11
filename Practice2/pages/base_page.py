# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 22:11
@Auth ： Zoey
@File ：base_page.py
@Description：
"""
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 选择定位方式
    def __find_element(self, by, locator):
        if by == "id":
            self.element = self.driver.find_element_by_id(locator)
        elif by == "css":
            self.element = self.driver.find_element_by_css_selector(locator)
        elif by == "xpath":
            self.element = self.driver.find_element_by_xpath(locator)
        return self.element

    # 点击元素
    def find_click(self, by, locator):
        self.__find_element(by, locator).click()

    # 输入值
    def send_value(self, by, locator, value):
        self.__find_element(by, locator).send_keys(value)

    # 获取元素值
    def get_text(self, by, locator):
        return self.__find_element(by, locator).text

    # 读取yaml文件，并根据action获取其他值，进行操作
    def parse_action(self, path):
        with open(path, "r", encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "send_value":
                self.send_value(step["by"], step["locator"], step["value"])
            elif step["action"] == "get_text":
                self.get_text(step["by"], step["locator"])
