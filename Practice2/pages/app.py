# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 22:16
@Auth ： Zoey
@File ：app.py
@Description：
"""

from appium import webdriver

from Practice2.pages.information_page import InformationPage


class App:

    def __init__(self):
        self.driver = None
        self.start()

    def start(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'HUAWEI'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = "true"
        # desired_caps['dontStopAppOnReset'] = "true"  # 设置首次启动的时候不停止app
        desired_caps['unicodeKeyBoard'] = "true"  # 设置中文输入
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def goto_main(self):
        return InformationPage(self.driver)
