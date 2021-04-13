# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-07 下午 13:45
@project : api_frame
@Author  : xhb
@Site    : 
@File    : get_token.py
@Software: PyCharm Community Edition
"""
import requests


class GetToken:
    url = "http://218.244.157.108:9002/api/api/auth/login"
    data = {"isApp": "false", "usernameOrPhone": "admin", "password": "123456", "rememberMe": "true"}

    @classmethod
    def get_token(cls):
        token = requests.post(cls.url, json=cls.data).json()["data"]["token"]
        return token


if __name__ == '__main__':
    print(GetToken.get_token())