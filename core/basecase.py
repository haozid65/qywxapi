# -*- coding: utf-8 -*-
# Time: 2022/4/26 18:13
# Author: Gavin

import unittest
import requests
from config import configdata
from common.mylogger import logger


class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        r = cls.request('get', f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={configdata["weixin"]["corpid"]}&corpsecret={configdata["weixin"]["corpsecrets"]["meetingroom"]}')
        cls.token = r.json()['access_token']

    @classmethod
    def request(cls, method: str, url, params=None, data=None, json=None, **args):
        method = method.upper()
        if method == 'GET':
            res = requests.get(url, params=params, **args)
            logger.info(f'请求方式：{method}, 请求url: {url}, 请求参数：{res.request.body}, 服务器返回结果：{res.text}')
            return res
        if method == 'POST':
            res = requests.post(url, data=data, json=json, **args)
            logger.info(f'请求方式：{method}, 请求url: {url}, 请求参数：{res.request.body}, 服务器返回结果：{res.text}')
            return res
