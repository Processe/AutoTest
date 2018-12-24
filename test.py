# coding=gbk
import requests
import json
import pymysql

null = None


def connect_mysql(sql, key=0):
    '''
    �������ݿ⣬������ѯ�����ز�ѯ���
    :param sql:
    :param key:
    :return:
    '''
    # �����ʹܲ��Ի���
    cnn = pymysql.connect(host='rds6vef326vef32o.mysql.rds.aliyuncs.com', port=3306, user='daily',
                          passwd='U8v+Dg$o3vQt', db='asset_mig', charset='utf8')
    # �����α�
    cursor = cnn.cursor()
    # ִ��SQL����������Ӧ����
    result = cursor.execute(sql)
    # ��ȡ��һ������
    row_4 = cursor.fetchone()
    # ��ȡ�����ֶ�ֵ
    # value = row_4.values()
    # ��ȡָ���ֶ�ֵ
    value = row_4[key]
    cnn.commit()
    # �ر�����
    cnn.close()
    return value


def login(username, password):
    '''
    ��¼�ӿ�
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
    print("��¼�ӿڣ�" + r.text)
    return sessions


def switch_position(session, positionId):
    '''
    �л���λ
    :param session:
    :param positionId: ����Ա��251����Ӫ����253����ز���254��Ӫҵ����252�����񲿣�255�����񲿣�256�����겿��257
    :return: ��
    '''
    url = "http://asset-daily.ycd360.cn/api/asset/accounts/switch/position"
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    data = {"positionId": positionId}
    r = requests.put(url, json=data, headers=headers)
    print("�л���λ��" + r.text)


def asset_items_add(sessions, zcls, customerTelephone, borrowAmount, rateMethod, repaymentWay, repaymentDuration,
                    financeProductId, customerName, idCard, sex, chusrq1):
    '''
    �����ʲ��ӿ�
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
                    {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "��ط�"},
                    {"propertyId": "218", "propertyCode": "nation", "propertyValue": "��"},
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
    print("�����ʲ��ӿڣ�" + r.text)
    r = r.json()
    return r["data"]


def asset_items_edit(sessions, asset_item_id, zcls, customerTelephone, borrowAmount, rateMethod, repaymentWay,
                     repaymentDuration, financeProductId, customerName, idCard, sex, chusrq1):
    '''
    �༭�ʲ��ӿ�
    :return:
    '''
    data = {"assetId": connect_mysql("select * from sys_asset where name = '%s'" % zcls),
            "id": asset_item_id,
            "propertyList": [
                {"propertyId": "61", "propertyCode": "customerTelephone", "propertyValue": customerTelephone},  # �ֻ�����
                {"propertyId": "100", "propertyCode": "borrowAmount", "propertyValue": borrowAmount},  # �����
                {"propertyId": "194", "propertyCode": "rateMethod", "propertyValue": rateMethod},  # ��Ϣ��ʽ
                {"propertyId": "177", "propertyCode": "repaymentWay", "propertyValue": repaymentWay},  # ���ʽ
                {"propertyId": "308", "propertyCode": "repaymentDuration", "propertyValue": repaymentDuration},  # ��������
                {"propertyId": "171", "propertyCode": "financeProductId", "propertyValue": financeProductId},  # ���ڲ�Ʒ
                {"propertyId": "307", "propertyCode": "customerSource", "propertyValue": ""},  # �ͻ���Դ
                {"propertyId": "20264", "propertyCode": "chedyt1", "propertyValue": ""},  # ������;
                {"propertyId": "174", "propertyCode": "customerName", "propertyValue": customerName},  # �ͻ�����
                {"propertyId": "214", "propertyCode": "idCard", "propertyValue": idCard},  # ���֤��
                {"propertyId": "215", "propertyCode": "domicilePlace", "propertyValue": "����"},  # ������ַ
                {"propertyId": "218", "propertyCode": "nation", "propertyValue": null},  # ����
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
    print("�༭�ʲ��ӿ�" + r.text)


def put_task_action_submit(session, taskId, datas):
    '''
    �ύ�ڵ�
    :param session:
    :param taskId: ����ID
    :return:��
    '''
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    url = 'http://asset-daily.ycd360.cn/api/asset/task/%s?action=submit' % taskId
    response = requests.put(url, json=datas, headers=headers)
    print("�ύ����" + response.text)


def finance_products(session, products_id):
    '''
    ��ѯ���ڲ�Ʒ��Ϣ:�������ޡ����ʽ
    :param products_id�����ڲ�Ʒid
    :return:li
    '''

    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    url = 'http://asset-daily.ycd360.cn/api/asset/finance-products/%s' % products_id
    r = requests.get(url, headers=headers)
    r = r.json()
    rateMethod = r["data"]["rateMethod"]  # ��Ϣ��ʽ
    repayment = r["data"]["repayment"]  # ���ʽ
    duration = r["data"]["duration"]  # ��������
    li = []
    li.append(rateMethod)
    li.append(repayment)
    li.append(duration)
    print("��ѯ��Ʒ��Ϣ�ӿڣ�" + str(li))
    return li


if __name__ == '__main__':

    # ����
    name = "չ��3"

    # �ֻ���
    phone = 18519030808

    # ����Ԥ���ֻ���
    bank_phone = phone

    # ���п���
    bank_card = 6222029223887064830

    # ���֤����
    ICcard = 420101198008125075

    # # ����
    # name = "������"
    #
    # # �ֻ���
    # phone = 18519030811
    #
    # # ���п���
    # bank_card = 6212461600000401731
    #
    # # ���֤����
    # ICcard = 110101199003074231

    # �ʲ�����
    asset_type = "����չ��"

    # �����
    account = "10089"

    # ������;
    cdyt = "3"

    # �ʲ����յȼ�
    zcfxdj = "84"

    # �Ƿ�����֧��
    sfstzf = "0"

    # ���ڲ�Ʒ����
    jrcp_id = "201"   # �ܲ�չ��-1����-�׸�
    # ��¼
    session = login("18519030809", "1adbb3178591fd5bb0c248518f39bf6d")
    # �л���λ
    switch_position(session, "252")
    # ��ȡ���ڲ���Ϣ��ʽ�����ʽ����������
    jrcp_info = finance_products(session, jrcp_id)

    # ��Ϣ��ʽ
    jxfs = jrcp_info[0]
    # ���ʽ
    hkfs = jrcp_info[1]
    # ��������
    jkqx = jrcp_info[2]

    # # �����ʲ�
    # asset_id = asset_items_add(session, asset_type, phone, account, jxfs, hkfs, jkqx, jrcp_id, name, ICcard, "M", "2018-11-21")
    # # �༭�ʲ���Ϣ
    # asset_items_edit(session, asset_id, asset_type, phone, account, jxfs, hkfs, jkqx, jrcp_id, name, ICcard, "M", "2018-11-21")
    # �ύ�����Ϣ����
    # �л���λ
    switch_position(session, "252")
    # �ύ�����Ϣ����
    tjfkxx_data = {
            "outputPropertyList": [{"propertyId": "20368","propertyValue": bank_phone},
            {"propertyId": "10186","propertyValue": "2018-11-21"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "214","propertyValue": ICcard},
            {"propertyId": "215","propertyValue": "��ط�"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "602","propertyValue": sfstzf},
            {"propertyId": "603","propertyValue": null},
            {"propertyId": "604","propertyValue": null},
            {"propertyId": "611","propertyValue": zcfxdj},
            {"propertyId": "242","propertyValue": null},
            {"propertyId": "20373","propertyValue": null}],
            "inputPropertyList": [{"propertyId": "60","propertyValue": "WSDYXG20181130013"},
            {"propertyId": "63","propertyValue": "Ӫҵ��"},
            {"propertyId": "64","propertyValue": "���´�"},
            {"propertyId": "67","propertyValue": "2018-11-30 18:25:33"},
            {"propertyId": "62","propertyValue": "����չ��"},
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
            {"propertyId": "218","propertyValue": "��"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "215","propertyValue": "��ط�"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"}],
            "uploadPropertyList": [{"propertyId": "42","propertyValue": "[]"},
            {"propertyId": "43","propertyValue": "[{\"name\":\"����δ����pc\",\"relationship\":\"��\",\"age\":\"\",\"phone\":\"12345678900\",\"workUnit\":\"����δ����pc\",\"post\":\"\",\"income\":\"\",\"otherIncome\":\"\",\"informedFlag\":1}]"},
            {"propertyId": "44","propertyValue": "[{\"name\":\"����δ����pc\",\"relationship\":\"��\",\"age\":\"\",\"phone\":\"12345678900\",\"informedFlag\":1}]"},
            {"propertyId": "46","propertyValue": "[{\"nature\":\"�ⷿ\",\"owner\":\"\",\"address\":\"\",\"area\":\"\",\"price\":\"\",\"certificateFlag\":\"\",\"mortgageFlag\":\"\",\"totalLoan\":\"\",\"totalSurplusLoan\":\"\",\"phone\":\"\",\"rent\":\"\"}]"},
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
            {"propertyId": "10187","propertyValue": "����δ����pc"},
            {"propertyId": "10188","propertyValue": "������δ����pc"},
            {"propertyId": "10232","propertyValue": "����δ����pc"},
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
            {"propertyId": "184","propertyValue": "����δ����pc"},
            {"propertyId": "187","propertyValue": "����δ����pc"},
            {"propertyId": "214","propertyValue": ICcard},
            {"propertyId": "215","propertyValue": "��ط�"},
            {"propertyId": "216","propertyValue": "[\"2018-11-05\",\"2018-12-14\"]"},
            {"propertyId": "217","propertyValue": "M"},
            {"propertyId": "226","propertyValue": 123456},
            {"propertyId": "242","propertyValue": 123456},
            {"propertyId": "269","propertyValue": "����δ����pc"},
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
            {"propertyId": "10172","propertyValue": "����"},
            {"propertyId": "10173","propertyValue": "1"},
            {"propertyId": "10186","propertyValue": "2018-11-21"},
            {"propertyId": "10319","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428878999190.7695617701690018.jpg\"]"},
            {"propertyId": "10320","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15428879030960.11580892072857041.jpg\"]"},
            {"propertyId": "10336","propertyValue": "[\"http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/workflowproperty/15435738021380.3785310067037544.png\"]"},
            {"propertyId": "20264","propertyValue": cdyt},
            {"propertyId": "20373","propertyValue": ""}]}

    put_task_action_submit(session, "78217", datas=tjfkxx_data)

    # ������
    # put_task_action_submit(session, "77596", datas=fksh_data)

