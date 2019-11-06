#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 10:03
# @Author  : lixiaofeng
# @Site    : 
# @File    : random_upload.py
# @Software: PyCharm

import os, random, time
from common.logger import Log
from common.settings import driver_path, check_file, data_path, data_img_path, file_not_exists_error

log = Log()


def random_num():
    file_list = os.listdir(data_img_path)
    num = random.randint(0, len(file_list) - 1)
    return num


def uploaded(type=0):
    autolt_path = check_file(os.path.join(driver_path, "upload.exe"))
    if not autolt_path:
        raise FileNotFoundError(file_not_exists_error.format(autolt_path))
    if type == 0:
        log.info('开始上传图片...')
        if not check_file(os.path.join(data_img_path, '{}.jpg').format(random_num())):
            log.error('要图片的视频不存在！')
        else:
            time.sleep(1)
            os.system(r'{} {}'.format(autolt_path, os.path.join(data_img_path, '{}.jpg').format(random_num())))
            log.info('上传图片成功... {},{}'.format(autolt_path, os.path.join(data_img_path, '{}.jpg').format(random_num())))
    elif type == 1:
        log.info('开始上传视频...')
        if not check_file(os.path.join(data_path, 'video.mp4')):
            log.error('要上传的视频不存在！')
        else:
            time.sleep(1)
            os.system('{} {}'.format(autolt_path, os.path.join(data_path, 'video.mp4')))
            log.info('上传视频成功... {},{}'.format(autolt_path, os.path.join(data_path, 'video.mp4')))
    elif type == 2:
        log.info('开始上传音频...')
        if not check_file(os.path.join(data_path, 'audio.wav')):
            log.error('要上传的音频不存在！')
        else:
            time.sleep(1)
            os.system('{} {}'.format(autolt_path, os.path.join(data_path, 'audio.wav')))
            log.info('上传音频成功... audio.wav')
    else:
        log.error('上传文件类型错误，上传失败!')


if __name__ == '__main__':
    # uploaded(type=0)
    os.system(r'D:\UIAutomation-formwork\driver\upload.exe D:\UIAutomation-formwork\data\img\28.jpg')