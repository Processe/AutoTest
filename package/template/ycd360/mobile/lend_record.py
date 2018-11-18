# coding=utf-8
# --author='fangfang'

from models.unittest_setup import Setup
import unittest
from models.logger import Logger

logger = Logger(logger="test_case").getlog()


class LendRecord:
    def __init__(self, trade, caseid):
        """
        定义案例trade和caseid
        :return:
        """
        self.trade = trade
        self.caseid = caseid

    def lend_record(self):
        # -------实例化基础类-----
        case = Setup()
        case.ycd360_mobile_setup(self.trade, self.caseid)
        datatools = case.datatools
        driver = case.driver
        functionlibrary = case.functionlibrary
        process = case.process
        screenshot = case.screenshot
        logger.info('------' + self.caseid + '开始执行------')

        # -----获取测试数据------
        username = datatools.getExcelDateRowValue('出借记录', '用户名', self.caseid)
        password = datatools.getExcelDateRowValue('出借记录', '密码', self.caseid)
        bdmc = datatools.getExcelDateRowValue('出借记录', '标的名称', self.caseid)
        bdzt = datatools.getExcelDateRowValue('出借记录', '标的状态', self.caseid)

        # -----业务逻辑代码------
        functionlibrary.ClickByName("我的")
        functionlibrary.IsExistByIdClick("com.ygjr.ycd.debug:id/dialog_iv_close")
        is_login = functionlibrary.elementIsExist("提现")
        if is_login:
            pass
        else:
            process.login(username, password)
            functionlibrary.ClickByName("我的")
        functionlibrary.ClickByName("我的出借")
        functionlibrary.ClickByName("出借记录")
        functionlibrary.ClickByName(bdmc)
        functionlibrary.CheckContentText("com.ygjr.ycd.debug:id/tender_detail_tv_status", bdzt)
        screenshot.takeTakesScreenshot("出借记录详情页面")

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭应用程序
        :return:
        """
        self.driver.quit()


