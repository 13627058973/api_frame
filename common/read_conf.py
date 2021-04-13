# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-13 下午 16:03
@project : api_frame
@Author  : xhb
@Site    : 
@File    : read_conf.py
@Software: PyCharm Community Edition
"""

import configparser
from common.project_path import *


cf = configparser.ConfigParser()
cf.read(CONF_PATH)
# sheet_file = cf.get("file", "file_path")
# sheet_name = cf.get("file", "sheet_name")
case = cf.get("mode", "case_data")
# print(eval(case), type(eval(case)))