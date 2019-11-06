# coding:utf-8
import logging
from logging.handlers import RotatingFileHandler
from common.settings import log_path, report_path, img_path, hour
import colorlog  # 控制台日志输入颜色
import time
import datetime
import os

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}


class Log:
    def __init__(self):
        self.logName = os.path.join(log_path, '%s.log' % hour)  # log文件的命名
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(filename)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
            log_colors=log_colors_config)  # 日志输出格式
        self.make = False
        self.handle_logs()

    def get_file_sorted(self, file_path):
        """最后修改时间顺序升序排列 os.path.getmtime()->获取文件最后修改时间"""
        dir_list = os.listdir(file_path)
        if not dir_list:
            return False
        else:
            dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
            return dir_list

    def complete_path(self, file_list, path):
        if isinstance(file_list, list):
            for file in file_list:
                file_path = os.path.join(path, file)  # 拼接文件的完整路径
                if os.path.isfile(file_path):
                    t_list = self.TimeStampToTime(os.path.getctime(file_path)).split('-')
                    now_list = self.TimeStampToTime(time.time()).split('-')
                    t = datetime.datetime(int(t_list[0]), int(t_list[1]),
                                          int(t_list[2]))  # 将时间转换成datetime.datetime 类型
                    now = datetime.datetime(int(now_list[0]), int(now_list[1]), int(now_list[2]))
                    if (now - t).days > 6:  # 创建时间大于6天的文件删除
                        self.delete_logs(file_path)
            if len(file_list) > 10:  # 限制目录下记录文件数量
                file_list = file_list[0:-10]
                for file in file_list:
                    file_path = os.path.join(path, file)
                    if os.path.isfile(file_path):
                        self.delete_logs(file_path)

    def TimeStampToTime(self, timestamp):
        """格式化时间"""
        timeStruct = time.localtime(timestamp)
        return str(time.strftime('%Y-%m-%d', timeStruct))

    def handle_logs(self):
        """处理日志过期天数和日志size备份"""
        log_list = self.get_file_sorted(log_path)
        report_list = self.get_file_sorted(report_path)
        report_img_list = self.get_file_sorted(img_path)
        if log_list:
            self.complete_path(log_list, log_path)
        if report_path:
            self.complete_path(report_list, report_path)
        if report_img_list:
            self.complete_path(report_img_list, img_path)

    def delete_logs(self, file_path):
        try:
            os.remove(file_path)
            return True
        except PermissionError as e:
            print('权限错误，删除日志文件失败！{}'.format(file_path))
            return False

    def __console(self, level, message):
        # 创建一个FileHandler，用于写到本地
        fh = RotatingFileHandler(filename=self.logName, mode='a', maxBytes=1024 * 1024 * 5, backupCount=5,
                                 encoding='utf-8')  # 使用RotatingFileHandler类，滚动备份日志
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        # 创建一个StreamHandler,用于输出到控制台
        ch = colorlog.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()  # 关闭打开的文件

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)


if __name__ == "__main__":
    log = Log()
    log.debug("---测试开始----")
    log.info("操作步骤")
    log.warning("----测试结束----")
    log.error("----测试错误----")
