# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/15 22:19
@Auth ： Zoey
@File ：test_contact.py
@Description：
"""

from Practice1.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()

    def test_addcontact(self):
        name = "B006"
        phone = "13099000991"
        editpage = self.app.goto_main().goto_addresslist().click_addcontact().addcontact_menual()
        editpage.edit_contact(name, phone)
        editpage.verify_ok()
