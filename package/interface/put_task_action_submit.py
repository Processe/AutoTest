# coding=utf-8
# --author='fangfang'

from models.httpTool import Http
from models.assetDB import AssetDB


def task_submit_risk_info_personal(session, asset_items_id, bank_phone, name, ICcard, isEntrustedPayment, riskLevel,
                                   bank_card, purpose):
    # 不传输入信息废掉的参数：account, product_id,duration, repayment, phone,
    '''
    提交风控信息
    :param riskLevel:
    :param isEntrustedPayment:
    :param ICcard:
    :param name:
    :param bank_phone:
    :param asset_items_id:
    :param purpose:
    :param bank_card:
    :param session:
    :param taskId:
    :param datas:
    :return:
    '''
    # 实例化http请求
    http = Http()
    # 实例化数据库
    asset_db = AssetDB()
    # 数据库获取taskId
    taskId = \
        asset_db.get_one(
            "select id from wf_application_task where asset_item_id = '%s' and status = 0" % asset_items_id)[0]
    url = '/api/asset/task/%s?action=submit' % taskId
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    # 提交风控信息数据
    null = None
    data = {
        "outputPropertyList": [{"propertyId": "20368", "propertyValue": bank_phone},
                               {"propertyId": "10186", "propertyValue": "2018-11-21"},
                               {"propertyId": "10319",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
                               {"propertyId": "10320",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
                               {"propertyId": "214", "propertyValue": ICcard},
                               {"propertyId": "215", "propertyValue": "大地方"},
                               {"propertyId": "216", "propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
                               {"propertyId": "217", "propertyValue": "M"},
                               {"propertyId": "602", "propertyValue": isEntrustedPayment},
                               {"propertyId": "603", "propertyValue": null},
                               {"propertyId": "604", "propertyValue": null},
                               {"propertyId": "605", "propertyValue": null},
                               {"propertyId": "606", "propertyValue": null},
                               {"propertyId": "607", "propertyValue": null},
                               {"propertyId": "608", "propertyValue": null},
                               {"propertyId": "10336", "propertyValue": null},
                               {"propertyId": "609", "propertyValue": null},
                               {"propertyId": "226", "propertyValue": null},
                               {"propertyId": "610", "propertyValue": null},
                               {"propertyId": "611", "propertyValue": riskLevel},
                               {"propertyId": "242", "propertyValue": null},
                               {"propertyId": "20373", "propertyValue": null}],
        "inputPropertyList": [],
        "uploadPropertyList": [{"propertyId": "42", "propertyValue": "[]"},
                               {"propertyId": "43",
                                "propertyValue": "[{\"name\":\"我是未开户pc\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12345678900\",\"workUnit\":\"我是未开户pc\",\"post\":\"\",\"income\":\"\",\"otherIncome\":\"\",\"informedFlag\":1}]"},
                               {"propertyId": "44",
                                "propertyValue": "[{\"name\":\"我是未开户pc\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12345678900\",\"informedFlag\":1},{\"name\":\"dfgn\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12222222222\",\"informedFlag\":1},{\"name\":\"dfgn\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12222222222\",\"informedFlag\":1},{\"name\":\"dfgn\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12222222222\",\"informedFlag\":1}]"},
                               {"propertyId": "46",
                                "propertyValue": "[{\"nature\":\"租房\",\"owner\":\"\",\"address\":\"\",\"area\":\"\",\"price\":\"\",\"certificateFlag\":\"\",\"mortgageFlag\":\"\",\"totalLoan\":\"\",\"totalSurplusLoan\":\"\",\"phone\":\"\",\"rent\":\"\"}]"},
                               {"propertyId": "190", "propertyValue": bank_card},
                               {"propertyId": "213", "propertyValue": "45"},
                               {"propertyId": "602", "propertyValue": "0"},
                               {"propertyId": "221", "propertyValue": "1"},
                               {"propertyId": "222", "propertyValue": "2"},
                               {"propertyId": "223", "propertyValue": "2"},
                               {"propertyId": "301", "propertyValue": "7,6,5"},
                               {"propertyId": "302", "propertyValue": "3"},
                               {"propertyId": "303", "propertyValue": "2"},
                               {"propertyId": "304", "propertyValue": ""},
                               {"propertyId": "305", "propertyValue": ""},
                               {"propertyId": "306", "propertyValue": ""},
                               {"propertyId": "309", "propertyValue": 111111},  # 年收入
                               {"propertyId": "10001", "propertyValue": "3"},
                               {"propertyId": "10002", "propertyValue": ""},
                               {"propertyId": "10003", "propertyValue": ""},
                               {"propertyId": "10005", "propertyValue": "1"},
                               {"propertyId": "10006", "propertyValue": "1"},
                               {"propertyId": "10174", "propertyValue": ""},
                               {"propertyId": "10187", "propertyValue": "我是未开户pc"},
                               {"propertyId": "10188", "propertyValue": "我我是未开户pc"},
                               {"propertyId": "10232", "propertyValue": "我是未开户pc"},
                               {"propertyId": "20000", "propertyValue": "123456876099"},
                               {"propertyId": "20008", "propertyValue": ""},
                               {"propertyId": "20009", "propertyValue": ""},
                               {"propertyId": "20368", "propertyValue": bank_phone},
                               {"propertyId": "20060",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737356280.6786269003404697.jpg\"]"},
                               {"propertyId": "20061", "propertyValue": ""},
                               {"propertyId": "20062", "propertyValue": ""},
                               {"propertyId": "20063", "propertyValue": ""},
                               {"propertyId": "20064", "propertyValue": ""},
                               {"propertyId": "20065", "propertyValue": ""},
                               {"propertyId": "20066", "propertyValue": ""},
                               {"propertyId": "20067", "propertyValue": ""},
                               {"propertyId": "20069",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737283870.5883633345080488.jpg\"]"},
                               {"propertyId": "20086",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737245230.11148077390400979.jpg\"]"},
                               {"propertyId": "20103", "propertyValue": ""},
                               {"propertyId": "174", "propertyValue": name},
                               {"propertyId": "184", "propertyValue": "车辆品牌型号"},
                               {"propertyId": "185", "propertyValue": "车辆评估价格"},  # 车辆评估价格
                               {"propertyId": "187", "propertyValue": "车牌号码"},
                               {"propertyId": "214", "propertyValue": ICcard},
                               {"propertyId": "215", "propertyValue": "大地方"},
                               {"propertyId": "216", "propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
                               {"propertyId": "217", "propertyValue": "M"},
                               {"propertyId": "226", "propertyValue": "226"},  # 月收入
                               {"propertyId": "242", "propertyValue": "车辆评估审核价格"},  # 车辆评估审核价格
                               {"propertyId": "269", "propertyValue": "我是未开户pc"},
                               {"propertyId": "602", "propertyValue": "0"},
                               {"propertyId": "603",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737761010.15125835795637044.png\"]"},
                               {"propertyId": "604",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737800910.8303972981695504.png\"]"},
                               {"propertyId": "605",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737846440.7873967460257065.png\"]"},
                               {"propertyId": "606",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737882990.11425967830625017.png\"]"},
                               {"propertyId": "607",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737919680.27319181714520213.png\"]"},
                               {"propertyId": "608",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737966430.38506140915578735.png\"]"},
                               {"propertyId": "609",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738054880.33449213683342793.png\"]"},
                               {"propertyId": "610",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738130220.7647498617890951.png\"]"},
                               {"propertyId": "611", "propertyValue": riskLevel},
                               {"propertyId": "10011", "propertyValue": "2010"},
                               {"propertyId": "10012", "propertyValue": "购车价格"},  # 10012-购车价格
                               {"propertyId": "10172", "propertyValue": "江淮"},
                               {"propertyId": "10173", "propertyValue": "1"},
                               {"propertyId": "10186", "propertyValue": "2018-11-21"},
                               {"propertyId": "10319",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
                               {"propertyId": "10320",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
                               {"propertyId": "10336",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738021380.3785310067037544.png\"]"},
                               {"propertyId": "20264", "propertyValue": purpose},
                               {"propertyId": "20373", "propertyValue": ""}
                               ]}
    http.set_data(data)
    http.set_headers(headers)
    http.set_url(url)
    r = http.putWithJson()
    status = r.status_code
    if status == 200:
        print('风控信息提交成功：' + r.text)
    else:
        print('风控信息提交失败：' + r.text)


def task_submit_risk_info_company(session, asset_items_id, bank_phone, name, gongsi_card, isEntrustedPayment, riskLevel,
                                  bank_card, purpose, cardType):
    '''
    新车垫资贷，提交风控信息
    :param session:
    :param taskId:
    :param datas:
    :return:
    '''
    # 实例化http请求
    http = Http()
    # 实例化数据库
    asset_db = AssetDB()
    # 数据库获取taskId
    taskId = \
        asset_db.get_one(
            "select id from wf_application_task where asset_item_id = '%s' and status = 0" % asset_items_id)[0]
    url = '/api/asset/task/%s?action=submit' % taskId
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    # 提交风控信息数据
    null = None
    data = {
        "outputPropertyList": [{"propertyId": "20368", "propertyValue": bank_phone},
                               {"propertyId": "174", "propertyValue": name},
                               {"propertyId": "20373", "propertyValue": null
                                }],
        "inputPropertyList": [
            # {"propertyId": "60","propertyValue": "WSDYXG20181217004"},
            {"propertyId": "63", "propertyValue": "营业部"},
            {"propertyId": "64", "propertyValue": "万事达"},
            {"propertyId": "67", "propertyValue": "2018-12-17 16:18:33"},
            {"propertyId": "62", "propertyValue": "新车垫资贷"},
            {"propertyId": "307", "propertyValue": ""},
            {"propertyId": "100", "propertyValue": "6321"},
            {"propertyId": "171", "propertyValue": "211"},
            {"propertyId": "308", "propertyValue": "1"},
            {"propertyId": "177", "propertyValue": "3"},
            {"propertyId": "20264", "propertyValue": purpose},
            {"propertyId": "66", "propertyValue": "0"},
            {"propertyId": "174", "propertyValue": name},
            {"propertyId": "61", "propertyValue": bank_phone},
            {"propertyId": "214", "propertyValue": "420101199404166850"},
            {"propertyId": "218", "propertyValue": "汉"},
            {"propertyId": "217", "propertyValue": "M"},
            {"propertyId": "215", "propertyValue": "大地方"},
            {"propertyId": "216", "propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "10320",
             "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "10319",
             "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"}],
        "uploadPropertyList": [{"propertyId": "269", "propertyValue": "杭州西湖"},
                               {"propertyId": "603",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450347576840.9278062838241732.jpg\"]"},
                               {"propertyId": "604",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450347602550.47017364101112125.jpg\"]"},
                               {"propertyId": "701", "propertyValue": ""},
                               {"propertyId": "702", "propertyValue": ""},
                               {"propertyId": "703", "propertyValue": ""},
                               {"propertyId": "704", "propertyValue": ""},
                               {"propertyId": "705", "propertyValue": cardType},
                               {"propertyId": "706", "propertyValue": bank_card},
                               {"propertyId": "708",
                                "propertyValue": "[{\"nameOfBorrower\":\"卢文人\",\"idCardOfBorrower\":\"110101199003074370\",\"validPeriodOfBorrowerIdCard\":\"[\\\"2018-12-17\\\",\\\"2019-01-22\\\"]\",\"phoneOfBorrower\":\"13256714578\",\"frontPhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348466010.2040742258491941.jpg\\\"]\",\"reversePhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348506100.021807664806680505.jpg\\\"]\",\"relationOfContacts\":1,\"nameOfContacts\":\"发广告\",\"phoneOfContacts\":\"15623456254\",\"amountOfLoanApply\":\"9600\",\"vehicleTypeByStages\":\"大众\",\"excelOfLoanApply\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450349029570.17188913977529086.png\\\"]\"},{\"nameOfBorrower\":\"向上走\",\"idCardOfBorrower\":\"110101199003074370\",\"validPeriodOfBorrowerIdCard\":\"[\\\"2018-12-17\\\",\\\"2019-01-22\\\"]\",\"phoneOfBorrower\":\"13256714578\",\"frontPhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348466010.2040742258491941.jpg\\\"]\",\"reversePhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348506100.021807664806680505.jpg\\\"]\",\"relationOfContacts\":1,\"nameOfContacts\":\"发广告\",\"phoneOfContacts\":\"15623456254\",\"amountOfLoanApply\":\"9600\",\"vehicleTypeByStages\":\"奔驰\",\"excelOfLoanApply\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450349029570.17188913977529086.png\\\"]\"},{\"nameOfBorrower\":\"叶问\",\"idCardOfBorrower\":\"110101199003074370\",\"validPeriodOfBorrowerIdCard\":\"[\\\"2018-12-17\\\",\\\"2019-01-22\\\"]\",\"phoneOfBorrower\":\"13256714578\",\"frontPhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348466010.2040742258491941.jpg\\\"]\",\"reversePhotoOfBorrowerIdCard\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450348506100.021807664806680505.jpg\\\"]\",\"relationOfContacts\":1,\"nameOfContacts\":\"发广告\",\"phoneOfContacts\":\"15623456254\",\"amountOfLoanApply\":\"9600\",\"vehicleTypeByStages\":\"保时捷\",\"excelOfLoanApply\":\"[\\\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450349029570.17188913977529086.png\\\"]\"}]"},
                               {"propertyId": "10188", "propertyValue": "杭州西湖"},
                               {"propertyId": "20368", "propertyValue": bank_phone},
                               {"propertyId": "709", "propertyValue": ""},
                               {"propertyId": "710", "propertyValue": ""},
                               {"propertyId": "711", "propertyValue": ""},
                               {"propertyId": "712", "propertyValue": ""},
                               {"propertyId": "713", "propertyValue": ""},
                               {"propertyId": "714",
                                "propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15450349114540.8688634920458502.png\"]"},
                               {"propertyId": "20086", "propertyValue": ""},
                               {"propertyId": "20103", "propertyValue": ""},
                               {"propertyId": "602", "propertyValue": isEntrustedPayment},
                               {"propertyId": "611", "propertyValue": riskLevel},
                               {"propertyId": "20268", "propertyValue": "1"},
                               {"propertyId": "68", "propertyValue": gongsi_card},
                               {"propertyId": "174", "propertyValue": name},
                               {"propertyId": "707", "propertyValue": gongsi_card},
                               {"propertyId": "20373", "propertyValue": ""
                                }]
    }
    http.set_data(data)
    http.set_headers(headers)
    http.set_url(url)
    r = http.putWithJson()
    status = r.status_code
    if status == 200:
        print('风控信息提交成功：' + r.text)
    else:
        print('风控信息提交失败：' + r.text)
