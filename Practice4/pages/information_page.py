# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 9:51
# @Author  : Zoey
# @File    : information_page.py
# @describe: 信息页面

from Practice4.pages.base_page import BasePage
from Practice4.pages.addresslist_page import AddresslistPage


class InformationPage(BasePage):

    # 进入到通讯录页面
    def goto_addresslist(self):
        self.parse_action("../pages/information_page.yaml", "goto_addresslist")
        return AddresslistPage(self.driver)
