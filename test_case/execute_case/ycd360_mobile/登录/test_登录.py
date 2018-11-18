# coding=utf-8
# --author='fangfang'

from models.mobile_Function import FunctionLibrary
from models.screenshot import Screenshot
from models.mobileDriver import Mobile
import unittest
import processed


class TestZZHK(unittest.TestCase):
    def setUp(self):
        # -----实例化基础类------
        driver = Mobile()
        self.driver = driver.driver
        self.functionlibrary = FunctionLibrary(self.driver)
        self.screenshot = Screenshot(self.driver)
        self.process = processed.Process(self.driver)
        self.username_ture = '18519030808'
        self.username_false = '18511030838'
        self.password_ture = 'asdf1234'
        self.password_false = 'asdf1111'

    def test_1login_ture(self):
        '''
        输入正确手机号密码登录
        :return:
        '''
        # -----业务逻辑代码------
        self.functionlibrary.ClickByName("我的")
        is_login = self.functionlibrary.elementIsExist("提现")
        if is_login:
            self.process.logout()
            self.functionlibrary.ClickByName("我的")
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_name", self.username_ture)
        self.functionlibrary.swipeOnScreenN(0.5, 0.5, 0.5, 0.5, 1)
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_pwd", self.password_ture)
        self.functionlibrary.ClickByName("登录")
        self.functionlibrary.ClickByName("取消")
        self.functionlibrary.waitNAME("首页")
        self.screenshot.takeTakesScreenshot('登录成功截图')
        self.process.logout()

    def test_2login_username_false(self):
        '''
        输入错误手机号码真确密码登录
        :return:
        '''
        # -----业务逻辑代码------
        self.functionlibrary.ClickByName("我的")
        is_login = self.functionlibrary.elementIsExist("提现")
        if is_login:
            self.process.logout()
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_name", self.username_false)
        self.functionlibrary.swipeOnScreenN(0.5, 0.5, 0.5, 0.5, 1)
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_pwd", self.password_ture)
        self.functionlibrary.ClickByName("登录")
        self.functionlibrary.CheckByText("com.ygjr.ycd.debug:id/dialog_tv_hint", "用户名或密码错误")
        self.screenshot.takeTakesScreenshot('登录失败截图')

    def test_3login_password_false(self):
        '''
        输入错误手机号正确密码登录
        :return:
        '''
        # -----业务逻辑代码------
        self.functionlibrary.ClickByName("我的")
        is_login = self.functionlibrary.elementIsExist("提现")
        if is_login:
            self.process.logout()
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_name", self.username_ture)
        self.functionlibrary.swipeOnScreenN(0.5, 0.5, 0.5, 0.5, 1)
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_pwd", self.password_false)
        self.functionlibrary.ClickByName("登录")
        self.functionlibrary.CheckByText("com.ygjr.ycd.debug:id/dialog_tv_hint", "用户名或密码错误")
        self.screenshot.takeTakesScreenshot('登录失败截图')

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭应用程序
        :return:
        """
        self.driver.quit()


