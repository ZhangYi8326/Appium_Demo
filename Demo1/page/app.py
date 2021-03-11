# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/6 22:08
@Auth ： Zoey
@File ：app.py
@Description：
"""
from Demo1.page.base_page import BasePage
from appium import webdriver

from Demo1.page.main import Main


class App(BasePage):
    def star(self):
        if self.driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0.1'
            desired_caps['deviceName'] = 'HUAWEI'
            desired_caps['appPackage'] = 'com.xueqiu.android'
            desired_caps['appActivity'] = '.common.MainActivity'
            self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.start_activity('com.xueqiu.android', '.common.MainActivity')

        return self

    def main(self):
        return Main(self.driver)
