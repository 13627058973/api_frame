# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-13 下午 16:03
@project : api_frame
@Author  : xhb
@Site    : 
@File    : read_conf.py
@Software: PyCharm Community Edition
"""

import configparser
from common.project_path import *


class ReadConfig:

    """读取配置文件的数据"""
    @staticmethod
    def read_config(conf_path, section, option):
        """
        :param conf_path: 配置文件的路径/地址
        :param section: 配置文件的段
        :param option: 配置文件段里面的选项/数据
        :return:
        """
        cf = configparser.ConfigParser()
        cf.read(conf_path)
        case = cf.get(section, option)
        return case


if __name__ == '__main__':
    print(ReadConfig.read_config(CONF_PATH, "MODE", "mode"))


