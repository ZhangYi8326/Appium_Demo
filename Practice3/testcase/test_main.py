# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 11:24
# @Author  : Zoey
# @File    : test_main.py
# @describe:


from Practice3.testcase.test_base import TestBase


class TestMain(TestBase):

    def test_main(self):
        self.app.main().goto_search()

    def test_windows(self):
        self.app.star().main().goto_windows()
