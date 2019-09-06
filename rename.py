#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 11:40
# @Author  : lixiaofeng
# @Site    : 
# @File    : rename.py
# @Software: PyCharm

import os

type = input('选择要改变的类型<1 case name 加 1；2 case name 去掉1>：')
if type == '1':
    make = input('case name 的共同特征：')
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'case')
py_path_list = os.listdir(path)
for i in py_path_list:
    py_path = os.path.join(path, i)
    if type == '1':
        if make in i:
            os.rename(py_path, os.path.join(path, '1' + os.path.basename(py_path)))
    if type == '2':
        if '1' in os.path.basename(py_path):
            os.rename(py_path, os.path.join(path, os.path.basename(py_path).strip('1')))
