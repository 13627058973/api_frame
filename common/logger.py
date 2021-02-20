# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-20 上午 9:02
@project : api_frame
@Author  : xhb
@Site    : 
@File    : logger.py
@Software: PyCharm Community Edition
"""
import logging
import time
from common.project_path import *


class Mylog:

    def __init__(self, log_name):
        self.log_name = log_name

    def my_log(self, msg, level):
        # 1，日志收集器（定义日志名称，级别，输出格式）
        logger = logging.getLogger(self.log_name)
        logger.setLevel("DEBUG")
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")

        # 2，日志输出器（控制台，指定文件）
        ch = logging.StreamHandler()  # 渠道是指定输出到工作台
        ch.setLevel("DEBUG")  # 只输出info以上级别
        ch.setFormatter(formatter)

        new = time.strftime("%Y-%m-%d")  # 获取到了当天的时间
        log_path = LOG_PATH + "/" + new + ".log"

        fh = logging.FileHandler(log_path, encoding="utf-8")  # 日志存放的地方
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        # 对接
        logger.addHandler(ch)
        logger.addHandler(fh)

        if level == "DEBUG":
            logger.debug(msg)

        if level == "INFO":
            logger.info(msg)

        if level == "WARNING":
            logger.warning(msg)

        if level == "ERROR":
            logger.error(msg)

        if level == "CRITICAL":
            logger.critical(msg)

        # 日志输出完毕后，要移除Handler,否则会导致日志重复
        logger.removeHandler(ch)
        logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")


if __name__ == '__main__':
    log = Mylog("root")
    log.info("我是个好人")




