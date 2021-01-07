# !/usr/bin/env python
# encoding: utf-8
"""
@Time : 2021-01-07 上午 11:34
@project : api_frame
@Author  : xhb
@Site    : 
@File    : get_cookies.py
@Software: PyCharm Community Edition
"""

"""
reflect(反射)
"""


class GetCookie:

    cookie = None
    a = 111


if __name__ == '__main__':

    res = hasattr(GetCookie, "cookie")  # 判断是否存在这个参数属性
    print(res)
    setattr(GetCookie, "cookie", "222")  # 设置该参数的属性值
    res = getattr(GetCookie, "a")  # 获取该参数的value值
    print(res)
    delattr(GetCookie, "a")  # 删除这个参数属性
    res = hasattr(GetCookie, "a")
    print(res)