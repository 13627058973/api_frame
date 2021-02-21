# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-06 上午 10:30
@project : api_frame
@Author  : xhb
@Site    : 
@File    : run.py
@Software: PyCharm Community Edition
"""
from case.Login.login import TestLogin
import unittest
import HTMLTestRunnerCN
import time
from common.send_email import SendMail
from common.project_path import *

new = time.strftime("%Y-%m-%d")
# 创建一个测试套件
suit = unittest.TestSuite()
# 创建一个用例加载器
loader = unittest.TestLoader()
# 加载用例到测试套件中
suit.addTest(loader.loadTestsFromTestCase(TestLogin))

report_path = os.path.join(REPORT_PATH, new + ".report.html")
with open(report_path, "wb") as file:
    runner = HTMLTestRunnerCN.HTMLTestReportCN(file,
                                               verbosity=2,
                                               title="登录测试",
                                               description="框架搭建",
                                               tester="xhb"
                                               )

    runner.run(suit)
# 发送邮件
SendMail().send_mail(report_path)






