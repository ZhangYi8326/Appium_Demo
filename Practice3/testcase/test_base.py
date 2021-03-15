# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 15:39
# @Author  : Zoey
# @File    : test_base.py
# @describe:

from Practice3.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()
