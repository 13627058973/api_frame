# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-23 上午 11:43
@project : api_frame
@Author  : xhb
@Site    : 
@File    : header_request.py
@Software: PyCharm Community Edition
"""
import requests
import json

login_url = "http://116.62.154.79:9012/api/api/auth/login"
login_data = {
    "usernameOrPhone": "admin",
    "password": "123456",
    "rememberMe": "true"
}
header = {"Content-Type": "application/json;charset=UTF-8 "}
login_res = requests.post(login_url, data=json.dumps(login_data), headers=header)
token = login_res.json()["data"]["token"]
print(token)
data = {"pageSize": 100, "currentPage": 1, "type": 1, "status": "", "title": "", "readStatus": ""}
url = "http://116.62.154.79:9012/api/information/findUserInfo"
header = {"token": token}

res = requests.post(url, json=data, headers=header)
print(res.text)