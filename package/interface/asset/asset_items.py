# coding=utf-8
# --author='fangfang'

from assetDB import AssetDB
from httpTool import Http
from interface.asset import finance_products
from package.models.logger import Logger

log = Logger(logger="asset_items").getlog()


def asset_items_add(sessions, assetType, customerTelephone, borrowAmount, financeProductId, customerName, idCard, sex):
    # 实例化http请求
    http = Http()
    # 实例化数据库
    database = AssetDB()
    url = "/api/asset/asset-items"
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + sessions}
    # 获取资产类型ID
    asset_id = database.get_one("select id from sys_asset where name = '%s'" % assetType)[0]
    # print(asset_id)
    # 计息方式
    rateMethod = finance_products.finance_products(sessions, financeProductId, "计息方式")
    # 还款方式
    repayment = finance_products.finance_products(sessions, financeProductId, "还款方式")
    # 还款期限
    duration = finance_products.finance_products(sessions, financeProductId, "还款期限")
    data = dict(assetId=asset_id,
                propertyList=[
                    {"propertyId": "61", "propertyCode": "customerTelephone", "propertyValue": customerTelephone},
                    {"propertyId": "100", "propertyCode": "borrowAmount", "propertyValue": borrowAmount},
                    {"propertyId": "194", "propertyCode": "rateMethod", "propertyValue": rateMethod},
                    {"propertyId": "177", "propertyCode": "repaymentWay", "propertyValue": repayment},
                    {"propertyId": "308", "propertyCode": "repaymentDuration", "propertyValue": duration},
                    {"propertyId": "171", "propertyCode": "financeProductId", "propertyValue": financeProductId},
                    {"propertyId": "307", "propertyCode": "customerSource", "propertyValue": ""},
                    {"propertyId": "20264", "propertyCode": "chedyt1", "propertyValue": ""},
                    {"propertyId": "174", "propertyCode": "customerName", "propertyValue": customerName},
                    {"propertyId": "214", "propertyCode": "idCard", "propertyValue": idCard},
                    {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "大地方"},
                    {"propertyId": "218", "propertyCode": "nation", "propertyValue": "汉"},
                    {"propertyId": "217", "propertyCode": "sex", "propertyValue": sex},  # "M"
                    {"propertyId": "10186", "propertyCode": "chusrq1", "propertyValue": "1983-11-21"},  # "2018-11-21"
                    {"propertyId": "216", "propertyCode": "cardValidPeriodEnd",
                     "propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
                    {"propertyId": "10319", "propertyCode": "idCardFrontPicture",
                     "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
                    {"propertyId": "10320", "propertyCode": "idCardBackPicture",
                     "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
                    {"propertyId": "236", "propertyCode": "xingszsy1",
                     "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15433205397830.7983244780280092.jpg\"]"
                     }
                ],
                step=1)
    http.set_url(url)
    http.set_headers(headers)
    http.set_data(data)
    r = http.postWithJson()
    status = r.status_code
    rt = r.text
    data_json = r.json()
    asset_item_id = data_json["data"]
    log.info("访问asset_login接口response：%s" % rt)
    return asset_item_id


def asset_items_edit(sessions, asset_item_id, assetType, customerTelephone, borrowAmount, financeProductId, customerName, idCard, sex):
    '''
    编辑资产接口
    :return:
    '''
    # 实例化http请求
    http = Http()
    # 实例化数据库
    database = AssetDB()
    # 获取资产类型ID
    asset_id = database.get_one("select id from sys_asset where name = '%s'" % assetType)[0]
    # 计息方式
    rateMethod = finance_products.finance_products(sessions, financeProductId, "计息方式")
    # 还款方式
    repayment = finance_products.finance_products(sessions, financeProductId, "还款方式")
    # 还款期限
    duration = finance_products.finance_products(sessions, financeProductId, "还款期限")
    data = {"assetId": asset_id,
            "id": asset_item_id,
            "propertyList": [
                {"propertyId": "61", "propertyCode": "customerTelephone", "propertyValue": customerTelephone},  # 手机号码
                {"propertyId": "100", "propertyCode": "borrowAmount", "propertyValue": borrowAmount},  # 借款金额
                {"propertyId": "194", "propertyCode": "rateMethod", "propertyValue": rateMethod},  # 计息方式
                {"propertyId": "177", "propertyCode": "repaymentWay", "propertyValue": repayment},  # 还款方式
                {"propertyId": "308", "propertyCode": "repaymentDuration", "propertyValue": duration},  # 还款期限
                {"propertyId": "171", "propertyCode": "financeProductId", "propertyValue": financeProductId},  # 金融产品
                {"propertyId": "307", "propertyCode": "customerSource", "propertyValue": ""},  # 客户来源
                {"propertyId": "20264", "propertyCode": "chedyt1", "propertyValue": ""},  # 车贷用途
                {"propertyId": "174", "propertyCode": "customerName", "propertyValue": customerName},  # 客户姓名
                {"propertyId": "214", "propertyCode": "idCard", "propertyValue": idCard},  # 身份证号
                {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "的撒"},  # 户籍地址
                {"propertyId": "218", "propertyCode": "nation", "propertyValue": "汉"},  # 民族
                {"propertyId": "217", "propertyCode": "sex", "propertyValue": sex},  # "M"
                {"propertyId": "10186", "propertyCode": "chusrq1", "propertyValue": "1983-11-21"},  # "2018-11-21"
                {"propertyId": "216", "propertyCode": "cardValidPeriodEnd",
                 "propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
                {"propertyId": "10319", "propertyCode": "idCardFrontPicture",
                 "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
                {"propertyId": "10320", "propertyCode": "idCardBackPicture",
                 "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
                {"propertyId": "236", "propertyCode": "xingszsy1",
                 "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15433205397830.7983244780280092.jpg\"]"
                 }],
            "step": 2,
            "businessType": 5,
            "assetInFinanceVersion": ""}
    url = "/api/asset/asset-items/%s" % asset_item_id
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + sessions}
    http.set_url(url)
    http.set_headers(headers)
    http.set_data(data)
    r = http.putWithJson()
    status = r.status_code
    rt = r.text
    r_json = r.json()
    log.info("访问asset_login接口response：%s" % rt)
    return r_json
