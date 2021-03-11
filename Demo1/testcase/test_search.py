# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/7 21:01
@Auth ： Zoey
@File ：test_search.py
@Description：
"""
from Demo1.page.app import App


class TestSearch:
    def test_search(self):
        App().star().main().goto_market().goto_search()
