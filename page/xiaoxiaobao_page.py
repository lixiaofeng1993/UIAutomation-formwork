#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/9 17:29
# @Author  : lixiaofeng
# @Site    : 
# @File    : xiaoxiaobao_page.py
# @Software: PyCharm

from common.basics import Crazy


class XiaoxiaobaoPage(Crazy):
    find_page_loc = ("id", "dkb")

    def clicks_find_page(self, n):
        self.clicks(self.find_page_loc, n)

    small_program_loc = ("xpath", "//android.widget.TextView[@text='小程序']")

    def click_small_program(self):
        self.click(self.small_program_loc)

    helper_btn_loc = ("xpath", "//android.widget.TextView[@text='小程序助手']")

    def element_helper_btn(self):
        return self.find_element(self.helper_btn_loc, status=False)

    def click_helper_btn(self):
        self.click(self.helper_btn_loc)

    test_small_program_name_loc = ("xpath", "//android.widget.TextView[@text='包妈优选']")

    def elements_test_small_program_name(self):
        return self.find_elements(self.test_small_program_name_loc, status=False)

    def element_test_small_program_name(self):
        return self.find_element(self.test_small_program_name_loc, status=False)

    delete_btn_loc = ("xpath", "//android.widget.TextView[@text='删除']")

    def click_delete_btn(self):
        self.click(self.delete_btn_loc)

    drop_delete_btn_loc = ("xpath", "//android.widget.TextView[@text='拖动到此处删除']")

    def element_drop_delete_btn(self):
        return self.find_element(self.drop_delete_btn_loc)

    my_small_program_loc = ("xpath", "//android.widget.TextView[@text='小程序助手']")

    def elements_my_small_program(self):
        return self.find_elements(self.my_small_program_loc)
