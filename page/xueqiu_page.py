#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: xueqiu_page.py
# 说   明: 
# 创建时间: 2019/12/8 15:35
'''

from common.basics import Crazy


class XueQiuPage(Crazy):
    skip_btn_loc = ("id", "tv_skip")

    def element_skip_btn(self):
        return self.find_element(self.skip_btn_loc)

    def click_skip_btn(self):
        self.click(self.skip_btn_loc)

    search_btn_loc = ("id", "tv_search")

    def element_search_btn(self):
        return self.find_element(self.search_btn_loc)

    def click_search_btn_loc(self):
        self.click(self.search_btn_loc)

    search_input_text_loc = ("id", "search_input_text")

    def input_search_input_text(self, text):
        self.send_keys(self.search_input_text_loc, text)

    def click_search_input_text(self):
        self.click(self.search_input_text_loc)

    name_btn_loc = ("id", "name")

    def element_name_btn(self):
        return self.find_element(self.name_btn_loc)

    def click_name_btn(self):
        self.click(self.name_btn_loc)

    price_text_loc = ("id", "current_price")

    def element_price(self):
        return self.find_element(self.price_text_loc)

    deal_btn_loc = ("xpath", "//android.widget.TabWidget[@index='0']/android.widget.RelativeLayout")

    def element_deal_btn(self):
        return self.find_elements(self.deal_btn_loc)