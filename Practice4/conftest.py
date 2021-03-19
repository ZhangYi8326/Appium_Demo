# -*- coding: utf-8 -*-
# @Time    : 2021/3/18 11:06
# @Author  : Zoey
# @File    : conftest.py
# @describe:

import logging
import pytest


# @pytest.fixture(scope="class")
def get_log():
    """
    日志输出
    :return:
    """
    log_z = logging.getLogger(__name__)  # 初始化logging
    log_z.setLevel(level=logging.INFO)  # 定义日志级别
    log_format = logging.Formatter('%(filename)s[line:%(lineno)d]%(levelname)s%(message).500s')
    console = logging.StreamHandler()  # 向控制台输出日志
    console.setFormatter(log_format)
    # log_z.addHandler(console)
    return log_z
