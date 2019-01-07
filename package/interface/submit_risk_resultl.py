# coding=utf-8
# --author='fangfang'

from models.httpTool import Http
from models.assetDB import AssetDB
from package.models.logger import Logger

log = Logger(logger='submit_risk_result').getlog()


def submit_risk_result(session, asset_items_id, result, allow_amount, riskCtrlRejectReson, remarks):
    # 实例化http请求
    http = Http()
    # 实例化数据库
    asset_db = AssetDB()
    # 数据库获取taskId
    taskId = asset_db.get_one(
            "select id from wf_application_task where asset_item_id = '%s' and status = 0" % asset_items_id)[0]
    url = '/api/asset/task/%s?action=submit' % taskId
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    # 风控审核结果
    data = {
        "outputPropertyList": [
                {"propertyId": "601", "propertyValue": result},
                {"propertyId": "228", "propertyValue": allow_amount},
                {"propertyId": "227", "propertyValue": riskCtrlRejectReson},
                {"propertyId": "20446", "propertyValue": remarks},
                ],
        "inputPropertyList": [],
        "uploadPropertyList": [
                {"propertyId": "601", "propertyValue": result},
                {"propertyId": "228", "propertyValue": allow_amount},
                {"propertyId": "227", "propertyValue": riskCtrlRejectReson},
                {"propertyId": "20446", "propertyValue": remarks}]
    }

    http.set_data(data)
    http.set_headers(headers)
    http.set_url(url)
    r = http.putWithJson()
    status = r.status_code
    rt = r.text
    if status == 200:
        r_json = r.json()
        log.info('访问submit_risk_result接口response%s' % rt)
        return r_json
    else:
        log.info('访问submit_risk_result接口response%s' % rt)
        return None

