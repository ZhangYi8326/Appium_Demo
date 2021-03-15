# -*- coding: utf-8 -*-
# @Time    : 2021/3/12 11:18
# @Author  : Zoey
# @File    : main.py
# @describe:
from selenium.webdriver.common.by import By

from Practice3.page.base_page import BasePage


class Main(BasePage):

    def goto_search(self):
        # self.find(By.ID, "com.xueqiu.android:id/tv_search").click()
        self.steps("../page/main.yaml")

    def goto_windows(self):
        self.find(By.ID, "post_status").click()
        self.find(By.ID, "com.xueqiu.android:id/tv_search").click()
