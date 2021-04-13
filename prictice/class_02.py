# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-03 下午 14:28
@project : api_frame
@Author  : xhb
@Site    : 
@File    : class_02.py
@Software: PyCharm Community Edition
"""
import requests


login_url = "http://47.114.62.29:9404/api/api/auth/login"
data = {"isApp": "false","usernameOrPhone":"aa1234","password":"123456","rememberMe":"true"}

url = "http://47.114.62.29:9404/api/region-file/upload/1"
file = {
    "file": ("111.jpg", open(r"G:\111.jpg", "rb"), "image/jpeg")
}

s = requests.session()
login_res = s.post(login_url, json=data)

file_res = s.post(url, files=file)
print(file_res.text)
