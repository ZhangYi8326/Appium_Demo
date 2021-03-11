# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/6 22:21
@Auth ： Zoey
@File ：market.py
@Description：
"""
from Demo1.page.base_page import BasePage
from Demo1.page.search import Search


class Market(BasePage):
    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self.driver)
