#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/8 17:41
# @Author  : lixiaofeng
# @Site    : 
# @File    : test_operate_manage.py
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
class TestOperateManage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.url = read_config.url
        cls.img_path = img_path

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def setParameters(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(self.img_path, img_name))