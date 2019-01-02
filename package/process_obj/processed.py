# coding=utf-8
# --author='fangfang'

from models.mobileFunction import FunctionLibrary
from models.screenshot import Screenshot
from models.logger import Logger

logger = Logger(logger="processed").getlog()


class Process:
    def __init__(self, driver, case_modle, case_id):
        self.driver = driver
        self.functionlibrary = FunctionLibrary(self.driver)
        self.screenshot = Screenshot(self.driver, case_modle, case_id)

    def login(self, username, pasword):
        # self.functionlibrary.ClickByName("我的")
        self.functionlibrary.waitNAME("登录")
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_name", username)
        self.functionlibrary.swipeOnScreenN(0.5, 0.5, 0.5, 0.5, 1)
        self.functionlibrary.SendKeysByID("com.ygjr.ycd.debug:id/login_et_pwd", pasword)
        self.functionlibrary.ClickByName("登录")
        self.functionlibrary.ClickByName("取消")
        self.functionlibrary.waitNAME("首页")
        self.screenshot.takeTakesScreenshot('登录成功截图')
        logger.info("process login execute succeed!")

    def logout(self):
        self.functionlibrary.ClickByName("我的")
        self.functionlibrary.waitNAME("设置中心")
        self.functionlibrary.ClickByName("设置中心")
        self.functionlibrary.ClickByName("退出账号")
        self.functionlibrary.ClickByName("确认")
        self.screenshot.takeTakesScreenshot('推出成功截图')
        logger.info("process logout execute succeed!")

