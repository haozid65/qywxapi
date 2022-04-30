"""
运行整个testcase下所有的文件
"""

import unittest
from testcase.test_meetingroom import TestMeetingRoom
from testcase.test_ddt.test_meetingroom_ddt import TestMeetingRoomDDT
from BeautifulReport import BeautifulReport


def allTests():
    """
    执行所有的用例
    :return:
    """
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    alltests = loader.discover(start_dir='testcase')
    suite.addTests(alltests)
    return suite

def smokeTest():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(TestMeetingRoom("test_1add_meetingroom"))
    # 批量添加多个测试用例，需要使用loader
    alltest = loader.loadTestsFromTestCase(TestMeetingRoomDDT)
    suite.addTests(alltest)
    return suite

if __name__ == '__main__':
    runner = BeautifulReport(smokeTest())
    runner.report(description='企业微信api测试', report_dir='reports')
