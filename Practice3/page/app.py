# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 11:07
# @Author  : Zoey
# @File    : app.py
# @describe:

from Practice3.page.base_page import BasePage
from appium import webdriver
from Practice3.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".common.MainActivity"

    def star(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0.1'
            desired_caps['deviceName'] = 'HUAWEI'
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            desired_caps['noReset'] = "true"
            # desired_caps['dontStopAppOnReset'] = "true"  # 设置首次启动的时候不停止app
            desired_caps['unicodeKeyBoard'] = "true"  # 设置中文输入
            # desired_caps['udid'] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.start_activity(self._package, self._activity)
        self._driver.implicitly_wait(5)
        return self

    def main(self):
        return Main(self._driver)
