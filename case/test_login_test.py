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
from hamcrest import *

import datetime, time
from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *
from common.basics import open_app
from page.xueqiu_page import XueQiuPage


class TestDemo:
    search_data = yaml.safe_load(open("search.yaml", "r"))
    print(search_data)

    # @classmethod
    def setup_class(self):
        self.driver = open_app()
        self.login = XueQiuPage(self.driver)

    # @pytest.mark.parametrize("keyword, expected_price", [
    #     ("jingdong", 10),
    #     ("alibaba", 100),
    #     ("pdd", 20)
    # ])
    # def test_search(self, keyword, expected_price):
    #     if self.login.element_skip_btn():
    #         self.login.click_skip_btn()
    #     if self.login.element_search_btn():
    #         self.login.click_search_btn_loc()
    #     self.login.input_search_input_text(keyword)
    #     if not self.login.element_name_btn():
    #         self.login.click_search_input_text()
    #     self.login.click_name_btn()
    #
    #     price = self.login.element_price()
    #
    #     assert float(price.text) > expected_price
    #     assert "price" in price.get_attribute("resource-id")
    #     assert_that(price.get_attribute("package"), equal_to("com.xueqiu.android"))

    # @pytest.mark.parametrize("keyword, expected_price", search_data)
    # def test_search(self):
    #     TestCase("testcase.yaml").run(self.login)

    def test_webview(self):
        time.sleep(5)
        self.login.element_deal_btn()[-2].click()
        time.sleep(5)
        for i in range(5):
            time.sleep(1)
            print(self.driver.contexts)

    # @classmethod
    def teardown_class(self):
        self.driver.quit()


# class TestCase:
#     def __init__(self, path):
#         with open(path, "r") as f:
#             self.steps = yaml.safe_load(f)
#             print(self.steps)
#
#     def run(self, driver):
#         for step in self.steps:
#             if isinstance(step, dict):
#                 if "id" in step.keys():
#                     time.sleep(3)
#                     elelment = driver.find_element(("id", step["id"]))
#                 elif "xpath" in step.keys():
#                     elelment = driver.find_element(("xpath", step["xpath"]))
#                 else:
#                     print(step.keys())
#
#                 if "input" in step.keys():
#                     elelment.send_keys(step["input"])
#                 elif "get" in step.keys():
#                     text = elelment.get_attribute(step["get"])
#                     print(text)
#                 elif "eq" in step.keys():
#                     assert float(text) >  step["eq"]
#                 else:
#                     elelment.click()
