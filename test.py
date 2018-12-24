# coding=gbk
import requests
import json
import pymysql

null = None


def connect_mysql(sql, key=0):
    '''
    链接数据库，并做查询，返回查询结果
    :param sql:
    :param key:
    :return:
    '''
    # 链接资管测试环境
    cnn = pymysql.connect(host='rds6vef326vef32o.mysql.rds.aliyuncs.com', port=3306, user='daily',
                          passwd='U8v+Dg$o3vQt', db='asset_mig', charset='utf8')
    # 创建游标
    cursor = cnn.cursor()
    # 执行SQL，并返回响应行数
    result = cursor.execute(sql)
    # 获取第一行数据
    row_4 = cursor.fetchone()
    # 获取所有字段值
    # value = row_4.values()
    # 获取指定字段值
    value = row_4[key]
    cnn.commit()
    # 关闭链接
    cnn.close()
    return value


def login(username, password):
    '''
    登录接口
    :param username:
    :param password:
    :return:
    '''
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8"}
    url = "http://asset-daily.ycd360.cn/api/asset/login"
    # datas = '{"account": "%s", "identifier": "%s"}' % (username, password)
    datas = {"account": username, "identifier": password}
    # datas = json.dumps(datas)
    r = requests.post(url, json=datas, headers=headers)
    sessions = r.cookies["SESSION"]
    print("登录接口：" + r.text)
    return sessions


def switch_position(session, positionId):
    '''
    切换岗位
    :param session:
    :param positionId: 管理员：251，运营部：253，风控部：254，营业部：252，服务部：255，财务部：256，发标部：257
    :return: 无
    '''
    url = "http://asset-daily.ycd360.cn/api/asset/accounts/switch/position"
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    data = {"positionId": positionId}
    r = requests.put(url, json=data, headers=headers)
    print("切换岗位：" + r.text)


def asset_items_add(sessions, zcls, customerTelephone, borrowAmount, rateMethod, repaymentWay, repaymentDuration,
                    financeProductId, customerName, idCard, sex, chusrq1):
    '''
    新增资产接口
    :param session:
    :return:
    '''
    data = dict(assetId=connect_mysql("select * from sys_asset where name = '%s'" % zcls),
                propertyList=[
                    {"propertyId": "61", "propertyCode": "customerTelephone", "propertyValue": customerTelephone},
                    {"propertyId": "100", "propertyCode": "borrowAmount", "propertyValue": borrowAmount},
                    {"propertyId": "194", "propertyCode": "rateMethod", "propertyValue": rateMethod},
                    {"propertyId": "177", "propertyCode": "repaymentWay", "propertyValue": repaymentWay},
                    {"propertyId": "308", "propertyCode": "repaymentDuration", "propertyValue": repaymentDuration},
                    {"propertyId": "171", "propertyCode": "financeProductId", "propertyValue": financeProductId},
                    {"propertyId": "307", "propertyCode": "customerSource", "propertyValue": ""},
                    {"propertyId": "20264", "propertyCode": "chedyt1", "propertyValue": ""},
                    {"propertyId": "174", "propertyCode": "customerName", "propertyValue": customerName},
                    {"propertyId": "214", "propertyCode": "idCard", "propertyValue": idCard},
                    {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "大地方"},
                    {"propertyId": "218", "propertyCode": "nation", "propertyValue": "汉"},
                    {"propertyId": "217", "propertyCode": "sex", "propertyValue": sex},  # "M"
                    {"propertyId": "10186", "propertyCode": "chusrq1", "propertyValue": chusrq1},  # "2018-11-21"
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
    url = "http://asset-daily.ycd360.cn/api/asset/asset-items"
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + sessions}
    r = requests.post(url, json=data, headers=headers)
    print("新增资产接口：" + r.text)
    r = r.json()
    return r["data"]


def asset_items_edit(sessions, asset_item_id, zcls, customerTelephone, borrowAmount, rateMethod, repaymentWay,
                     repaymentDuration, financeProductId, customerName, idCard, sex, chusrq1):
    '''
    编辑资产接口
    :return:
    '''
    data = {"assetId": connect_mysql("select * from sys_asset where name = '%s'" % zcls),
            "id": asset_item_id,
            "propertyList": [
                {"propertyId": "61", "propertyCode": "customerTelephone", "propertyValue": customerTelephone},  # 手机号码
                {"propertyId": "100", "propertyCode": "borrowAmount", "propertyValue": borrowAmount},  # 借款金额
                {"propertyId": "194", "propertyCode": "rateMethod", "propertyValue": rateMethod},  # 计息方式
                {"propertyId": "177", "propertyCode": "repaymentWay", "propertyValue": repaymentWay},  # 还款方式
                {"propertyId": "308", "propertyCode": "repaymentDuration", "propertyValue": repaymentDuration},  # 还款期限
                {"propertyId": "171", "propertyCode": "financeProductId", "propertyValue": financeProductId},  # 金融产品
                {"propertyId": "307", "propertyCode": "customerSource", "propertyValue": ""},  # 客户来源
                {"propertyId": "20264", "propertyCode": "chedyt1", "propertyValue": ""},  # 车贷用途
                {"propertyId": "174", "propertyCode": "customerName", "propertyValue": customerName},  # 客户姓名
                {"propertyId": "214", "propertyCode": "idCard", "propertyValue": idCard},  # 身份证号
                {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "的撒"},  # 户籍地址
                {"propertyId": "218", "propertyCode": "nation", "propertyValue": null},  # 民族
                {"propertyId": "217", "propertyCode": "sex", "propertyValue": sex},  # "M"
                {"propertyId": "10186", "propertyCode": "chusrq1", "propertyValue": chusrq1},  # "2018-11-21"
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
    url = "http://asset-daily.ycd360.cn/api/asset/asset-items/%s" % asset_item_id
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + sessions}
    r = requests.put(url, json=data, headers=headers)
    print("编辑资产接口" + r.text)


def put_task_action_submit(session, taskId, datas):
    '''
    提交节点
    :param session:
    :param taskId: 任务ID
    :return:无
    '''
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    url = 'http://asset-daily.ycd360.cn/api/asset/task/%s?action=submit' % taskId
    response = requests.put(url, json=datas, headers=headers)
    print("提交任务" + response.text)


def finance_products(session, products_id):
    '''
    查询金融产品信息:还款期限、还款方式
    :param products_id：金融产品id
    :return:li
    '''

    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    url = 'http://asset-daily.ycd360.cn/api/asset/finance-products/%s' % products_id
    r = requests.get(url, headers=headers)
    r = r.json()
    rateMethod = r["data"]["rateMethod"]  # 计息方式
    repayment = r["data"]["repayment"]  # 还款方式
    duration = r["data"]["duration"]  # 还款期限
    li = []
    li.append(rateMethod)
    li.append(repayment)
    li.append(duration)
    print("查询产品信息接口：" + str(li))
    return li


if __name__ == '__main__':

    # 姓名
    name = "展期3"

    # 手机号
    phone = 18519030808

    # 银行预留手机号
    bank_phone = phone

    # 银行卡号
    bank_card = 6222029223887064830

    # 身份证号码
    ICcard = 420101198008125075

    # # 姓名
    # name = "吴先生"
    #
    # # 手机号
    # phone = 18519030811
    #
    # # 银行卡号
    # bank_card = 6212461600000401731
    #
    # # 身份证号码
    # ICcard = 110101199003074231

    # 资产类型
    asset_type = "车抵展期"

    # 借款金额
    account = "10089"

    # 车贷用途
    cdyt = "3"

    # 资产风险等级
    zcfxdj = "84"

    # 是否受托支付
    sfstzf = "0"

    # 金融产品定义
    jrcp_id = "201"   # 总部展期-1个月-易港
    # 登录
    session = login("18519030809", "1adbb3178591fd5bb0c248518f39bf6d")
    # 切换岗位
    switch_position(session, "252")
    # 获取金融产计息方式、还款方式、还款期限
    jrcp_info = finance_products(session, jrcp_id)

    # 计息方式
    jxfs = jrcp_info[0]
    # 还款方式
    hkfs = jrcp_info[1]
    # 还款期限
    jkqx = jrcp_info[2]

    # # 新增资产
    # asset_id = asset_items_add(session, asset_type, phone, account, jxfs, hkfs, jkqx, jrcp_id, name, ICcard, "M", "2018-11-21")
    # # 编辑资产信息
    # asset_items_edit(session, asset_id, asset_type, phone, account, jxfs, hkfs, jkqx, jrcp_id, name, ICcard, "M", "2018-11-21")
    # 提交风控信息任务
    # 切换岗位
    switch_position(session, "252")
    # 提交风控信息数据
    tjfkxx_data = {
            "outputPropertyList": [{"propertyId": "20368","propertyValue": bank_phone},
            {"propertyId": "10186","propertyValue": "2018-11-21"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "214","propertyValue": ICcard},
            {"propertyId": "215","propertyValue": "大地方"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "602","propertyValue": sfstzf},
            {"propertyId": "603","propertyValue": null},
            {"propertyId": "604","propertyValue": null},
            {"propertyId": "611","propertyValue": zcfxdj},
            {"propertyId": "242","propertyValue": null},
            {"propertyId": "20373","propertyValue": null}],
            "inputPropertyList": [{"propertyId": "60","propertyValue": "WSDYXG20181130013"},
            {"propertyId": "63","propertyValue": "营业部"},
            {"propertyId": "64","propertyValue": "万事达"},
            {"propertyId": "67","propertyValue": "2018-11-30 18:25:33"},
            {"propertyId": "62","propertyValue": "车抵展期"},
            {"propertyId": "307","propertyValue": ""},
            {"propertyId": "100","propertyValue": account},
            {"propertyId": jrcp_id,"propertyValue": "201"},
            {"propertyId": "308","propertyValue": jkqx},
            {"propertyId": "177","propertyValue": hkfs},
            {"propertyId": "20264","propertyValue": ""},
            {"propertyId": "66","propertyValue": "0"},
            {"propertyId": "174","propertyValue": name},
            {"propertyId": "61","propertyValue": phone},
            {"propertyId": "214","propertyValue": ICcard},
            {"propertyId": "218","propertyValue": "汉"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "215","propertyValue": "大地方"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"}],
            "uploadPropertyList": [{"propertyId": "42","propertyValue": "[]"},
            {"propertyId": "43","propertyValue": "[{\"name\":\"我是未开户pc\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12345678900\",\"workUnit\":\"我是未开户pc\",\"post\":\"\",\"income\":\"\",\"otherIncome\":\"\",\"informedFlag\":1}]"},
            {"propertyId": "44","propertyValue": "[{\"name\":\"我是未开户pc\",\"relationship\":\"打啊\",\"age\":\"\",\"phone\":\"12345678900\",\"informedFlag\":1}]"},
            {"propertyId": "46","propertyValue": "[{\"nature\":\"租房\",\"owner\":\"\",\"address\":\"\",\"area\":\"\",\"price\":\"\",\"certificateFlag\":\"\",\"mortgageFlag\":\"\",\"totalLoan\":\"\",\"totalSurplusLoan\":\"\",\"phone\":\"\",\"rent\":\"\"}]"},
            {"propertyId": "190","propertyValue": bank_card},
            {"propertyId": "213","propertyValue": "45"},
            {"propertyId": "221","propertyValue": "1"},
            {"propertyId": "222","propertyValue": "2"},
            {"propertyId": "223","propertyValue": "2"},
            {"propertyId": "301","propertyValue": "7,6,5"},
            {"propertyId": "302","propertyValue": "3"},
            {"propertyId": "303","propertyValue": "2"},
            {"propertyId": "304","propertyValue": ""},
            {"propertyId": "305","propertyValue": ""},
            {"propertyId": "306","propertyValue": ""},
            {"propertyId": "309","propertyValue": 123456},
            {"propertyId": "10001","propertyValue": "3"},
            {"propertyId": "10002","propertyValue": ""},
            {"propertyId": "10003","propertyValue": ""},
            {"propertyId": "10005","propertyValue": "1"},
            {"propertyId": "10006","propertyValue": "1"},
            {"propertyId": "10174","propertyValue": ""},
            {"propertyId": "10187","propertyValue": "我是未开户pc"},
            {"propertyId": "10188","propertyValue": "我我是未开户pc"},
            {"propertyId": "10232","propertyValue": "我是未开户pc"},
            {"propertyId": "20000","propertyValue": "123456876099"},
            {"propertyId": "20008","propertyValue": ""},
            {"propertyId": "20009","propertyValue": ""},
            {"propertyId": "20368","propertyValue": bank_phone},
            {"propertyId": "20060","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737356280.6786269003404697.jpg\"]"},
            {"propertyId": "20061","propertyValue": ""},
            {"propertyId": "20062","propertyValue": ""},
            {"propertyId": "20063","propertyValue": ""},
            {"propertyId": "20064","propertyValue": ""},
            {"propertyId": "20065","propertyValue": ""},
            {"propertyId": "20066","propertyValue": ""},
            {"propertyId": "20067","propertyValue": ""},
            {"propertyId": "20069","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737283870.5883633345080488.jpg\"]"},
            {"propertyId": "20086","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737245230.11148077390400979.jpg\"]"},
            {"propertyId": "20103","propertyValue": ""},
            {"propertyId": "174","propertyValue": name},
            {"propertyId": "184","propertyValue": "我是未开户pc"},
            {"propertyId": "187","propertyValue": "我是未开户pc"},
            {"propertyId": "214","propertyValue": ICcard},
            {"propertyId": "215","propertyValue": "大地方"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "226","propertyValue": 123456},
            {"propertyId": "242","propertyValue": 123456},
            {"propertyId": "269","propertyValue": "我是未开户pc"},
            {"propertyId": "602","propertyValue": "0"},
            {"propertyId": "603","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737761010.15125835795637044.png\"]"},
            {"propertyId": "604","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737800910.8303972981695504.png\"]"},
            {"propertyId": "605","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737846440.7873967460257065.png\"]"},
            {"propertyId": "606","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737882990.11425967830625017.png\"]"},
            {"propertyId": "607","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737919680.27319181714520213.png\"]"},
            {"propertyId": "608","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435737966430.38506140915578735.png\"]"},
            {"propertyId": "609","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738054880.33449213683342793.png\"]"},
            {"propertyId": "610","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738130220.7647498617890951.png\"]"},
            {"propertyId": "611","propertyValue": zcfxdj},
            {"propertyId": "10011","propertyValue": "2010"},
            {"propertyId": "10012","propertyValue": 123456},
            {"propertyId": "10172","propertyValue": "江淮"},
            {"propertyId": "10173","propertyValue": "1"},
            {"propertyId": "10186","propertyValue": "2018-11-21"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "10336","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738021380.3785310067037544.png\"]"},
            {"propertyId": "20264","propertyValue": cdyt},
            {"propertyId": "20373","propertyValue": ""}]}

    put_task_action_submit(session, "78217", datas=tjfkxx_data)

    # 风控审核
    # put_task_action_submit(session, "77596", datas=fksh_data)

