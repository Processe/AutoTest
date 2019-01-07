# coding=utf-8
# --author='fangfang'
from models.unittest_setup import Setup
import unittest
from models.logger import Logger

logger = Logger(logger="test_case").getlog()


class TestCJJL(unittest.TestCase):
    def setUp(self):
        """
        实例化基础类
        :return:
        """
        self.caseid = "出借记录_004"
        self.trade = "出借记录"
        case = Setup()
        case.asset_web_setup(self.trade, self.caseid)
        self.datatools = case.datatools
        self.case_module = case.module
        self.driver = case.driver
        self.functionlibrary = case.functionlibrary
        self.process = case.process
        self.screenshot = case.screenshot
        logger.info('------' + self.caseid + '开始执行------')
    def test_procedure(self):
        # -----获取测试数据------
        username = self.datatools.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        password = self.datatools.getExcelDateRowValue(self.trade, self.caseid, '密码')
        bdmc = self.datatools.getExcelDateRowValue(self.trade, self.caseid, '标的名称')
        hkfs = self.datatools.getExcelDateRowValue(self.trade, self.caseid, '还款方式')

        # -----业务逻辑代码------
        self.functionlibrary.ClickByName("我的")
        self.functionlibrary.IsExistByIdClick("com.ygjr.ycd.debug:id/dialog_iv_close")
        is_login = self.functionlibrary.elementIsExist("提现")
        if is_login:
            pass
        else:
            self.process.login(username, password)
            self.functionlibrary.ClickByName("我的")
        self.functionlibrary.ClickByName("我的出借")
        self.functionlibrary.ClickByName("出借记录")
        self.functionlibrary.ClickByName(bdmc)
        xmhkfs_get = self.functionlibrary.getCJJLXQ("项目还款方式")
        self.functionlibrary.dataCompare(hkfs, xmhkfs_get)
        self.screenshot.takeTakesScreenshot("出借记录详情页面")

    def tearDown(self):
        """
        测试结束后的操作，这里基本上都是关闭应用程序
        :return:
        """
        self.driver.quit()


