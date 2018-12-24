# coding=utf-8
# --author='fangfang'

import requests
from package.models.messageTool import MessageTool


class ycd360_assert:
    def __init__(self):
        self.host = 'http://daily.ygclc.com'
        self.mt = MessageTool()
        self.appId = "aishangjie_1"
        self.version = "00"

    def accountStatusQuery(self, phone, cardId, name, bankAccountId):
        '''
        开户查询接口（对接编号1）
        :param phone:
        :param cardId:
        :param name:
        :param bankAccountId:
        :return:
        '''
        path = '/api/aishangjie/accountStatusQuery.html'
        url = self.host + path
        # s = sign("420101199404166850", "18514593476", "刘强文", "6212461600000501696")
        data = {"version": self.version, "appId": self.appId, "phone": phone, "cardId": cardId, "name": name,
                "bankAccountId": bankAccountId}
        l = self.mt.dict_sorted_to_list(data)
        s = self.mt.param_to_string(l)
        m = self.mt.encryption_md5(s)
        print("m:" + m)
        print(data)
        data.update({"sign": m})
        print(data)
        r = requests.post(url, json=data)
        print("查询账户状态接口：" + r.text)

    def assetPush(self, orgLoanId, asset_type, phone, cardId, name, bankAccountId):
        '''
        资产风控推送接口
        :return:
        '''
        path = "/api/aishangjie/assetPush.html"
        url = self.host + path
        # data = {
        #         "version": "00",
        #         "appId": "aishangjie_1",
        #         "orgLoanId": orgLoanId,
        #         "phone": phone,
        #         "cardId": cardId,
        #         "name": name,
        #         "type": asset_type,
        #         "style": "style",
        #         "bankAccountId": bankAccountId,
        #         "timeLimit": "1",
        #         "isday": "0",
        #         "timeLimitDay": "0",
        #         "assetApr": "20",
        #         "account": "5600.00",
        #         "entrustFlag": "entrustFlag",
        #         "riskGrade": "riskGrade",
        #         "useType": "249",
        #         "repayGuarantee": "工资收入",
        #         "photo1": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/6429192c91eef3e4.jpg",
        #         "photo2": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/f2d271607788f5e4.png",
        #         "photo3": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/1fc6853170bd9739.jpg",
        #         "realname": "周承琦",
        #         "sex": "男",
        #         "birthday": "----------",
        #         "age": "24",
        #         "cardValidDate": "2015年02月16日至2025年02月16日",
        #         "bankName": "杭州",
        #         "householdRegister": "1",
        #         "address": "杭州西湖",
        #         "maritalStatus": "1",
        #         "childrenStatus": "1",
        #         "education": "本科",
        #         "estateStatus": "1",
        #         "carStatus": "1",
        #         "carLoanStatus": "1",
        #         "socialSecurityStatus": "1",
        #         "accFundStatus": "1",
        #         "sesameCreditScore": "345",
        #         "unitIndustry": "金融",
        #         "unitProperties": "贷款",
        #         "unitScale": "",
        #         "unitName": "",
        #         "unitAddress": "",
        #         "unitPhone": "",
        #         "duty": "",
        #         "workingLife": "",
        #         "income": "5000.0",
        #         "sourceIncome": "工作",
        #         "contactName1": "",
        #         "contactRelation1": "",
        #         "contactPhone1": "400 002 5151",
        #         "contactName2": "",
        #         "contactRelation2": "",
        #         "contactPhone2": "",
        #         "contactName3": "",
        #         "contactRelation3": "",
        #         "contactPhone3": "",
        #         "otherName1": "",
        #         "otherRelation1": "",
        #         "otherPhone1": "",
        #         "otherName2": "",
        #         "otherRelation2": "",
        #         "otherPhone2": "",
        #         "otherName3": "",
        #         "otherRelation3": "",
        #         "otherPhone3": "",
        #         "repayPath": "1",
        #         "elecSignAuthStatus": "0",
        #         "bailPhone": ""
        #     }
        data = {
                "birthday": "----------",
                "income": "5000.0",
                "education": "本科",
                "repayPath": "1",
                "contactPhone1": "4000025151",
                "type": asset_type,
                "useType": "249",
                "repayGuarantee": "工资收入",
                "photo2": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/6429192c91eef3e4.jpg",
                "photo3": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/f2d271607788f5e4.png",
                "elecSignAuthStatus": "1",
                "isday": "0",
                "assetApr": "20",
                "appId": self.appId,
                "timeLimitDay": "0",
                "cardValidDate": "2015年02月16日至2025年02月16日",
                "bankAccount": bankAccountId,
                "orgLoanId": orgLoanId,
                "sex": "男",
                "version": self.version,
                "realname": name,
                "timeLimit": "1",
                "photo1": "http://51fanbei.oss-cn-hangzhou.aliyuncs.com/test/1fc6853170bd9739.jpg",
                "phone": phone,
                "cardId": cardId,
                "style": "0",
                "riskGrade": "81",
                "account": "5000.00"
                }
        l = self.mt.dict_sorted_to_list(data)
        # print(l)
        s = self.mt.param_to_string(l)
        print(s)
        m = self.mt.encryption_md5(s)
        print(m)
        data.update({"sign": m})
        print(data)
        r = requests.post(url, json=data)
        print("资产风控推送接口：" + r.text)
        return orgLoanId

    def assetConfirm(self, orgLoanId):
        '''
        确认资产风控推送接口
        :return:
        '''
        path = "/api/aishangjie/assetConfirm.html"
        url = self.host + path
        data = {"version": self.version, "appId": self.appId, "orgLoanId": orgLoanId}
        l = self.mt.dict_sorted_to_list(data)
        # print(l)
        s = self.mt.param_to_string(l)
        print(s)
        m = self.mt.encryption_md5(s)
        print(m)
        data.update({"sign": m})
        print(data)
        r = requests.post(url, json=data)
        rt = r.text
        print("资产风控推送接口：" + rt)

    def assetRevoke(self, orgLoanId):
        '''
        确认资产推送
        :return:
        '''
        path = "/api/aishangjie/assetRevoke.html"
        url = self.host + path
        data = {"version": self.version, "appId": self.appId, "orgLoanId": orgLoanId}
        l = self.mt.dict_sorted_to_list(data)
        # print(l)
        s = self.mt.param_to_string(l)
        print(s)
        m = self.mt.encryption_md5(s)
        print(m)
        data.update({"sign": m})
        r = requests.post(url, json=data)
        rt = r.text
        print("查询资产状态接口：" + rt)

    def assetStatusQuery(self, orgLoanId):
        '''
        查询资产状态
        :return:
        '''
        path = "/api/aishangjie/assetStatusQuery.html"
        url = self.host + path
        data = {"version": self.version, "appId": self.appId, "orgLoanId": orgLoanId}
        l = self.mt.dict_sorted_to_list(data)
        s = self.mt.param_to_string(l)
        m = self.mt.encryption_md5(s)
        data.update({"sign": m})
        r = requests.post(url, json=data)
        rt = r.text
        print("查询资产状态接口：" + rt)
