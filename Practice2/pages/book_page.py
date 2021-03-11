# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 22:20
@Auth ： Zoey
@File ：book_page.py
@Description：
"""

from Practice2.pages.base_page import BasePage


class BookPage(BasePage):

    def add_member(self):
        """
        :return:
        """
        # self.find_click("xpath", "//*[@text='添加成员']")
        # self.find_click("xpath", "//*[@text='手动输入添加']")
        # self.send_value("xpath", "//*[@text='必填']", "B003")
        # self.send_value("xpath", "//*[@text='手机号']", "13700000002")
        # self.find_click("xpath", "//*[@text='设置部门']")
        # self.find_click("id", "com.tencent.wework:id/fik")
        # self.find_click("id", "com.tencent.wework:id/gq7")
        # self.find_click("id", "com.tencent.wework:id/gpp")
        # text = self.get_text("xpath", "//*[@text='B003']")
        # print(text)
        # return text
        self.parse_action(r"../pages/mydata.yaml")
