# coding=utf-8
# --author='fangfang'

from interface.asset import login
from package.models import getDateTools
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "登录"
        self.case_id = "ZGXT_DL_004"
        self.dt = getDateTools.GetDataTools("资管接口.xlsx")
        self.username = self.dt.getExcelDateRowValue(self.trade, self.case_id, "用户名")
        self.password = self.dt.getExcelDateRowValue(self.trade, self.case_id, "密码")

    def test_login(self):
        login.asset_login(self.username, self.password)

    def tearDown(self):
        self.dt.setExcelDateRowValue(self.trade, self.case_id, '执行状态', '1-已执行')
        self.dt.setExcelDateRowValue(self.trade, self.case_id, '运行结果', '执行成功')


