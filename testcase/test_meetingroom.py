# -*- coding: utf-8 -*-
# Time: 2022/4/30 11:32
# Author: Gavin
from core.basecase import BaseCase
import random
from pojo import MeetingRoom


class TestMeetingRoom(BaseCase):

    """
    meetingroom加入房间
    """
    def test_1add_meetingroom(self):
        url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/add?access_token={self.token}'
        adddata = {
                  "name":f"{random.random()}F-会议室",
                  "capacity":10,
                  "city":"深圳",
                  "building":"腾讯大厦",
                  "floor":"18F",
                  "equipment":[1,2,3],
                  "coordinate":
                  {
                    "latitude":"22.540503",
                    "longitude":"113.934528"
                  }
                }
        res = self.request(method='post', url=url, json=adddata)
        # 添加断言
        self.assertEqual(res.json()["errcode"], 0)
        self.assertEqual(res.json()["errmsg"], 'ok')
        # 设置上下游传参
        MeetingRoom.meetingroom_id = res.json()["meetingroom_id"]

    def test_2query_meetingroom(self):
        query_url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/list?access_token={self.token}'
        query_data = {
                          "city":"深圳",
                          "building":"腾讯大厦",
                          "floor":"18F",
                          "equipment":[1,2,3]
                        }
        res = self.request(method='post', url=query_url, json=query_data)
        meetingroom_list= res.json()['meetingroom_list']
        tmplist = []
        for meetingroom in meetingroom_list:
            tmplist.append(meetingroom['meetingroom_id'])
        print(tmplist)
        # 添加断言
        # 上面添加的会议室id应该在temlist中
        self.assertTrue(MeetingRoom.meetingroom_id in tmplist)

    def test_3del_meeting_room(self):
        del_url = f'https://qyapi.weixin.qq.com/cgi-bin/oa/meetingroom/del?access_token={self.token}'
        del_data = {
                  "meetingroom_id": MeetingRoom.meetingroom_id   # getattr(MeetingRoom, 'meetingroom_id'
                }
        res = self.request(method='post', url=del_url, json=del_data)
        # 删除 添加断言
        self.assertEqual(res.json()["errcode"], 0)
        self.assertEqual(res.json()["errmsg"], "ok")
