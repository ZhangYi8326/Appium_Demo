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
from Practice1.pages.addresslist_page import AdressListPage


class InformationPage(BasePage):

    def goto_work_page(self):
        # 进入到工作台页面
        self.parse_action("../pages/information_page.yaml", "goto_work_page")
        return WorkPage(self.driver)

    def goto_addresslist(self):
        # 进入到通讯录页面
        self.parse_action("../pages/information_page.yaml", "goto_addresslist")
        return AdressListPage(self.driver)


