#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/22 18:16
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_easytest_login.py
# @Software: PyCharm


import unittest, time, paramunittest
from BeautifulReport import BeautifulReport
from page.easytest_login_page import LoginPage
from common.basics import open_browser
from common.logger import Log
from common.settings import img_path
from common.random_upload import uploaded
from common import read_config


@paramunittest.parametrized(
    {'user': 'lixiaofeng', 'pwd': 'fengzi802300'},
)
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.img_path = img_path
        cls.url = read_config.url

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setParameters(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    def test_login(self):
        login = self.login
        login.open(self.url, t="login")
        login.input_user(self.user)
        login.input_password(self.pwd)
        login.click_btn()
        self.assertEqual(login.get_title(), "EasyTest-自动化测试平台")
        self.log.info("登录成功！")
        print(login.current_window_handle())
        login.click_user_img()
        login.click_blog()
        print(login.current_window_handle())
        login.switch_window_handle(1)
        print(login.text_blog_tag())


if __name__ == '__main__':
    unittest.main()
