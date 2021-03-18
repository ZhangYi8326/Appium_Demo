# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 15:28
# @Author  : Zoey
# @File    : test_member.py
# @describe:

from Practice4.pages.app import App


class TestMember:

    def setup(self):
        self.app = App()

    def test_member(self):
        self.member = "B004"
        self.app.goto_main().goto_addresslist().goto_detail(self.member).goto_editdetail_page().goto_del_page().del_member()
