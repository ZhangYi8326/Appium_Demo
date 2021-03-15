# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/15 21:45
@Auth ： Zoey
@File ：addcontact_page.py
@Description：
"""

from Practice1.pages.base_page import BasePage
from Practice1.pages.editcontact_page import EditContactPage


class AddContactPage(BasePage):

    def addcontact_menual(self):
        # 点击手动输入添加
        self.parse_action(r"../pages/addcontact_page.yaml", "addcontact_menual")
        return EditContactPage()
