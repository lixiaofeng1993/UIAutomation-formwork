#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/6 10:32
# @Author  : lixiaofeng
# @Site    : 
# @File    : settings.py
# @Software: PyCharm

import os, platform, time

pattern = '/' if platform.system() != 'Windows' else '\\'
file_not_exists_error = "文件路径：{} 不存在，请检查并添加."
element_not_click_error = "元素定位异常，无法点击."
element_not_input_error = "元素定位异常，无法输入."


class CustomException(Exception):
    """自定义异常类"""

    def __init__(self, error):
        self.error = error

    def __str__(self):
        exception_msg = "Message: %s\n" % self.error
        return exception_msg


class NoTextFountException(CustomException):
    """
    没有发现文本异常
    """
    pass


def check_dir(path):
    """
    检查目录是否存在，不存在则创建目录
    :param path:
    :return: path
    """
    if not os.path.exists(path):
        os.mkdir(path)
    return path


def check_file(path):
    """
    检查文件是否存在，不存在则抛出错误
    :param path:
    :return:
    """
    if not os.path.exists(path):
        return False
    else:
        return path


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

driver_path = check_dir(os.path.join(BASE_DIR, "driver"))  # 驱动文件路径

data_path = check_dir(os.path.join(BASE_DIR, "data"))  # 上传文件路径
data_img_path = check_dir(os.path.join(data_path, "img"))  # 上传图片路径
data_txt_path = check_dir(os.path.join(data_path, "txt" + pattern + "city.txt"))  # txt文件路径

config_path = check_dir(os.path.join(BASE_DIR, "config"))  # 配置文件目录
cfg_path = check_file(os.path.join(config_path, "cfg.ini"))

case_path = check_dir(os.path.join(BASE_DIR, "testcase"))  # case目录

report_path = check_dir(os.path.join(BASE_DIR, "report"))  # 报告路径

img_path = check_dir(os.path.abspath('img/' if platform.system() != 'Windows' else '\\img'))  # 截图路径

log_path = check_dir(os.path.join(BASE_DIR, "logs"))  # 日志路径

hour = time.strftime('%Y-%m-%d')
now = time.strftime('%Y-%m-%d %H-%M-%S')

if __name__ == '__main__':
    print(data_txt_path)
