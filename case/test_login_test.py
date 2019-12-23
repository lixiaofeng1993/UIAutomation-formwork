#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: test_login.py
# 说   明: 
# 创建时间: 2019/11/16 19:18
'''
import time
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.basics import open_app
import pytest


class TestDemo:
    # search_data = yaml.safe_load(open("search.yaml", "r", encoding="utf-8"))
    # print(search_data)

    def setup(self):
        self.driver = open_app(html=False)
        self.driver.implicitly_wait(10)
        # self.__update()

    # def __update(self):
    #     if self.driver.find_element_by_id("com.xueqiu.android:id/update_id_ok"):
    #         self.driver.find_element_by_id("com.xueqiu.android:id/image_cancel").click()

    # @pytest.mark.parametrize("keyword, expected_price", [
    #     ("拼多多", 20),
    #     ("阿里巴巴", 200),
    #     ("京东", 10),
    # ])
    # def test_search(self, keyword, expected_price):
    #     self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
    #     search_element = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    #     search_element.click()
    #     search_element.send_keys(keyword)
    #     if self.driver.find_elements_by_id("com.xueqiu.android:id/name"):
    #         self.driver.find_elements_by_id("com.xueqiu.android:id/name")[0].click()
    #         price = self.driver.find_element_by_id("com.xueqiu.android:id/current_price")
    #         assert float(price.text) > expected_price

    # @pytest.mark.parametrize("keyword, expected_price", search_data)
    # def test_search(self, keyword, expected_price):

    # self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
    # search_element = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
    # search_element.click()
    # search_element.send_keys(keyword)
    # if self.driver.find_elements_by_id("com.xueqiu.android:id/name"):
    #     self.driver.find_elements_by_id("com.xueqiu.android:id/name")[0].click()
    #     price = self.driver.find_element_by_id("com.xueqiu.android:id/current_price")
    #     assert float(price.text) > expected_price

    def test_yinqing(self):
        Case("testcase.yaml").run(self.driver)

    # def test_webview(self):
    #     time.sleep(3)
    #     element = self.driver.find_elements_by_xpath("//android.widget.TabWidget[@index='0']/android.widget.RelativeLayout")
    #     element[-2].click()
    #     for i in range(5):
    #         print(self.driver.contexts)
    #     # self.driver.switch_to.context(self.driver.contexts.last)
    #     self.driver.find_element_by_xpath("//android.view.View[@text='A股开户']").click()
    #     # self.driver.find_element_by_xpath("//android.widget.TextView[@text='更多券商']").click()
    #     WebDriverWait(self.driver, 20).until(
    #         expected_conditions.visibility_of_element_located(("xpath", "//android.view.View[@text='  ']")))
    #     WebDriverWait(self.driver, 20).until(expected_conditions.visibility_of_element_located(
    #         ("xpath", "//android.view.View[@index='1']/android.widget.EditText")))  # NAF 为 true
    #     self.driver.find_element_by_xpath("//android.view.View[@text='  ']").click()
    #     self.driver.find_element_by_xpath("//android.view.View[@index='1']/android.widget.EditText").send_keys(
    #         "18701137212")

    # def test_chrome(self):
    #     self.driver.get("http://www.easytest.xyz/")
    #     # self.driver.get("http://testerhome.com")
    #
    #     for i in range(5):
    #         time.sleep(2)
    #         print(self.driver.contexts)
    #     self.driver.switch_to.context(self.driver.contexts[0])
    #
    #     self.driver.find_element_by_accessibility_id("Close").click()
    #
    #     # self.driver.switch_to.context(self.driver.contexts[-1])
    #     WebDriverWait(self.driver, 20).until(
    #         expected_conditions.visibility_of_element_located(("xpath", "//android.widget.Button[@text='菜单']")))
    #     self.driver.find_element_by_xpath("//android.widget.Button[@text='菜单']").click()
    #     assert self.driver.find_element_by_xpath("//android.widget.Button[@text='菜单']").text == "菜单"

    def teradown(self):
        self.driver.quit()


class Case:
    def __init__(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.steps = yaml.safe_load(f)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element = None
            if isinstance(step, dict):
                if "id" in step.keys():
                    element = driver.find_element_by_id(step.get("id"))
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step.get("xpath"))
                else:
                    print(step.keys())

                if "input" in step.keys():
                    element.send_keys(step.get("input"))
                elif "get" in step.keys():
                    text = element.get_attribute(step.get("get"))
                elif "eq" in step.keys():
                    assert float(text) > float(step.get("eq"))
                else:
                    element.click()
