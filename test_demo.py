# -*- coding: utf-8 -*-
# Time: 2022/4/26 18:03
# Author: Gavin

import requests
from core.basecase import BaseCase
import unittest


class TestDemo(BaseCase):

    def test_01(self):
        print('test_01: '.format(self.token))

    def test_02(self):
        print('test_02: '.format(self.token))


if __name__ == '__main__':
    unittest.main(verbosity=2)
