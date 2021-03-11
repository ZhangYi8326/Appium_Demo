# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/10 22:54
@Auth ： Zoey
@File ：test_add_member.py
@Description：手动输入添加成员
"""

from Practice2.pages.app import App


class TestAddMember:

    def setup(self):
        self.app = App()

    def test_add_member(self):
        self.app.goto_main().goto_book_page().add_member()
