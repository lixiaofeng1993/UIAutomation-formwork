#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 18:57
# @Author  : lixiaofeng
# @Site    : 
# @File    : 1test.py
# @Software: PyCharm


from wxpy import *

bot = Bot(cache_path=True)  # 注意手机确认登录

friends = bot.friends()
