# coding=utf-8
# --author='fangfang'

import os
import pickle
import time
import sys
from appium import webdriver
from configparser import ConfigParser
from models.path import get_obj_path
from models.logger import Logger
sep = os.path.sep  # 当前系统分隔符

logger = Logger(logger="testServer").getlog()

PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
    )


class ScriptError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Mobile(object):
    '''
    创建appium 的webdriver类
    '''
    def __init__(self):
        '''

        :param url: 建立链接appium的 IF
        :param port: 建立链接appium的端口
        :param udid: 移动设备的udid
        :param platformName: 移动端操作系统平台 Android/IOS
        '''
        self.path = get_obj_path()
        config = ConfigParser()
        # file_path = os.path.dirname(os.getcwd()) + '/config/config.ini'
        file_path = self.path + '/config/config.ini'
        config.read(file_path)
        port = config.get("testServer", "port")
        logger.info("You had select %s port." % port)
        url = config.get("testServer", "url")
        logger.info("The test server url is: %s" % url)
        deviceName = config.get("testServer", "deviceName")
        logger.info("The test server deviceName is: %s" % deviceName)
        platformName = config.get("testServer", "platformName")
        logger.info("The test server platformName is: %s" % platformName)
        appPackage = config.get("APPType", "appPackage")  # 定义APP包名
        logger.info("The APP Type appPackage is: %s" % appPackage)
        appActivity = config.get("APPType", "appActivity")  # 定义APPactivity名称
        logger.info("The APP Type appActivity is: %s" % appActivity)

        self.url = url
        self.port = port
        self.udid = deviceName
        self.platformName = platformName
        # conf文件目录
        self.configPath = sep.join([self.path, 'config'])
        # conf文件
        self.configFile = "%s%sconf%sdriver.ini" % (self.configPath, sep, sep)
        desired_caps = {}
        compare = "True"
        desired_caps["noSign"] = "true"
        desired_caps["noReset"] = "true"
        # 启用UNICODE输入，可以输入中文
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True
        desired_caps["deviceName"] = self.udid  # 定义手机设备udid
        desired_caps["platformName"] = self.platformName  # 定义手机操作平台
        desired_caps["udid"] = self.udid  # 定义IOS设备udid ，安卓可以不设置
        desired_caps["url"] = 'http://' + self.url +':' + self.port  # 定义appium服务器IP和端口号
        # desired_caps["app"] = os.path.dirname(self.url)+"/apps/{param1}" #定义安装包路径
        desired_caps["appPackage"] = appPackage
        desired_caps["appActivity"] = appActivity
        self.driver = webdriver.Remote(desired_caps["url"] + '/wd/hub', desired_caps)
        logger.info("-----------------webdriver建立完成-----------------")

    def ADBStopAPP(self):
        iosCommand = "adb shell am force-stop com.ygjr.ycd.debug"
        os.system(iosCommand)

    def quitDriver(self):
        self.driver.quit()
        self.ADBStopAPP()

    def mobile_setConfig(self):
        try:
            if not os.path.exists(self.configFile):
                # 如果持久化driver的文件不存在，就启动driver，然后保存driver
                f1 = open(self.driver, "wb")
                pickle.dump(self.driver, f1, 0)
                f1.close()
                # 是否登陆
                self.isLogin = 1
            else:
                # 否则就从文件中将driver读取出来，如果发生异常，第一件事是删除文件
                f1 = open(self.configFile, "rb")
                self.driver = pickle.load(f1)
                f1.close()
                time.sleep(1)
                self.isLogin = 0

        except Exception as e:
            funcName = sys._getframe().f_code.co_name
            raise ScriptError(funcName + "--" + "--driver init error--" + "--[异常信息]:%s" % repr(e))
            # self.track = "手机银行"

