# coding=utf-8
# --author='fangfang'

from interface.asset import switch_position, asset_items, submit_risk_info, login

if __name__ == "__main__":
    # 金融产品定义
    # product_id = "201"   # 车抵展期-15天
    # product_id = "199"   # 车抵展期-等额本息-一个月
    # product_id = "200"   # 总部展期-三个月-易港
    # product_id = "205"   # 总部快速续贷_先息后本_3个月
    product_id = "211"  # 新車墊資貸  一次性--一個月
    # product_id = "215"   # 新车垫资贷 一次性--15天
    # product_id = "214"  # 新车垫资贷  --三个月等本
    # product_id = "217"  # 新车垫资贷  --6个月等本  ---易港不存在

    # 岗位
    positionId = "营业部"  # 业务部
    # 资产类型
    asset_type = "新车垫资贷"
    # asset_type = "总部快速续贷"
    # asset_type = "车抵展期"
    # 借款金额
    account = 500
    # 姓名
    # name = "金融01"
    # # 手机号
    # phone = 18519030811
    # # 银行预留手机号
    # bank_phone = phone
    # # 银行卡号
    # bank_card = 6212461600000401731
    # # 身份证号码
    # ICcard = 110101199003074231
    # 姓名
    # name = "刘强文"
    # # 手机号
    # phone = 18514593476
    # # 银行预留手机号
    # bank_phone = phone
    # # 身份证号码
    # ICcard = 420101199404166850
    # # 银行卡号
    # bank_card = 6222023405200738161    # 6212461600000501696  # 电子账号

    # # 姓名   已开户、授权 公司账户
    name = "大连濠林汽车经纪服务有限公司"
    # 手机号
    phone = 13296747005
    # 银行预留手机号
    bank_phone = phone
    # 营业执照号码
    gongsi_card = "91210211MA0UREXG02"
    # 银行卡号
    bank_card = "622848123456156413"
    # # # 电子银行账号    # # bank_card = "6212461600001001639"    622848123456156413
    #
    # 身份证号码：
    ICcard = "420101199404166850"
    # # 姓名   已开户、未授权 公司账户
    # name = "上海商派网络科技有限公司"
    # # 手机号
    # phone = 13950123611
    # # 银行预留手机号
    # bank_phone = phone
    # # 营业执照号码
    # gongsi_card = "91310104794480009"
    # # 银行卡号
    # bank_card = "6212461450000123574"

    #
    # 车贷用途
    purpose = "3"
    # 资产风险等级
    riskLevel = "96"
    # 是否受托支付
    isEntrustedPayment = "0"
    # 借款人性质
    cardType = 0  # 0-公司，1-个人

    session = login.get_session("18519030808", "1adbb3178591fd5bb0c248518f39bf6d")
    switch_position.switch_position(session, positionId)
    # # 计息方式
    # rateMethod = finance_products.finance_products(session, product_id, "计息方式")
    # # 还款方式
    # repayment = finance_products.finance_products(session, product_id, "还款方式")
    # # 还款期限
    # duration = finance_products.finance_products(session, product_id, "还款期限")

    asset_item_id = asset_items.asset_items_add(session, asset_type, phone, account,
                                                product_id, name, ICcard, "M")
    asset_items.asset_items_edit(session, asset_item_id, asset_type, phone, account,
                                 product_id, name, ICcard, "M")
    submit_risk_info.task_submit_risk_info_personal(session, asset_item_id, bank_phone, name, ICcard,
                                                    isEntrustedPayment, riskLevel, bank_card, purpose)
    # put_task_action_submit.task_submit_risk_info_company(session, asset_item_id, bank_phone, name, gongsi_card,
    #                                                      isEntrustedPayment, riskLevel, bank_card, purpose, cardType)
