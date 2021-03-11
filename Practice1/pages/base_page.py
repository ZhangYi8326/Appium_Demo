# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:42
@Auth ： Zoey
@File ：base_page.py
@Description：
"""

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def app_init(self):
        pass

    def find_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()

    def find(self, locator):
        return self.driver.find_element_by_xpath(locator).text

    # 滑动操作
    def swip(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path):
        with open(path, "r", encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["locator"])
            elif step["action"] == "find":
                self.find(step["locator"])


