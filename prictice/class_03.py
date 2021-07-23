# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-04-07 上午 11:26
@project : api_frame
@Author  : xhb
@Site    :
@File    : class_03.py
@Software: PyCharm Community Edition
"""
import requests
from common.do_excel import DoExcel
from common.project_path import *
import unittest
from ddt import ddt, data
from common.logger import MyLog
from common.get_data import GetCookie
from common.get_token import GetToken

Data = DoExcel(DATA_PATH, "bayonet").get_data()
# if getattr(GetCookie, "token"):
#     token = getattr(GetCookie, 'token')
# else:
#     setattr(GetCookie, "token", GetToken.get_token())

headers = {"token": GetToken.get_token()}


@ddt
class TestBayonet(unittest.TestCase):

    def setUp(self):
        self.BayonetDate = DoExcel(DATA_PATH, "bayonet")
        self.logger = MyLog("root")

    @data(*Data)
    def test_bayonet(self, item):
        self.logger.info("***********************")
        self.logger.info("正在执行的用例是{}".format(item["title"]))
        self.logger.info("请求的数据是：{}".format(item["data"]))
        res = requests.post(item["url"], json=eval(item["data"]), headers=headers)
        self.logger.info("接口返回的结果是{}".format(res.json()))
        try:
            self.assertEqual(item["ExpectResult"], res.json()["message"])
            TestResult = "PASS"  # 如果不报错，测试通过
        except AssertionError as e:
            print("接口错误，错误是{}".format(e))
            TestResult = "Fail"  # 如果报错了，测试不通过
        finally:  # 不管测试结果是否正确，都把结果写入文件
            self.logger.info("*********开始写入结果********")
            self.BayonetDate.write_back(item["case_id"] + 1, 8, str(res.json()["message"]))  # 写入实际结果
            self.BayonetDate.write_back(item["case_id"] + 1, 9, TestResult)  # 写入测试结果
            self.logger.info("*********结束写入数据********")
        # print(res.text)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
