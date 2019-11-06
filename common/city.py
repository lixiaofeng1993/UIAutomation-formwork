#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 18:23
# @Author  : lixiaofeng
# @Site    : 
# @File    : city.py
# @Software: PyCharm

from common.settings import data_txt_path

city_list = []
tag_list = ["id", "district_code", "parent_code", "district_name", "level_type"]
with open(data_txt_path, "r", encoding="utf-8") as f:
    res = f.readlines()
    for data in res:
        data_list = data.strip("\n").split("\t")
        data_dict = dict(zip(tag_list, data_list))
        city_list.append(data_dict)

city_name = ""
for city in city_list:
    if city.get("district_code") in ["320000", "320100", "320102"]:
        city_name += city.get("district_name")

print(city_name)