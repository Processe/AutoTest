# coding=utf-8
# --author='fangfang'

from models.mobileFunction import FunctionLibrary
from models.screenshot import Screenshot
from models.mobileDriver import Mobile
from models.getDateTools import GetDataTools
from processed import Process
import unittest
from models.logger import Logger

logger = Logger(logger="test_case").getlog()

class TestCJJL(unittest.TestCase):
    def setUp(self):
        """
        实例化基础类
        :return:
        """
        mobile = Mobile()
        self.driver = mobile.open_app()
        self.functionlibrary = FunctionLibrary(self.driver)
        self.case_id = "出借记录_006"
        self.datatools = GetDataTools()
        self.case_module = self.datatools.getCaseModle('出借记录', self.case_id)
        self.process = Process(self.driver, self.case_module, self.case_id)
        self.screenshot = Screenshot(self.driver, self.case_module, self.case_id)
        logger.info('------' + self.case_id + '开始执行------')

    def test_procedure(self):
        # -----获取测试数据------
        username = self.datatools.getExcelDateRowValue('出借记录', '用户名', self.case_id)
        password = self.datatools.getExcelDateRowValue('出借记录', '密码', self.case_id)
        bdmc = self.datatools.getExcelDateRowValue('出借记录', '标的名称', self.case_id)
        hkfs = self.datatools.getExcelDateRowValue('出借记录', '还款方式', self.case_id)

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


