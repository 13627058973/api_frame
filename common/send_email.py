# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-02-21 上午 9:11
@project : api_frame
@Author  : xhb
@Site    : 
@File    : send_email.py
@Software: PyCharm Community Edition
"""

import yagmail


class SendMail:

    subject = "python"  # 主题
    sender = "1269357308@qq.com"   # 发送人账号
    pwd = "qvljnelbrvgjhabe"  # 密码
    port = 465   # 端口号
    smtp_server = 'smtp.qq.com'  # 发送服务器
    contents = "python接口框架"  # 邮箱正文
    receiver = ['1269357308@qq.com']  # 接收人的QQ
    # '953561304@qq.com',

    # 发送邮件
    def send_mail(self, email_path):
        # 连接邮件服务器
        yag = yagmail.SMTP(self.sender, self.pwd, self.smtp_server, self.port)
        # 发送邮件
        yag.send(self.receiver, self.subject, self.contents, email_path)
        # 关闭邮件
        yag.close()


if __name__ == '__main__':
    SendMail().send_mail(r"D:\api_frame\result\report_html\2021-02-20.report.html")



