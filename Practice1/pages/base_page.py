# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/8 21:42
@Auth ： Zoey
@File ：base_page.py
@Description：
"""

import yaml
import json
import logging
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


logging.basicConfig(level=logging.INFO,
                    # 日志格式
                    # 时间、代码所在文件名、代码行号、日志级别名字、日志信息
                    format='%(asctime).19s%(filename)s[line:%(lineno)d]%(levelname)s%(message).500s',
                    # 打印日志的时间
                    datefmt='%a, %d, %b, %Y, %H:%M:%S',
                    # 日志文件存放的目录(目录必须存在)及日志文件名
                    filename='report.log',
                    # 打开日志文件的方式
                    filemode='w'
                    )


class BasePage:
    # 定义一个字典
    _params = dict()
    # 定义一个弹框列表
    _blacklist = list[(MobileBy.ID, "com.tencent.wework:id/ig0"),
                      (MobileBy.XPATH, '//*[@text="关闭"]')
                    ]
    _max_num = 3
    _error_num = 0
    log = logging.getLogger(__name__)

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_click(self, by, locator):
        self.log.info(f"find: by={by}, locator = {locator}")
        try:
            element = self.driver.find_element(by, locator).click()
            self._error_num = 0
            return element
        except Exception as e:
            # 处理黑名单逻辑
            # 设置最大查找次数
            if self._error_num > self._max_num:
                self._error_num = 0
                raise e
            # 每次进except 一次执行+1操作
            self._error_num += 1
            # 处理黑名单
            for ele in self._blacklist:
                # find_elements 返回一个元素列表，如果没有则返回空
                eles = self.driver.find_elements(*ele)
                if len(eles) > 0:
                    eles[0].click()
                    return self.find(by, locator)
            # 如果黑名单都处理完，仍然没有找到想要的元素，则抛出异常
            raise e

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 滑动操作
    def swip(self, text):
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 f'text("{text}").instance(0));').click()

    def parse_action(self, path, fun_name):
        with open(path, "r", encoding="utf-8") as f:
            function = yaml.safe_load(f)
            steps: list(dict) = function[fun_name]
        # json 序列化与反序列化
        # json.doups()序列化 python对象转化成字符串
        # json.load()反序列化 将字符串，转化成字符串
        raw = json.dumps(steps)
        for key, value in self._params.items():
            raw = raw.replace("${"+key+"}", value)
        for step in steps:
            if step["action"] == "find_click":
                self.find_click(step["by"], step["locator"])
            elif step["action"] == "find":
                self.find(step["by"], step["locator"])
            elif step["action"] == "swip":
                self.swip(step["text"])
            elif step["action"] == "find_sendkeys":
                self.find(step["by"], step["locator"]).send_keys(step["text"])


