#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/6 11:53
# @Author  : lixiaofeng
# @Site    : 
# @File    : login.py
# @Software: PyCharm
import unittest, time, paramunittest
from BeautifulReport import BeautifulReport
from page.login_page import LoginPage
from common.basics import open_browser
from common.logger import Log
from common.settings import img_path
from common.random_upload import uploaded
from common import read_config


@paramunittest.parametrized(
    {'user': 'root', 'pwd': 'admin'},
)
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    def setParameters(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))

    @BeautifulReport.add_test_img('test_login')
    def test_login(self):
        login = self.login
        login.open(self.url, t='小小包早教后台管理')
        login.input_user(self.user)
        login.input_password(self.pwd)
        login.click_login_btn()
        self.assertEqual(login.text_check_login_success(0), '首页')



        # def test_upload(self):
        #     time.sleep(3)
        #     login = self.login
        #     login.clicks_tag(4)
        #     login.clicks_ant_tag(1)
        #     time.sleep(3)
        #     login.click_add_video()
        #     time.sleep(2)
        #     login.input_img_name('测试图片')
        #     login.click_upload()
        #     uploaded(type=0)
        #
        #     time.sleep(5)
        #     login.click_sure()
        #     time.sleep(2)


if __name__ == '__main__':
    unittest.main()
