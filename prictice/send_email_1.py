# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-20 下午 16:56
@project : api_frame
@Author  : xhb
@Site    : 
@File    : send_email_1.py
@Software: PyCharm Community Edition
"""
import yagmail
import os
import time
from common.project_path import *


new = time.strftime("%Y-%m-%d")
#  -----1，跟发件相关的参数------
subject = "pthon"
smtp_server = 'smtp.qq.com'  # 发送服务器
port = 465  # 端口
sender = '1269357308@qq.com'  # 账号
psw = 'qvljnelbrvgjhabe'  # 密码
receiver = ['953561304@qq.com', '1269357308@qq.com']  # 接收人的QQ

# 连接邮箱服务器
yag = yagmail.SMTP(sender, psw, smtp_server, port)

# 邮箱正文
contents = "python接口框架搭建"
# 附件地址
attachments = r"D:\api_frame\result\report_html\2021-02-20.report.html"
print(attachments)
yag.send(receiver, subject, contents, attachments)
yag.close()