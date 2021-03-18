# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 9:52
# @Author  : Zoey
# @File    : addresslist_page.py
# @describe: 通讯录列表页面

from Practice4.pages.base_page import BasePage
from Practice4.pages.detail_page import DetailPage


class AddresslistPage(BasePage):

    # 进入到个人信息页
    def goto_detail(self, member):
        self._params["member"] = member
        self.parse_action("../pages/addresslist_page.yaml", "goto_deatil")
        return DetailPage(self.driver)

    # # 判断是否删除成功
    # def del_suc(self):
    #     self.parse_action()
