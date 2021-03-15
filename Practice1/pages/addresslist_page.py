# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/15 21:42
@Auth ： Zoey
@File ：addresslist_page.py
@Description：
"""

from Practice1.pages.base_page import BasePage
from Practice1.pages.addcontact_page import AddContactPage


class AdressListPage(BasePage):

    def click_addcontact(self):
        # 点击添加成员按钮
        self.parse_action(r"../pages/addresslist.yaml", "click_addcontact")
        return AddContactPage(self.driver)
