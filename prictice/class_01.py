# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-03-17 下午 15:28
@project : api_frame
@Author  : xhb
@Site    : 
@File    : class_01.py
@Software: PyCharm Community Edition
"""
# from common.read_conf import *
# from openpyxl import load_workbook
#
# # print()
# wb = load_workbook(sheet_file)
# mode = eval(case)
# for key in mode:
#     sheet = wb[key]
#     if mode[key] == "all":
#         print("哇哈哈矿泉水")
#     else:
#         for case_id in mode[key]:
#             print(case_id)
#
# a = "python"
# print(a.find("1"))
# if a.find("o") == 1:
#     print("hello")
import requests


class File:

    def __init__(self):
        pass

    def http_file(self):
        url = "http://47.114.62.29:9404/api/region-file/upload/1"
        token = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI1NDM4Iiwic3ViIjoiYWExMjM0IiwiaWF0IjoxNjE2NjQwNTU0fQ" \
                ".ainsVUO79wpzVMycbx32cZXkSNm71UQbtkfnM5Wi_Zs"

        header = {"token": token}

        file = {
            "file": ("111.jpg", open(r"G:\111.jpg", "rb"), "image/jpeg")
        }

        file1 = {
            'file': open(r'G:\111.jpg', 'rb'),  # => 用name指定文件
            'Content-Disposition': 'form-data',
            'Content-Type': 'image/jpeg',
            'filename': '111.jpg'
        }

        res = requests.post(url, files=file, headers=header)
        print(res.text)


if __name__ == '__main__':
    File().http_file()