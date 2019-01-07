# coding=utf-8
# --author='fangfang'

from package.interface import asset_items, switch_position, login, submit_risk_info
from package.template.asset.interface.asset_interface_setup import Setup
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "提交风控信息"
        self.case_id_001 = "ZGXT_TJFKXX_001"
        self.case_id_002 = "ZGXT_TJFKXX_002"
        self.case_id_003 = "ZGXT_TJFKXX_003"
        self.case_id_004 = "ZGXT_TJFKXX_004"
        self.case_id_005 = "ZGXT_TJFKXX_005"
        self.case_id_006 = "ZGXT_TJFKXX_006"
        self.case_id_007 = "ZGXT_TJFKXX_007"
        self.case_id_008 = "ZGXT_TJFKXX_008"
        self.case_id_009 = "ZGXT_TJFKXX_009"
        self.case_id_010 = "ZGXT_TJFKXX_010"
        self.case_id_011 = "ZGXT_TJFKXX_011"

    def test_submit_risk_info_001(self):
        data = Setup(self.trade, self.case_id_001)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.bank_no, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_002(self):
        data = Setup(self.trade, self.case_id_002)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_003(self):
        data = Setup(self.trade, self.case_id_003)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_004(self):
        data = Setup(self.trade, self.case_id_004)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_005(self):
        data = Setup(self.trade, self.case_id_005)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_006(self):
        data = Setup(self.trade, self.case_id_006)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_007(self):
        data = Setup(self.trade, self.case_id_007)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_008(self):
        data = Setup(self.trade, self.case_id_008)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_009(self):
        data = Setup(self.trade, self.case_id_009)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_010(self):
        data = Setup(self.trade, self.case_id_010)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_info_011(self):
        data = Setup(self.trade, self.case_id_011)
        data.put_task_action_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, data.position)
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            r_json = submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                                    data.asset_customer_name,
                                                                    data.company_card, data.isEntrustedPayment,
                                                                    data.risk_level,
                                                                    data.company_account, data.purpose,
                                                                    data.card_type)
        else:
            r_json = submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                                     data.asset_customer_name,
                                                                     data.asset_card, data.isEntrustedPayment,
                                                                     data.risk_level,
                                                                     data.asset_account, data.purpose)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def tearDown(self):
        pass
