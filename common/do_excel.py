# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-07 下午 15:14
@project : api_frame
@Author  : xhb
@Site    : 
@File    : do_excel.py
@Software: PyCharm Community Edition
"""

from openpyxl import load_workbook
from common.read_conf import *


class DoExcel:

    def __init__(self, file, sheet_login):
        self.file = file
        self.sheet_login = sheet_login

    def get_data(self):  # 获取表单的数据
        wb = load_workbook(self.file)
        sheet = wb[self.sheet_login]
        data = []
        for i in range(2, sheet.max_row + 1):
            item = {}
            item["case_id"] = sheet.cell(i, 1).value
            item["url"] = sheet.cell(i, 2).value
            item["data"] = sheet.cell(i, 3).value
            item["title"] = sheet.cell(i, 4).value
            item["method"] = sheet.cell(i, 5).value
            item["type"] = sheet.cell(i, 6).value
            item["ExpectResult"] = sheet.cell(i, 7).value
            # item["ActualResult"] = sheet.cell(i, 8).value
            # item["TestResult"] = sheet.cell(i, 9).value
            data.append(item)
        return data

    def write_back(self, row, columns, value):  # 写入文件
        wb = load_workbook(self.file)
        sheet = wb[self.sheet_login]

        # 在表格中赋值
        sheet.cell(row, columns).value = value

        # 保存文件
        wb.save(self.file)


if __name__ == '__main__':
    test_data = DoExcel(sheet_file, sheet_name).get_data()
    DoExcel(sheet_file, sheet_name).write_back(2, 8, "1111")
    for item in test_data:
        print(item)

