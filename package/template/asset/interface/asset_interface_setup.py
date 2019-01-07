# coding=utf-8
# --author='fangfang'
from package.models.getDateTools import GetDataTools


class Setup:
    def __init__(self, trade, caseid):
        self.gt = GetDataTools("资管接口")
        self.trade = trade
        self.caseid = caseid
        self.username = None
        self.passwd = None
        self.position = None
        self.asset_type = None
        self.asset_phone = None
        self.asset_account = None
        self.asset_finace = None
        self.asset_purpose = None
        self.asset_customer_name = None
        self.asset_card = None
        self.asset_address = None
        self.asset_nation = None
        self.asset_sex = None
        self.asset_birthday = None
        self.asset_card_phone1 = None
        self.asset_card_phone2 = None
        self.asset_driver1 = None
        self.card_type = None
        self.bank_phone = None
        self.bank_no = None
        self.risk_level = None
        self.company_account = None
        self.company_card = None
        self.isEntrustedPayment = None
        self.company_address = None
        self.opening_bank = None
        self.asset_package_info = None
        self.purpose = None
        self.risk_result = None
        self.allow_amount = None
        self.riskCtrlRejectReson = None
        self.riskCtrl_remarks = None

    def set_return_info(self, col, value):
        self.gt.setExcelDateRowValue(self.trade, self.caseid, col, value)

    def set_result(self, result, response):
        self.gt.setExcelDateRowValue(self.trade, self.caseid, '执行结果', result)
        self.gt.setExcelDateRowValue(self.trade, self.caseid, '执行状态', '1-已执行')
        self.gt.setExcelDateRowValue(self.trade, self.caseid, '返回报文', response)

    def asset_login_setup(self):
        self.username = self.gt.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        self.passwd = self.gt.getExcelDateRowValue(self.trade, self.caseid, '密码')

    def switch_position_setup(self):
        self.username = self.gt.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        self.passwd = self.gt.getExcelDateRowValue(self.trade, self.caseid, '密码')
        self.position = self.gt.getExcelDateRowValue(self.trade, self.caseid, '部门')

    def asset_add_setup(self):
        self.username = self.gt.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        self.passwd = self.gt.getExcelDateRowValue(self.trade, self.caseid, '密码')
        self.position = self.gt.getExcelDateRowValue(self.trade, self.caseid, '部门')
        self.asset_type = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产类型')
        self.asset_phone = self.gt.getExcelDateRowValue(self.trade, self.caseid, '手机号码')
        self.asset_account = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款金额')
        self.asset_finace = self.gt.getExcelDateRowValue(self.trade, self.caseid, '金融产品')
        self.asset_purpose = self.gt.getExcelDateRowValue(self.trade, self.caseid, '车贷用途')
        self.asset_customer_name = self.gt.getExcelDateRowValue(self.trade, self.caseid, '客户姓名')
        self.asset_card = self.gt.getExcelDateRowValue(self.trade, self.caseid, '身份证号码')
        self.asset_address = self.gt.getExcelDateRowValue(self.trade, self.caseid, '户籍地址')
        self.asset_nation = self.gt.getExcelDateRowValue(self.trade, self.caseid, '民族')
        self.asset_sex = self.gt.getExcelDateRowValue(self.trade, self.caseid, '性别')
        self.asset_birthday = self.gt.getExcelDateRowValue(self.trade, self.caseid, '出生日期')
        self.asset_card_phone1 = self.gt.getExcelDateRowValue(self.trade, self.caseid, '身份证正面照')
        self.asset_card_phone2 = self.gt.getExcelDateRowValue(self.trade, self.caseid, '身份证反面照')
        self.asset_driver1 = self.gt.getExcelDateRowValue(self.trade, self.caseid, '行驶证首页')

    def put_task_action_setup(self):
        self.username = self.gt.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        self.passwd = self.gt.getExcelDateRowValue(self.trade, self.caseid, '密码')
        self.position = self.gt.getExcelDateRowValue(self.trade, self.caseid, '部门')
        self.asset_type = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产类型')
        self.asset_phone = self.gt.getExcelDateRowValue(self.trade, self.caseid, '手机号码')
        self.asset_account = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款金额')
        self.asset_finace = self.gt.getExcelDateRowValue(self.trade, self.caseid, '金融产品')
        self.asset_customer_name = self.gt.getExcelDateRowValue(self.trade, self.caseid, '客户姓名')
        self.asset_card = self.gt.getExcelDateRowValue(self.trade, self.caseid, '身份证号码')
        self.asset_sex = self.gt.getExcelDateRowValue(self.trade, self.caseid, '性别')
        self.card_type = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款人性质')
        self.bank_phone = self.gt.getExcelDateRowValue(self.trade, self.caseid, '银行预留手机号')
        self.bank_no = self.gt.getExcelDateRowValue(self.trade, self.caseid, '银行卡号')
        self.risk_level = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产风险等级')
        self.company_account = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司账号')
        self.company_card = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司营业执照号码')
        self.isEntrustedPayment = self.gt.getExcelDateRowValue(self.trade, self.caseid, '是否受托支付')
        self.company_address = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司地址')
        self.opening_bank = self.gt.getExcelDateRowValue(self.trade, self.caseid, '开户行')
        self.asset_package_info = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产包信息')
        self.purpose = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款用途')

    def submit_risk_result_setup(self):
        self.username = self.gt.getExcelDateRowValue(self.trade, self.caseid, '用户名')
        self.passwd = self.gt.getExcelDateRowValue(self.trade, self.caseid, '密码')
        self.position = self.gt.getExcelDateRowValue(self.trade, self.caseid, '部门')
        self.asset_type = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产类型')
        self.asset_phone = self.gt.getExcelDateRowValue(self.trade, self.caseid, '手机号码')
        self.asset_account = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款金额')
        self.asset_finace = self.gt.getExcelDateRowValue(self.trade, self.caseid, '金融产品')
        self.asset_customer_name = self.gt.getExcelDateRowValue(self.trade, self.caseid, '客户姓名')
        self.asset_card = self.gt.getExcelDateRowValue(self.trade, self.caseid, '身份证号码')
        self.asset_sex = self.gt.getExcelDateRowValue(self.trade, self.caseid, '性别')
        self.card_type = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款人性质')
        self.bank_phone = self.gt.getExcelDateRowValue(self.trade, self.caseid, '银行预留手机号')
        self.bank_no = self.gt.getExcelDateRowValue(self.trade, self.caseid, '银行卡号')
        self.risk_level = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产风险等级')
        self.company_account = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司账号')
        self.company_card = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司营业执照号码')
        self.isEntrustedPayment = self.gt.getExcelDateRowValue(self.trade, self.caseid, '是否受托支付')
        self.company_address = self.gt.getExcelDateRowValue(self.trade, self.caseid, '公司地址')
        self.opening_bank = self.gt.getExcelDateRowValue(self.trade, self.caseid, '开户行')
        self.asset_package_info = self.gt.getExcelDateRowValue(self.trade, self.caseid, '资产包信息')
        self.purpose = self.gt.getExcelDateRowValue(self.trade, self.caseid, '借款用途')
        self.risk_result = self.gt.getExcelDateRowValue(self.trade, self.caseid, '风控审核结果')
        self.allow_amount = self.gt.getExcelDateRowValue(self.trade, self.caseid, '准借金额')
        self.riskCtrlRejectReson = self.gt.getExcelDateRowValue(self.trade, self.caseid, '不通过原因')
        self.riskCtrl_remarks = self.gt.getExcelDateRowValue(self.trade, self.caseid, '风控审核备注')

