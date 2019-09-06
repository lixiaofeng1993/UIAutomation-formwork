#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/3 18:57
# @Author  : lixiaofeng
# @Site    : 
# @File    : 1test.py
# @Software: PyCharm
# import random
#
# text = random.uniform(1, 10)
#
# print(round(text, 2))

# !/usr/bin/env python
# -*- coding:utf-8 -*-

# from page_objects import PageElement,PageObject
# from selenium import webdriver
# from common.basics import open_browser
#
# class LoginPage(PageObject):
#
#     username = PageElement(id_='username')
#     password = PageElement(id_='password')
#     login_button = PageElement(tag_name='button')
#
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome(executable_path=r'D:\UIAutomation\driver\chromedriver.exe')
#     page = LoginPage(driver, root_uri='https://dev.edu.xxbmm.com/zh')
#     page.get('/login')
#     page.username = 'root'
#     page.password = 'admin'
#     page.login_button.click()
#


class Boos:

    def __init__(self):
        self.money = 10000
        self.goods = 0
        self.staff = 1

    def sell_goods(self):
        return self.goods * 10

class Employee(Boos):

    def __init__(self):
        Boos.__init__(self)
        self.attr = 300

    def boos_money(self):
        for i in range(1, 121):
            if i % 12 == 1 and i >= 12:
                self.staff += 1
                if self.attr < 500:
                    self.attr += 50
            self.goods = self.attr * self.staff
            self.money += self.sell_goods() - self.staff * 2000
        print(self.money)

if __name__ == '__main__':
    Employee().boos_money()