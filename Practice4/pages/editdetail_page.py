# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 14:57
# @Author  : Zoey
# @File    : editdetail_page.py
# @describe:

from Practice4.pages.base_page import BasePage
from Practice4.pages.del_page import DelPage


class EditDetailPage(BasePage):

    def goto_del_page(self):
        self.parse_action("../pages/editdetail_page.yaml", "goto_del_page")
        return DelPage(self.driver)
