# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 17:37
# @Author  : Zoey
# @File    : base_page.py
# @describe:

from appium.webdriver.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find(self, by, locator=None):
        try:
            if isinstance(by, tuple):
                return self.driver.find_elements(*by)
            else:
                return self.driver.find_element(by, locator)
        except Exception as e:
            for

