# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 16:39
# @Author  : Zoey
# @File    : webhook.py
# @describe: 钉钉机器人发送推送

import json
import requests


class WebHook:
    def __init__(self):
        self.url = "你的webhook地址"

    def web_hook(self):
        url = self.url
        program = {
             "msgtype": "text", # 消息类型，固定为text
             "text": {
                 "content": "我就是我, @15775690803 小富婆"    # 消息内容
             },
             "at": {
                 "atMobiles": [
                     "15775690803"  # 被@人的手机号
                 ],
                 "isAtAll": False   # 是否@所有人
             }
         }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(program), headers=headers)


if __name__ == '__main__':
    a = WebHook()
    a.web_hook()
