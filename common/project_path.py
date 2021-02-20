# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-20 上午 10:07
@project : api_frame
@Author  : xhb
@Site    : 
@File    : project_path.py
@Software: PyCharm Community Edition
"""
import os

# 获取项目的路径
BASH_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志的路径
LOG_PATH = os.path.join(BASH_PATH + r"\result\log")
# 截图的路径
IMAGE_PATH = os.path.join(BASH_PATH, r"\result\image")
# 报告的路径
REPORT_PATH = os.path.join(BASH_PATH, r"\result\report_html")