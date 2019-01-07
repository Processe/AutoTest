# coding=utf-8
# --author='fangfang'

from package.interface import switch_position, login
from package.template.asset.interface.asset_interface_setup import Setup
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "切换部门"
        self.case_id_001 = "ZGXT_QHBM_001"
        self.case_id_002 = "ZGXT_QHBM_002"
        self.case_id_003 = "ZGXT_QHBM_003"
        self.case_id_004 = "ZGXT_QHBM_004"
        self.case_id_005 = "ZGXT_QHBM_005"
        self.case_id_006 = "ZGXT_QHBM_006"
        self.case_id_007 = "ZGXT_QHBM_007"

    def test_switch_position_001(self):
        data = Setup(self.trade, self.case_id_001)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_002(self):
        data = Setup(self.trade, self.case_id_002)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_003(self):
        data = Setup(self.trade, self.case_id_003)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_004(self):
        data = Setup(self.trade, self.case_id_004)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_005(self):
        data = Setup(self.trade, self.case_id_005)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_006(self):
        data = Setup(self.trade, self.case_id_006)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_switch_position_007(self):
        data = Setup(self.trade, self.case_id_007)
        data.switch_position_setup()
        sesion = login.get_session(data.username, data.passwd)
        r_json = switch_position.switch_position(sesion, data.position)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def tearDown(self):
        pass
