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

path_file = r"D:\api_frame\config\config.ini"


cf = configparser.ConfigParser()
cf.read(path_file)
sheet_file = cf.get("file", "file_path")
sheet_name = cf.get("file", "sheet_name")