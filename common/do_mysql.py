# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-05-24  09:26
@project : api_frame
@Author  : xhb
@Site    : 
@File    : do_mysql.py
@Software: PyCharm Community Edition
"""
from pymysql import *
from common.project_path import *
from common.read_conf import ReadConfig


class DoMysql:

    @staticmethod
    def do_mysql(sql, start):  # statement sql语句
        # 连接数据库
        mysql_info = eval(ReadConfig.read_config(CONF_PATH, "DB", "mysql_info"))
        db = Connection(**mysql_info)
        # 创建一个游标
        cursor = db.cursor()

        # 执行语句
        cursor.execute(sql)

        # 取结果
        if start == 1:
            res = cursor.fetchone()  # 元祖  针对一条数据
        else:
            res = cursor.fetchall()  # 列表  针对多条数据
        # 关闭游标
        cursor.close()
        # 关闭连接
        db.close()


if __name__ == '__main__':
    DoMysql.do_mysql("select * from bs_role where role_name = '维修人'")
