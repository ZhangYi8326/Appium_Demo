# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 15:04
# @Author  : Zoey
# @File    : del_page.py
# @describe: 删除联系人页面

from Practice4.pages.base_page import BasePage


class DelPage(BasePage):

    def del_member(self):
        # 进行删除操作
        self.parse_action("../pages/del_page.yaml", "del_member")
