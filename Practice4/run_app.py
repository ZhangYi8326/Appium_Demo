# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:58
# @Author  : Zoey
# @File    : run_app.py
# @describe:  程序入口

import pytest

from Practice4.webhook import WebHook

pytest.main(["-s", "-q", "--alluredir=./result/5"])
WebHook().web_hook()

