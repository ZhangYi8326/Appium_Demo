# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 14:06
# @Author  : Zoey
# @File    : test_logging.py
# @describe:

import logging
from time import ctime
import time
import sys


# class GetLogging:
#     logging.basicConfig(level=logging.INFO)
#
#     def loop0(self):
#         logging.info("start loop0 at " + ctime())
#         time.sleep(4)
#         logging.info("end loop0 " + ctime())
#
#     def loop1(self):
#         logging.info("start loop0 at " + ctime())
#         time.sleep(2)
#         logging.info("end loop0 " + ctime())


class FormatLogging:

    def __init__(self):
        self.log_z = logging.getLogger(__name__)   # 初始化logging
        # logging.basicConfig(level=logging.DEBUG,
        #                     # 日志格式
        #                     # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
        #                     format='%(asctime).19s%(filename)s[line:%(lineno)d]%(levelname)s%(message).500s',
        #                     # 打印日志的时间
        #                     datefmt='%a, %d, %b, %Y, %H:%M:%S',
        #                     stream=sys.stderr,
        #                     # # 日志文件存放的目录(目录必须存在)及日志文件名
        #                     # filename='report.log',
        #                     # # 打开日志文件的方式
        #                     # filemode='w'
        #                     )
        self.log_z.setLevel(level=logging.DEBUG)    # 定义日志级别
        log_format = logging.Formatter('%(filename)s[line:%(lineno)d]%(levelname)s%(message).500s')
        console = logging.StreamHandler()   # 向控制台输入日志
        console.setLevel(level=logging.DEBUG)
        console.setFormatter(log_format)
        self.log_z.addHandler(console)

    def get_logger(self):
        return self.log_z


if __name__ == '__main__':
    # log = GetLogging()
    # logging.info("start all at " + ctime())
    # log.loop0()
    # log.loop1()
    # logging.info("end all at " + ctime())
    logger = FormatLogging().get_logger()
    logger.debug("start logging " + ctime())
    time.sleep(5)
    logger.info("end logging" + ctime())
