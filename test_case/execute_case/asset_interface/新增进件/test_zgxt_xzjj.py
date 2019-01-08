# coding=utf-8
# --author='fangfang'

from interface.asset import switch_position, asset_items, login
from package.template.asset.interface.asset_interface_setup import Setup
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "新增进件"
        self.case_id_001 = "ZGXT_XZJJ_001"
        self.case_id_002 = "ZGXT_XZJJ_002"
        self.case_id_003 = "ZGXT_XZJJ_003"
        self.case_id_004 = "ZGXT_XZJJ_004"
        self.case_id_005 = "ZGXT_XZJJ_005"
        self.case_id_006 = "ZGXT_XZJJ_006"
        self.case_id_007 = "ZGXT_XZJJ_007"
        self.case_id_008 = "ZGXT_XZJJ_008"
        self.case_id_009 = "ZGXT_XZJJ_009"
        self.case_id_010 = "ZGXT_XZJJ_010"
        self.case_id_011 = "ZGXT_XZJJ_011"
        self.case_id_012 = "ZGXT_XZJJ_012"
        self.case_id_013 = "ZGXT_XZJJ_013"
        self.case_id_014 = "ZGXT_XZJJ_014"
        self.case_id_015 = "ZGXT_XZJJ_015"
        self.case_id_016 = "ZGXT_XZJJ_016"
        self.case_id_017 = "ZGXT_XZJJ_017"

    def test_asset_items_001(self):
        data = Setup(self.trade, self.case_id_001)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_002(self):
        data = Setup(self.trade, self.case_id_002)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_003(self):
        data = Setup(self.trade, self.case_id_003)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_004(self):
        data = Setup(self.trade, self.case_id_004)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_005(self):
        data = Setup(self.trade, self.case_id_005)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_006(self):
        data = Setup(self.trade, self.case_id_006)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_007(self):
        data = Setup(self.trade, self.case_id_007)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_008(self):
        data = Setup(self.trade, self.case_id_008)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_009(self):
        data = Setup(self.trade, self.case_id_009)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_010(self):
        data = Setup(self.trade, self.case_id_010)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_011(self):
        data = Setup(self.trade, self.case_id_011)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_012(self):
        data = Setup(self.trade, self.case_id_012)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_013(self):
        data = Setup(self.trade, self.case_id_013)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_014(self):
        data = Setup(self.trade, self.case_id_014)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_015(self):
        data = Setup(self.trade, self.case_id_015)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_016(self):
        data = Setup(self.trade, self.case_id_016)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_asset_items_017(self):
        data = Setup(self.trade, self.case_id_017)
        data.asset_add_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        r_json = asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone, data.asset_account, data.asset_finace, data.asset_customer_name, data.asset_card, data.asset_sex)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def tearDown(self):
        pass
