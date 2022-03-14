# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-20 下午 13:49
@project : api_frame
@Author  : xhb
@Site    : 
@File    : test_login.py
@Software: PyCharm Community Edition
"""
import time, os
import pytest
from common.logger import MyLog
from common.project_path import *
from common.http_request import HttpRequest as HR

data_info = [{"data": {"username": "xhb_user","password": "xhb123..A"},
              "title": "正常登陆", "method":"post", "expect": 0},
             {"data":{"username": "xhb_user","password": "xhb123..A"},
              "title": "账号错误", "method":"post", "expect": 500},
             {"data":{"username": "xhb_user","password": "xhb123..A"},
              "title": "密码错误", "method":"post", "expect": 500},
             {"data":{"username": "xhb_user","password": "xhb123..A"},
              "title": "密码为空", "method":"post", "expect": 500},
             {"data":{"username": "xhb_user","password": "xhb123..A"},
              "title": "账号为空", "method":"post", "expect": 500}]

url = "http://121.196.225.143/prod-api/login"


# 清除日志文件
# @pytest.fixture()
# def clear_info():
#     new = time.strftime("%Y-%m-%d")  # 获取到了当天的时间
#     log_path = LOG_PATH + "/" + new + ".log"
#     if log_path:
#         os.remove(log_path)
#     else:
#         print("今天第一次生成日志")


class TestCase:

    # @pytest.mark.usefixtures("clear_info")
    @pytest.mark.usefixtures("session_fixture")
    @pytest.mark.usefixtures("class_fixture")
    @pytest.mark.usefixtures("my_function")
    @pytest.mark.parametrize("data", data_info)
    def test_case(self, data):
        res = HR().http_request(data["method"], url, data["data"])
        print(res, 111)