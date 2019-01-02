# coding=utf-8
# --author='fangfang'

from package.interface import login
from package.models import getDateTools
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "登录"
        self.case_id = "ZGXT_DL_002"
        self.dt = getDateTools.GetDataTools("资管接口")
        self.username = self.dt.getExcelDateRowValue(self.trade, self.case_id, "用户名")
        self.password = self.dt.getExcelDateRowValue(self.trade, self.case_id, "密码")

    def test_login(self):
        r_json = login.asset_login(self.username, self.password)
        if r_json["success"] is False and r_json['message'] == "用户校验失败":
            self.dt.setExcelDateRowValue(self.trade, self.case_id, '执行状态', '1-已执行')
            self.dt.setExcelDateRowValue(self.trade, self.case_id, '执行结果', '执行成功')
            self.dt.setExcelDateRowValue(self.trade, self.case_id, "返回报文", str(r_json))
        elif r_json["success"] is True and r_json['message'] != "":
            self.dt.setExcelDateRowValue(self.trade, self.case_id, '执行状态', '1-已执行')
            self.dt.setExcelDateRowValue(self.trade, self.case_id, '执行结果', '执行失败')
            self.dt.setExcelDateRowValue(self.trade, self.case_id, "返回报文", str(r_json))

    def tearDown(self):
        pass


