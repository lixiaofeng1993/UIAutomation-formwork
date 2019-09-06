#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 10:03
# @Author  : lixiaofeng
# @Site    : 
# @File    : random_upload.py
# @Software: PyCharm

import os, random
from common.logger import Log
from common import read_config

log = Log()

upfile_img_path = os.path.join(read_config.upfile_path, 'ad')


def random_num():
    if os.path.exists(upfile_img_path):
        file_list = os.listdir(upfile_img_path)
        num = random.randint(0, len(file_list) - 1)
        return num
    else:
        log.error('图片目录不存在！')


def uploaded(type=0):
    if not os.path.exists(read_config.autolt_path):
        log.error('autolt工具生成的可执行文件不存在！')
    else:

        if type == 0:
            log.info('开始上传图片...')
            if not os.path.exists(os.path.join(upfile_img_path, '{}.jpg').format(random_num())):
                log.error('要图片的视频不存在！')
            else:
                os.system('{} "{}"'.format(read_config.autolt_path,
                                           os.path.join(upfile_img_path, '{}.jpg').format(random_num())))
                log.info('上传图片成功... {}.jpg'.format(random_num()))
        elif type == 1:
            log.info('开始上传视频...')
            if not os.path.exists(os.path.join(read_config.upfile_path, 'video.mp4')):
                log.error('要上传的视频不存在！')
            else:
                os.system('{} "{}"'.format(read_config.autolt_path, os.path.join(read_config.upfile_path, 'video.mp4')))
                log.info('上传视频成功... video.mp4')
        elif type == 2:
            log.info('开始上传音频...')
            if not os.path.exists(os.path.join(read_config.upfile_path, 'audio.wav')):
                log.error('要上传的音频不存在！')
            else:
                os.system('{} "{}"'.format(read_config.autolt_path, os.path.join(read_config.upfile_path, 'audio.wav')))
                log.info('上传音频成功... audio.wav')
        else:
            log.error('上传文件类型错误，上传失败!')


if __name__ == '__main__':
    uploaded(type=0)
