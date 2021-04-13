# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-13 下午 14:06
@project : api_frame
@Author  : xhb
@Site    : 
@File    : aa.py
@Software: PyCharm Community Edition
"""

import unittest


class TestMoth(unittest.TestCase):

    def test_add(self):
        print("1")

    def test_sum(self):
        print("sum".format(1))

    def test_minus(self):
        print("-1")


if __name__ == '__main__':
    unittest.main()