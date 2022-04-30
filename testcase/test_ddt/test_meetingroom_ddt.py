# -*- coding: utf-8 -*-
# Time: 2022/4/30 18:57
# Author: Gavin
from ddt import ddt, data, unpack, file_data
from core.basecase import BaseCase
import unittest


@ddt
class TestMeetingRoomDDT(BaseCase):
    @unittest.skip("No Test")
    @data(["1234567890123456789012345678901", 40058, "name exceed max utf8 words 30"], ["", 40058, "missing paramters name"])
    @unpack
    def test_add_meetingroom(self, name, expext_errcode, expext_err_msg):
        """
        测试一场景
        :return:
        """
        url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}'
        adddata = {
            "name": name,
            "capacity": 10,
        }
        res = self.request(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(res.json()["errcode"], expext_errcode)
        self.assertTrue(expext_err_msg in res.json()['errmsg'])
        # 设置上下游传参
        # MeetingRoom.meetingroom_id = res.json()["meetingroom_id"]

    @unittest.skip("No Test")
    @file_data("../../testdata/meetingroom/addmeetingroom.json")
    def test_add_meetingroom_json_data(self, name, expext_errcode, expext_err_msg):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}'
        adddata = {
            "name": name,
            "capacity": 10,
        }
        res = self.request(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(res.json()["errcode"], expext_errcode)
        self.assertTrue(expext_err_msg in res.json()['errmsg'])

    @file_data("../../testdata/meetingroom/addmeetingroom.yaml")
    def test_add_meetingroom_yaml_data(self, name, expext_errcode, expext_err_msg):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}'
        adddata = {
            "name": name,
            "capacity": 10,
        }
        res = self.request(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(res.json()["errcode"], expext_errcode)
        self.assertTrue(expext_err_msg in res.json()['errmsg'])
