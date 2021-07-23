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

    @staticmethod
    def http_request(url, data, method):  # 默认请求类型是json类型
        try:
            if method.upper() == "GET":
                result = requests.get(url, params=data)

            elif method.upper() == "POST":
                # 请求方式是json
                # if content_type == "json":
                #     result = requests.post(url, json=data)
                # # 请求方式是表单
                # elif content_type == "form":
                #     result = requests.post(url, data=data)
                result = requests.post(url, data=data, json=json)

            else:
                print("请求方式错误")
        except Exception as e:
            print("请求方式的代码出错了{}".format(e))
            raise e

        return result


if __name__ == '__main__':
    headers = {

    }
    login_url = "http://121.196.225.143/prod-api/system/post"
    login_data = {"postCode": "5",
                  "postName": "软件测1试",
                  "postSort": 5,
                  "status": "0",
                  "remark": "测试账号通用"
                  }
    data = json.dumps(login_data)
    res = requests.post(login_url, json=data)
    print(res.text)
