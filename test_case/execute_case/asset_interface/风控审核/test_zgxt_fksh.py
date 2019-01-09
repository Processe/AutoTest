# coding=utf-8
# --author='fangfang'

from interface.asset import switch_position, asset_items, submit_risk_info, submit_risk_resultl, login
from package.template.asset.interface.asset_interface_setup import Setup
import unittest


class Login(unittest.TestCase):
    def setUp(self):
        self.trade = "风控审核"
        self.case_id_001 = "ZGXT_FKSH_001"
        self.case_id_002 = "ZGXT_FKSH_002"
        self.case_id_003 = "ZGXT_FKSH_003"
        self.case_id_004 = "ZGXT_FKSH_004"
        self.case_id_005 = "ZGXT_FKSH_005"
        self.case_id_006 = "ZGXT_FKSH_006"
        self.case_id_007 = "ZGXT_FKSH_007"
        self.case_id_008 = "ZGXT_FKSH_008"

    def test_submit_risk_result_001(self):
        data = Setup(self.trade, self.case_id_001)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_002(self):
        data = Setup(self.trade, self.case_id_002)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_003(self):
        data = Setup(self.trade, self.case_id_003)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_004(self):
        data = Setup(self.trade, self.case_id_004)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_005(self):
        data = Setup(self.trade, self.case_id_005)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_006(self):
        data = Setup(self.trade, self.case_id_006)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_007(self):
        data = Setup(self.trade, self.case_id_007)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def test_submit_risk_result_008(self):
        data = Setup(self.trade, self.case_id_008)
        data.submit_risk_result_setup()
        sesion = login.get_session(data.username, data.passwd)
        switch_position.switch_position(sesion, '营业部')
        asset_item_id = asset_items.asset_items_add(sesion, data.asset_type, data.asset_phone, data.asset_account,
                                                    data.asset_finace, data.asset_customer_name, data.asset_card,
                                                    data.asset_sex)
        asset_items.asset_items_edit(sesion, asset_item_id, data.asset_type, data.asset_phone,
                                     data.asset_account, data.asset_finace, data.asset_customer_name,
                                     data.asset_card, data.asset_sex)
        if data.card_type == '0':
            submit_risk_info.task_submit_risk_info_company(sesion, asset_item_id, data.bank_phone,
                                                           data.asset_customer_name,
                                                           data.company_card, data.isEntrustedPayment,
                                                           data.risk_level,
                                                           data.company_account, data.purpose,
                                                           data.card_type)
        else:
            submit_risk_info.task_submit_risk_info_personal(sesion, asset_item_id, data.bank_phone,
                                                            data.asset_customer_name,
                                                            data.asset_card, data.isEntrustedPayment,
                                                            data.risk_level,
                                                            data.asset_account, data.purpose)
        switch_position.switch_position(sesion, data.position)
        r_json = submit_risk_resultl.submit_risk_result(sesion, asset_item_id, data.risk_result, data.allow_amount, data.riskCtrlRejectReson, data.riskCtrl_remarks)
        if r_json["success"] is True and r_json['message'] == "":
            data.set_return_info('返回资产编号', asset_item_id)
            data.set_result('执行成功', str(r_json))
        elif r_json["success"] is False and r_json['message'] != "":
            data.set_result('执行失败', str(r_json))

    def tearDown(self):
        pass

