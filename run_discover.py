# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-13 上午 11:56
@project : api_frame
@Author  : xhb
@Site    : 
@File    : run_discover.py
@Software: PyCharm Community Edition
"""
import unittest
import HTMLTestRunnerCN


case = r"D:\api_frame\case\Bayonet"
file = r"D:\api_frame\result\report_html"

testcase = unittest.TestSuite()

discover = unittest.defaultTestLoader.discover(".")

# discover 加载的用例循环加入测试套件中
for test_suit in discover:
    for test_case in test_suit:
        testcase.addTests(test_case)

runner = unittest.TextTestRunner()
runner.run(discover)


