# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/15 21:54
@Auth ： Zoey
@File ：editcontact_page.py
@Description：
"""

from Practice1.pages.base_page import BasePage


class EditContactPage(BasePage):

    def edit_contact(self):
        """
        编辑成员
        :return:
        """
        self.parse_action("../pages/editcontact_page.yaml", "edit_contact")

    def verify_ok(self):
        """
        :return:
        """
        self.parse_action("../pages/editcontact_page.yaml", "verify_ok")
