# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 9:53
# @Author  : Zoey
# @File    : detail_page.py
# @describe: 个人信息页面

from Practice4.pages.base_page import BasePage
from Practice4.pages.editdetail_page import EditDetailPage


class DetailPage(BasePage):

    def goto_editdetail_page(self):
        # 进入到编辑成员页面
        self.parse_action("../pages/detail_page.yaml", "goto_editdetail_page")
        return EditDetailPage(self.driver)
