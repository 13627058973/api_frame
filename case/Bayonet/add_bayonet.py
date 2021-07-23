# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-03 下午 15:58
@project : api_frame
@Author  : xhb
@Site    : 
@File    : add_bayonet.py
@Software: PyCharm Community Edition
"""
from common.http_request import HttpRequest as hr
import unittest
import requests

"""添加卡口测试用例"""
token = None
"""
self.assertEqual("预期结果", "实际结果")
"""


class TestBayonet(unittest.TestCase):

    def setUp(self):  # 登录获取token
        global token
        url = "http://218.244.157.108:9002/api/api/auth/login"
        data = {"isApp": "false", "usernameOrPhone": "admin", "password": "123456", "rememberMe": "true"}
        token = requests.post(url, json=data).json()["data"]["token"]

    def test_normal(self):  # 正常添加卡口
        url = "http://218.244.157.108:9002/api/bs-bayonet/addBayonet"
        data = {"longitude": "115.89230", "latitude": "28.676945",
                "bayonetName": "大门", "coords": "115.89230,28.676945",
                "spatialCoordinateType": "BD-09", "territoryId": "7",
                "borderGps": "115.892771,28.677151|115.893831,28.676937",
                "boundary": [["115.892771,28.677151"], ["115.893831,28.676937"]]}
        header = {"token": globals()["token"]}
        result = requests.post(url, json=data, headers=header)
        self.assertEqual("添加成功", result.json()["message"])

    def test_repetition(self):  # 添加重复的卡口
        pass


if __name__ == '__main__':
    unittest.main()
