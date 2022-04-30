# -*- coding: utf-8 -*-
# Time: 2022/4/28 17:45
# Author: Gavin
# import requests
# res = requests.get(
#             # 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={configdata["weixin"]["corpid"]}&corpsecret={configdata["weixin"]["corpid"]["meetingroom"]}')
#             'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww89b2a53d32946206&corpsecret=fyIg-qCidHf5IrUMUn5563j3_4rhXPC5Ix_v8AhZlXk')
# print(res.json())
from config import configdata

# data = {'corpid': configdata["weixin"]["corpid"], 'corpsecret': ["corpsecrets"]["meetingroom"]}
data = {'corpsecret': ["meetingroom"]}

print('----------------', data)
