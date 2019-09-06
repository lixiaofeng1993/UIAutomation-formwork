#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 11:53
# @Author  : lixiaofeng
# @Site    : 
# @File    : login_page.py
# @Software: PyCharm
from common.basics import Crazy


class LoginPage(Crazy):
    user_loc = ('id', 'username')

    def input_user(self, username):
        self.send_keys(self.user_loc, username)

    password_loc = ('id', 'password')

    def input_password(self, pwd):
        self.send_keys(self.password_loc, pwd)

    login_btn_loc = ('tag name', 'button')

    def click_login_btn(self):
        self.click(self.login_btn_loc)

    check_login_success_loc = ('xpath', '//div[@class="menuContainer___2WW7T"]/div/ul/li/a/span')

    def text_check_login_success(self, n):
        return self.get_texts(self.check_login_success_loc, n)

    tag_loc = ('xpath', '//div[@class="menuContainer___2WW7T"]/div/ul/li')

    def clicks_tag(self, n):
        self.clicks(self.tag_loc, n)

    ant_tag_loc = ('xpath', '//ul[@class="ant-menu ant-menu-sub ant-menu-inline"]/li/a')

    def clicks_ant_tag(self, n):
        self.clicks(self.ant_tag_loc, n)

    add_video_loc = ('xpath', '//div[@class="header___3l9tq"]/span/button')

    def click_add_video(self):
        self.click(self.add_video_loc)

    click_upload_loc = ('xpath', '//form[@class="ant-form ant-form-horizontal"]/div[6]/div[2]/div/span')

    def click_upload(self):
        self.click(self.click_upload_loc)
