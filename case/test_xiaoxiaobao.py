#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 17:28
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_xiaoxiaobao.py
# @Software: PyCharm

import pytest
import time

from page.xiaoxiaobao_page import XiaoxiaobaoPage
from common.basics import open_app


class TestXiaoxiaobao:
    def setup(self):
        self.driver = open_app()
        self.xiao = XiaoxiaobaoPage(self.driver)

    def test_login(self):
        self.xiao.clicks_find_page(2)
        self.xiao.click_small_program()
        self.find_program(self.xiao.elements_test_small_program_name(), status=1)
        self.find_program(self.xiao.element_helper_btn())

        time.sleep(5)

    def find_program(self, element, status=0):
        while True:
            if element:
                if status == 1:
                    for ele in element:
                        self.xiao.long_press(ele)
                        self.xiao.click_delete_btn()
                elif status == 0:
                    element.click()
                break
            else:
                self.xiao.swipeUp()
