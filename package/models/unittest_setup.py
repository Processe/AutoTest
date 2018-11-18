# coding=utf-8
# --author='fangfang'

from models.screenshot import Screenshot
from models.getDateTools import GetDataTools
from models.webFunction import FunctionLibrary
from models.webDriver import BrowserEngine
from models.mobileDriver import Mobile
from processed import Process


class Setup(object):
    def __init__(self):
        self.driver = None
        self.functionlibrary = None
        self.process = None
        self.datatools = None
        self.module = None
        self.screenshot = None
        self.casemodel = None
        self.trade = None
        self.caseid = None

    def asset_web_setup(self, trade, caseID):
        """
        实例化基础类
        :return:
        """
        self.trade = trade
        self.caseid = caseID
        driver = BrowserEngine()
        self.driver = driver.open_browser()
        self.functionlibrary = FunctionLibrary(self.driver)
        self.datatools = GetDataTools("资管系统")
        self.module = self.datatools.getExcelDateRowValue(self.trade, '案例所属模块', self.caseid)
        self.process = Process(self.driver, self.module, self.caseid)
        self.screenshot = Screenshot(self.driver, self.module, self.caseid)

    def asset_mobile_setup(self, trade, caseID):
        """
        实例化基础类
        :return:
        """
        self.trade = trade
        self.caseid = caseID
        mobile = Mobile()
        self.driver = mobile.open_app()
        self.functionlibrary = FunctionLibrary(self.driver)
        self.datatools = GetDataTools("资管系统")
        self.module = self.datatools.getExcelDateRowValue(self.trade, '案例所属模块', self.caseid)
        self.process = Process(self.driver, self.module, self.caseid)
        self.screenshot = Screenshot(self.driver, self.module, self.caseid)

    def ycd360_web_setup(self, trade, caseID):
        """
        实例化基础类
        :return:
        """
        self.trade = trade
        self.caseid = caseID
        driver = BrowserEngine()
        self.driver = driver.open_browser()
        self.functionlibrary = FunctionLibrary(self.driver)
        self.datatools = GetDataTools("易港金融")
        self.module = self.datatools.getExcelDateRowValue(self.trade, '案例所属模块', self.caseid)
        self.process = Process(self.driver, self.module, self.caseid)
        self.screenshot = Screenshot(self.driver, self.module, self.caseid)

    def ycd360_mobile_setup(self, trade, caseID):
        """
        实例化基础类
        :return:
        """
        self.trade = trade
        self.caseid = caseID
        mobile = Mobile()
        self.driver = mobile.open_app()
        self.functionlibrary = FunctionLibrary(self.driver)
        self.datatools = GetDataTools("易港金融")
        self.module = self.datatools.getExcelDateRowValue(self.trade, '案例所属模块', self.caseid)
        self.process = Process(self.driver, self.module, self.caseid)
        self.screenshot = Screenshot(self.driver, self.module, self.caseid)
