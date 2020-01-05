#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: test_login_weixin.py
# 说   明: 
# 创建时间: 2020/1/5 14:51
'''
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.weixin_page import LoginWeixin
from common.app import App
import pytest


class TestWin:
    def setup(self):
        self.driver = App.open_app(html=False)

    def test_img(self):
        LoginWeixin(self.driver).login_wecat()
