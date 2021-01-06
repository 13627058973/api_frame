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
import json
from common.http_request import HttpRequest as HR

test_data = [{"data":{"isApp": "false", "usernameOrPhone": "admin", "password": "123456", "rememberMe": "true"},
              "title": "正常登陆", "method":"post", "expect": 0},
             {"data":{"isApp": "false", "usernameOrPhone": "admin11", "password": "123456", "rememberMe": "true"},
              "title": "账号错误", "method":"post", "expect": 5001},
             {"data":{"isApp": "false", "usernameOrPhone": "admin", "password": "12345678", "rememberMe": "true"},
              "title": "密码错误", "method":"post", "expect": 5001},
             {"data":{"isApp": "false", "usernameOrPhone": "admin", "password": "", "rememberMe": "true"},
              "title": "密码为空", "method":"post", "expect": 1000},
             {"data":{"isApp": "false", "usernameOrPhone": "", "password": "12345678", "rememberMe": "true"},
              "title": "账号为空", "method":"post", "expect": 1000}]


def run():
    login_url = "http://47.114.59.169:8088/api/api/auth/login"
    for item_data in test_data:
        print("正在测试的用例是{}".format(item_data["title"]))
        res = HR().http_request(login_url, item_data["data"], item_data["method"], "json")
        print("请求的结果是：", res.text)


run()