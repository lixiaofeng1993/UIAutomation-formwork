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
        """微信小程序"""
        """长按删除"""
        self.xiao.clicks_find_page(2)
        self.xiao.click_small_program()
        self.find_program(self.xiao.elements_test_small_program_name(), status=1)
        self.find_program(self.xiao.element_helper_btn())
        """长按拖拽"""
        self.xiao.swipeDown()
        element = self.xiao.element_test_small_program_name()
        element_obj = self.xiao.long_press(element)
        element1 = self.xiao.element_drop_delete_btn()
        self.xiao.unknown_drag_and_drop(element_obj, element1)
        self.xiao.click_helper_btn()
        """长按拖拽"""
        element = self.xiao.element_helper_btn()
        element1 = self.xiao.elements_my_small_program()[-1]
        self.xiao.drag_and_drop(element, element1)

    def find_program(self, element, status=0):
        """长按，删除"""
        i = 0
        while True:
            i += 1
            if element:
                if status == 1:
                    for ele in element:
                        self.xiao.long_press(ele)
                        self.xiao.click_delete_btn()
                elif status == 0:
                    element.click()
                break
            if i >= 3:
                break
            else:
                self.xiao.swipeUp()

    def teardown(self):
        self.driver.quit()
