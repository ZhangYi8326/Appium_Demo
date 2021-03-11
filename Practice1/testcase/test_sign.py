# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:34
@Auth ： Zoey
@File ：test_sign.py
@Description：
"""
from Practice1.pages.app import App


class TestSign:

    def setup(self):
        self.app = App()

    def test_sign(self):
        self.app.goto_main().goto_work_page().goto_sing_page().sign()
