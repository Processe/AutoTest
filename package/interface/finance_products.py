# coding=utf-8
# --author='fangfang'

from models.httpTool import Http
from package.models.logger import Logger

log = Logger(logger='finance_products').getlog()


def finance_products(session, products_id, info):
    '''
    查询金融产品信息:还款期限、还款方式
    :param products_id：金融产品id
    :return:li
    '''
    # 实例化http请求工具
    http = Http()
    # 请求头
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    # 请求url
    url = '/api/asset/finance-products/%s' % products_id
    http.set_headers(headers)
    http.set_url(url)
    r = http.getWithJson()
    status = r.status_code
    rt = r.text
    r_json = r.json()
    getinfo = None
    if status == 200:
        if r_json["success"] is True:
            # print("查询金融产品信息成功：" + rt)
            if info == "计息方式":
                getinfo = r_json["data"]["rateMethod"]  # 计息方式
            elif info == "还款方式":
                getinfo = r_json["data"]["repayment"]  # 还款方式
            elif info == "还款期限":
                getinfo = r_json["data"]["duration"]  # 还款期限
        else:
            print("查询金融产品信息失败：" + rt)
    else:
        print("查询金融产品信息失败：" + rt)
    # li = []
    # li.append(rateMethod)
    # li.append(repayment)
    # li.append(duration)

    log.info("查询产品信息【" + info + "】为：" + str(getinfo))
    return getinfo
