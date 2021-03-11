# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:12
@Auth ： Zoey
@File ：information_page.py
@Description：消息页面
"""
import time
from Practice1.pages.work_page import WorkPage
from Practice1.pages.base_page import BasePage


class InformationPage(BasePage):

    def goto_work_page(self):
        self.parse_action(r"../pages/information_page.yaml")
        return WorkPage(self.driver)
