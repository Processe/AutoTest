# -*- coding: utf-8 -*-
# @Time    : 2018/12/12 0012 下午 16:46
# @Author  : fangfang
# @File    : asset_push.py

from models.httpTool import Http
import time

host = "dev.ygclc.com"
path = "/api/aishangjie/assetPush.html"


def asset_push():

    http = Http()
    url = host + path
    print(url)
    # headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8"}
    # headers = {'Connection': 'close'}
    data = {
        "accFundStatus":"1",
        "account":"500",
        "address":"浙江省杭州市",
        "age":"22",
        "appId":"ycd360_1",
        "assetApr":"8",
        "bankAccount":"6212461600000701213",
        "bankName":"江西银行",
        "birthday":"1975-06-01",
        "buyTime":"2010",
        # "carBand":"奥迪",
        # "carLicensePlate":"云A1E1X7",
        # "carLoanStatus":"0",
        # "carModel":"别克牌SGM7161LEAT",
        # "carPhotos":["http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "http://ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg"],
        # "carPrice":"253500.00",
        # "carStatus":"1",
        # "cardId":"440103197506012059",
        # "cardType":"1616",
        # "cardValidDate":"2007年07月04日至2020年08月22日",
        # "childrenStatus":"0",
        # "contactName1":"111",
        # "contactPhone1":"11",
        # "contactRelation1":"11",
        # "duty":"部门主管",
        # "education":"本科",
        # "elecSignAuthStatus":"1",
        # "estateStatus":"1",
        # "evaluationPrice":"103500.00",
        # "income":"20000",
        # "isday":"0",
        # "maritalStatus":"0",
        # "orgLoanId":"ycd1111111111111117117",
        # "otherName1":"111",
        # "otherPhone1":"11",
        # "otherRelation1":"11",
        # "phone":"13296742004",
        # "photo1":"http: //ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "photo2":"http: //ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "photo3":"http: //ycd360.oss-cn-hzfinance.aliyuncs.com/asset/daily/asset_workflow_prp/IMG_20180714_154554.jpg",
        # "realname":"退回保证金测试账户",
        # "repayGuarantee":"工资收入，经营收入，房屋收入，店铺收入，理财收入，其他收入，投资收入，月收入：20000，个人信誉状况良好,无不良记录。",
        # "repayPath":"1",
        # "riskGrade":"88",
        # "sesameCreditScore":"888",
        # "sex":"男",
        # "socialSecurityStatus":"1",
        # "sourceIncome":"工资收入，经营收入，房屋收入，店铺收入，理财收入，其他收入，投资收入",
        # "style":"3",
        # "timeLimit":"3",
        # "type":"103",
        # "unitAddress":"杭州市拱墅区",
        # "unitIndustry":"传统制造业",
        # "unitName":"易港金融",
        # "unitPhone":"38927438374",
        # "unitProperties":"私营企业",
        # "unitScale":"100-499人",
        # "useType":"245",
        # "workingLife":"2",
        "assetPartnerId":"1"
    }
    http.set_url(url)
    #v http.set_headers(headers)
    http.set_data(data)
    flag = False

    r = http.postWithJson()
    # while not flag:
    #
    #     try:
    #         r = http.postWithJson()
    #     except:
    #         print(u'[%s] HTTP请求失败！！！正在准备重发。。。')
    #         time.sleep(0.5)
    #         continue
    #     flag = True


    return r


if __name__ == "__main__":

    r = asset_push()
    print(r.text)

