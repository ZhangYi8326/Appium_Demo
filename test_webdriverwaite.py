# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 18:05
# @Author  : Zoey
# @File    : test_webdriverwaite.py
# @describe:
from appium.webdriver import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriverWaite:
    def setup(self):
        desired_caps = dict()
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'HUAWEI'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = "true"
        # desired_caps['dontStopAppOnReset'] = "true"  # 设置首次启动的时候不停止app
        desired_caps['unicodeKeyBoard'] = "true"    # 设置中文输入
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        # WebDriverWait(self.driver, 10).until(expect_conditions)
        current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        assert float(current_price) > 200
