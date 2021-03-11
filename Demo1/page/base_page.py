# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/6 21:41
@Auth ： Zoey
@File ：base_page.py
@Description：
"""
import yaml
from appium.webdriver.webdriver import WebDriver


class BasePage:
    black_list = []
    param = dict()

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        try:
            return self.driver.find_elements(*by) if isinstance(by, tuple) else self.driver.find_element(by, locator)
        except Exception as e:
            for black in self.black_list:
                elements = self.driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)
            raise e

    def steps(self, path):  # 数据驱动，读取文件
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        element.click()
                    if "send" == step["action"]:
                        content: str = step["value"]
                        for param in self.param:
                            content = content.replace("{%s}" % param, self.param[param])
                        element.send_keys(content)
