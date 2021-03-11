# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:13
@Auth ： Zoey
@File ：work_page.py
@Description：工作台页面
"""

import time
from Practice1.pages.base_page import BasePage
from Practice1.pages.sigin_page import SignPage


class WorkPage(BasePage):

    def goto_sing_page(self):
        self.swip("打卡")
        return SignPage(self.driver)
