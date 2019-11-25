#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: test_login.py
# 说   明: 
# 创建时间: 2019/11/16 19:18
'''

import unittest, time, paramunittest
from BeautifulReport import BeautifulReport
from page.login_page import LoginPage
from common.basics import open_app
from common.logger import Log
from common.settings import img_path
from common.random_upload import uploaded
from common import read_config


@paramunittest.parametrized(
    {'user': '15652708023', 'pwd': 'beijing123456'},
)
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = open_app()
        cls.log = Log()
        cls.login = LoginPage(cls.driver)
        cls.img_path = img_path

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
        if login.element_skip_button():
            login.click_skip_button()
        login.click_search_button()
        login.click_search_text()
        login.input_search_text("alibaba")
        print(self.driver.get_performance_data_types())
        self.driver.find_element_by_android_uiautomator()
        self.driver.get_performance_data("com.xueqiu.android", "batteryinfo", 5)


if __name__ == '__main__':
    unittest.main()
