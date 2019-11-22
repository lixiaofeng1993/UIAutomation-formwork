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
    user_loc = ("id", "user")

    def input_user(self, user):
        self.send_keys(self.user_loc, user)

    password_loc = ("id", "pswd")

    def input_password(self, pwd):
        self.send_keys(self.password_loc, pwd)

    btn_loc = ("id", "btn")

    def click_btn(self):
        self.click(self.btn_loc)

    user_img_loc = ("class name", "dropdown")

    def click_user_img(self):
        self.click(self.user_img_loc)

    blog_loc = ("xpath", "//ul[@class='dropdown-menu']/li[9]/a")

    def click_blog(self):
        self.click(self.blog_loc)

    blog_tag_loc = ("id", "Header1_HeaderTitle")

    def text_blog_tag(self):
        return self.get_text(self.blog_tag_loc)
