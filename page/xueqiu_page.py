#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: xueqiu_page.py
# 说   明: 
# 创建时间: 2019/12/8 15:35
'''
from common.base_page import BasePage


class SearchPage(BasePage):
    _search_loc = ("id", "com.xueqiu.android:id/home_search")
    _search_input_loc = ("id", "com.xueqiu.android:id/search_input_text")
    _name_loc = ("id", "com.xueqiu.android:id/name")
    _price_loc = ("id", "com.xueqiu.android:id/current_price")

    def search(self, keyword):
        self.click(self._search_loc)
        self.send_keys(self._search_input_loc, keyword)
        while True:
            if self.find_element(self._name_loc, status=False):
                self.clicks(self._name_loc, 0)
                break
            else:
                self.click(self._search_input_loc)
        return self

    def get_current_price(self):
        return float(self.get_text(self._price_loc))
