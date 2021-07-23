# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-06 上午 10:30
@project : api_frame
@Author  : xhb
@Site    :
@File    : run_unittestreport.py
@Software: PyCharm Community Edition
"""

from case.Login.login import TestLogin
from prictice.class_03 import TestBayonet
import unittest
import HTMLTestRunnerCN
import time
from common.send_email import SendMail
from unittestreport import TestRunner
from common.project_path import *


new = time.strftime("%Y-%m-%d")
# 创建一个测试套件
suit = unittest.TestSuite()
# 创建一个用例加载器
loader = unittest.TestLoader()
# 加载用例到测试套件中
suit.addTest(loader.loadTestsFromTestCase(TestLogin))
suit.addTest(loader.loadTestsFromTestCase(TestBayonet))

filename = new + ".report.html"

runner = TestRunner(suit,
                    filename=filename,
                    report_dir=REPORT_PATH,
                    title='测试报告',
                    tester='xhb',
                    desc="出入口项目测试生成的报告",
                    templates=1
                    )

runner.run()
# 发送邮件
# SendMail().send_mail(report_path)

