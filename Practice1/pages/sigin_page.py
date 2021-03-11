# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:13
@Auth ： Zoey
@File ：sigin_page.py
@Description：打卡页面
"""
from Practice1.pages.base_page import BasePage


class SignPage(BasePage):

    def sign(self):
        self.parse_action("../pages/sign_page.yaml")
        # self.find_click("//*[@text='外出打卡']")
        # self.find_click("//*[contains(@text,'次外出')]")
        # self.find("//*[@text='外出打卡成功']")

    # def first_sign(self):
    #     self.find_click("//*[@text='上下班打卡']")
