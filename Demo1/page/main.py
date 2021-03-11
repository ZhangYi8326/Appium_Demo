# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/6 22:17
@Auth ： Zoey
@File ：main.py
@Description：
"""
from Demo1.page.base_page import BasePage
from Demo1.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.steps("../page/main.yaml")
        return Market(self.driver)
