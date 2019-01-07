# coding=utf-8
# --author='fangfang'

from package.interface import login
from package.template.asset.interface.asset_interface_setup import Setup
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "登录"
        self.case_id_001 = "ZGXT_DL_001"
        self.case_id_002 = "ZGXT_DL_002"
        self.case_id_003 = "ZGXT_DL_003"
        self.case_id_004 = "ZGXT_DL_004"

    def test_login_001(self):
        data = Setup(self.trade, self.case_id_001)
        data.asset_login_setup()
        r_json = login.asset_login(data.username, data.passwd)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_login_002(self):
        data = Setup(self.trade, self.case_id_002)
        data.asset_login_setup()
        r_json = login.asset_login(data.username, data.passwd)
        if r_json["success"] is False and r_json['message'] == "用户校验失败":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is True and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_login_003(self):
        data = Setup(self.trade, self.case_id_003)
        data.asset_login_setup()
        r_json = login.asset_login(data.username, data.passwd)
        if r_json["success"] is False and r_json['message'] == "登录服务错误":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is True and r_json['message'] != "登录服务错误":
            data.set_result('执行失败', str(r_json))

    def test_login_004(self):
        data = Setup(self.trade, self.case_id_004)
        data.asset_login_setup()
        r_json = login.asset_login(data.username, data.passwd)
        if r_json["success"] is False and r_json['message'] == "登录服务错误":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is True and r_json['message'] != "登录服务错误":
            data.set_result('执行失败', str(r_json))

    def tearDown(self):
        pass

