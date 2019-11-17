#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: login_page.py
# 说   明: 
# 创建时间: 2019/11/16 19:07
'''

from common.basics import Crazy


class LoginPage(Crazy):
    skip_button_loc = ("id", "com.xueqiu.android:id/tv_skip")

    def element_skip_button(self):
        return self.find_element(self.skip_button_loc)

    def click_skip_button(self):
        self.click(self.skip_button_loc)

    search_button_loc = ("id", "com.xueqiu.android:id/tv_search")

    def click_search_button(self):
        self.click(self.search_button_loc)

    search_text_loc = ("id", "com.xueqiu.android:id/search_input_text")

    def click_search_text(self):
        self.click(self.search_text_loc)

    def input_search_text(self, text):
        self.send_keys(self.search_text_loc, text)

    # contains(@text, "文本")
    new_pople_loc = ("xpath", '//*[@resource-id="com.xueqiu.android:id/tag_guide_text" and @text="新手福利"]')

    def element_new_pople(self):
        return self.find_element(self.new_pople_loc)

    shares_search_loc = ("id", "com.xueqiu.android:id/name")

    def click_shares_search(self):
        self.click(self.shares_search_loc)