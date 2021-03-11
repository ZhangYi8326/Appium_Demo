# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/9 22:19
@Auth ： Zoey
@File ：information_page.py
@Description：
"""

from Practice2.pages.base_page import BasePage
from Practice2.pages.book_page import BookPage


class InformationPage(BasePage):

    def goto_book_page(self):
        self.parse_action(r"../pages/mydata.yaml")
        return BookPage(self.driver)
