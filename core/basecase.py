# -*- coding: utf-8 -*-
# Time: 2022/4/26 18:13
# Author: Gavin

import unittest
import requests
from config import configdata


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        res = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={configdata["weixin"]["corpid"]}&corpsecret={configdata["weixin"]["corpid"]["meetingroom"]}')
        # cls.token = res.json()
        # print(cls.token)
        return cls.token

