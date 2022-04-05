# -*- coding: utf-8 -*-
# Time: 2022/4/5 16:05
# Author: Gavin
import requests
import datetime

# class historyToday:
#     def history_today(self, date):
now_mouth = datetime.datetime.now().strftime('%m').lstrip("0")
now_day = datetime.datetime.now().strftime('%d').lstrip("0")
now_date = now_mouth + "/" + now_day

url = "http://v.juhe.cn/todayOnhistory/queryEvent.php"
data = {"key": "acfcb3484c56ee390e359f9df121b2a4", "date": "5/25"}
res = requests.get(url, data)
print(res.json())