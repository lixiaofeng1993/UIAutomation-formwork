#!/user/bin/env python
# coding=utf-8
'''
# 创 建 人: 李先生
# 文 件 名: app.py
# 说   明: 
# 创建时间: 2019/12/24 19:34
'''
import os
from selenium import webdriver
from appium import webdriver as app
from selenium.common.exceptions import *
from common.logger import Log
from common import read_config
from common.settings import driver_path, check_file, file_not_exists_error


class App:
    @classmethod
    def open_browser(cls, browser="chrome"):
        """打开浏览器函数。firefox、chrome、ie,phantomjs"""

        try:
            if browser == "firefox":
                Log().info("start browser name :Firefox")
                executable_path = check_file(os.path.join(driver_path, "geckodriver.exe"))
                if not executable_path:
                    raise FileNotFoundError(file_not_exists_error.format(executable_path))
                else:
                    driver = webdriver.Firefox(executable_path=executable_path)
                    return driver
            elif browser == "chrome":
                Log().info("start browser name :Chrome")
                # 加启动配置,忽略 Chrome正在受到自动软件的控制 提示
                option = webdriver.ChromeOptions()
                option.add_argument("disable-infobars")
                # chrome启动静默模式;默认显示浏览器界面
                if read_config.chrome_interface != "True":
                    option.add_argument("headless")
                executable_path = check_file(os.path.join(driver_path, "chromedriver.exe"))
                if not executable_path:
                    raise FileNotFoundError(file_not_exists_error.format(executable_path))
                else:
                    driver = webdriver.Chrome(chrome_options=option, executable_path=executable_path)
                    return driver
            elif browser == "ie":
                Log().info("start browser name :Ie")
                driver = webdriver.Ie()
                return driver
            elif browser == "js":
                Log().info("start browser name :PhantomJS")
                driver = webdriver.PhantomJS()
                return driver
            else:
                Log().warning("额，暂不支持此浏览器诶。先试试firefox、chrome、ie、phantomJS浏览器吧。")
                raise NoSuchWindowException("额，暂不支持此浏览器诶。先试试firefox、chrome、ie、phantomJS浏览器吧。")
        except Exception as msg:
            Log().error("浏览器出错了呀！{}".format(msg))
            raise Exception("浏览器出错了呀！{}".format(msg))

    @classmethod
    def open_app(cls, html=False):
        try:
            desired_caps = {
                "platformName": read_config.platform_name,

                "deviceName": read_config.device_name,

                # "platformVersion": read_config.platform_version,

                "automationName": read_config.automationName,

                # 不重置app
                "noReset": True,

                # 隐藏手机默认键盘
                "unicodeKeyboard": True,

                "resetKeyboard": True,

                # "udid": "" # 指定运行设备
                # "chromeOptions": {"androidProcess": "com.tencent.mm:tools"}
            }

            if not html:
                desired_caps.update({"appPackage": read_config.app_package,

                                     "appActivity": read_config.app_activity, })
            else:
                executable_path = check_file(os.path.join(os.path.join(driver_path, "h5"), "chromedriver.exe"))
                desired_caps.update({"browserName": read_config.browserName,

                                     "chromedriverExecutable": executable_path,

                                     "showChromedriverLog": True, })

            # 关联appium
            driver = app.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            return driver
        except Exception as e:
            raise Exception("连接 Appium 出错：{}".format(e))
