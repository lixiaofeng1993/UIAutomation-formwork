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

    helper_btn_loc = ("xpath", "//android.widget.TextView[@text='小程序助手' and @resource-id='com.tencent.mm:id/cg']")

    def element_helper_btn(self):
        return self.find_element(self.helper_btn_loc, status=False)

    test_small_program_name_loc = ("xpath", "//android.widget.TextView[@text='包妈优选']")

    def elements_test_small_program_name(self):
        return self.find_elements(self.test_small_program_name_loc)

    delete_btn_loc = ("xpath", "//android.widget.TextView[@text='删除']")

    def click_delete_btn(self):
        self.click(self.delete_btn_loc)
