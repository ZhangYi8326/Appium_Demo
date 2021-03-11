# -*- coding: utf-8 -*-
# @Time    : 2021/2/26 15:41
# @Author  : Zoey
# @File    : test_param.py
# @describe:

from appium import webdriver
import time
import pytest
from hamcrest import *

from appium.webdriver.common.mobileby import MobileBy


class TestParam:
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
        desired_caps['unicodeKeyBoard'] = "true"  # 设置中文输入
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        pass
        # self.driver.quit()

    @pytest.mark.parametrize('searchkey, price', [
        ("阿里巴巴", 235),
        ("小米", 25)
    ])
    def test_search(self, searchkey, price):
        """
        1、打开雪球app
        2、点击搜索框
        3、输入“阿里巴巴” or “小米”
        4、点击第一个搜索结果
        5、判断股票价格
        :return:
        """
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        time.sleep(3)
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys(searchkey)
        time.sleep(3)
        self.driver.find_elements_by_xpath("//*[@resource-id='com.xueqiu.android:id/name']")[0].click()
        current_price = self.driver.find_elements_by_id("com.xueqiu.android:id/current_price")[0].text
        # expect_price = 235
        assert_that(float(current_price), close_to(price, price*0.1))
        time.sleep(3)


if __name__ == '__main__':
    pytest.main()
