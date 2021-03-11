# -*- coding: utf-8 -*-
"""
@Time ： 2021/2/10 17:56
@Auth ： Zoey
@File ：test_firstappium.py
@Description：
"""

from appium import webdriver
import time
import pytest
from appium.webdriver.common.touch_action import TouchAction


class TestFirst:

    def setup(self):
        desired_caps = dict()
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'HUAWEI'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.common.MainActivity'
        desired_caps['noReset'] = "true"
        # desired_caps['dontStopAppOnReset'] = "true"  # 设置首次启动的时候不停止app
        desired_caps['unicodeKeyBoard'] = "true"    # 设置中文输入
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200

    def test_attr(self):
        """
        1、打开【雪球】应用首页
        2、定位首页的搜索框
        3、判断搜索框是否可用，并查看搜索框name属性值
        4、打印搜索框这个元素的左上角坐标和它的宽高
        5、向搜索框输入:alibaba
        6、判断【阿里巴巴】是否可见
        7、如果可见，打印‘搜索成功’点击，如果不可见，打印‘搜索失败’
        :return:
        """
        self.driver.implicitly_wait(5)
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        if search_enabled == True:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            alibaba_element = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
            element_display = alibaba_element.get_attribute("displayed")
            if element_display == 'true':
                print("搜索成功")
            else:
                print("搜索失败")

    def test_touchaction(self):
        """
        滑动操作
        :return:
        """
        action = TouchAction(self.driver)
        #   获取宽和高
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        print(window_rect)
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()


if __name__ == '__main__':
    pytest.main()
