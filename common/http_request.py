# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-06 上午 10:40
@project : api_frame
@Author  : xhb
@Site    : 
@File    : http_request.py
@Software: PyCharm Community Edition
"""
import json
import requests


class HttpRequest(object):
    """封装请求方式"""
    def http_request(self, url, data, method, content_type):
        try:
            if method.upper() == "GET":
                res = requests.get(url, params=data)
            # 如果请求方式是 post，且请求的数据是表单格式的数据
            elif method.upper() == "POST" and content_type == "form":
                res = requests.post(url, data=data)
            # 如果请求的方式是 json,且请求的数据是json格式
            elif method.upper() == "POST" and content_type == "json":
                res = requests.post(url, json=data)

            else:
                print("请求方式错误")
        except Exception as e:
            print("请求方式的代码出错了{}".format(e))
            raise e

        return res


if __name__ == '__main__':
    login_url = "http://47.114.59.169:8088/api/api/auth/login"
    login_data = {
        "isApp": "false",
        "usernameOrPhone": "admin",
        "password": "123456",
        "rememberMe": "true"
    }
    HR = HttpRequest()
    HR.http_request(login_url, login_data, "post", "json")