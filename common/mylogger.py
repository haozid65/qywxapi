# -*- coding: utf-8 -*-
# Time: 2022/4/28 16:46
# Author: Gavin

"""
自定义日志
1、控制台输出
2、运行日志记录到文件
"""
import logging
import os

logger = logging.getLogger('wxapi')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.DEBUG)
# 添加控制台输出
logger.addHandler(sh)
# 定义日志存放文件路径
logs = os.path.join(os.path.dirname(__file__), '../logs')
if not os.path.exists(logs):
    os.mkdir(logs)
logfile = os.path.join(logs, 'wxapilog.log')
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

if __name__ == '__main__':
    logger.info('This is test')