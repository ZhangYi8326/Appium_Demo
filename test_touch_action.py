# -*- coding: utf-8 -*-
# @Time    : 2021/2/25 11:22
# @Author  : Zoey
# @File    : test_touch_action.py
# @describe:

from appium import webdriver
import pytest
import time
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:

    def setup(self):
        desired_caps = dict()
        desired_caps["platformName"] = "android"
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'HUAWEI'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_touch_action(self):
        """
        手势密码锁
        :return:
        """
        action = TouchAction(self.driver)
        time.sleep(3)
        action.press(x=94, y=140).wait(200).move_to(x=292, y=136).wait(200).move_to(x=481, y=141).wait(200)\
            .move_to(x=480, y=327).release().perform()
        time.sleep(3)


if __name__ == '__main__':
    pytest.main()
