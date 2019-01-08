# coding=utf-8
# --author='fangfang'

from models.httpTool import Http
from models.logger import Logger

log = Logger(logger="asset_login").getlog()


def switch_position(session, position):
    positionId = None
    # 根据岗位判断岗位编号
    if position == '营业部':
        positionId = '252'
    elif position == '运营部':
        positionId = '253'
    elif position == '风控部':
        positionId = '254'
    elif position == '服务部':
        positionId = '255'
    elif position == '财务部':
        positionId = '256'
    elif position == '发标部':
        positionId = '257'
    elif position == '管理员':
        positionId = '258'
    # 实例化http请求
    http = Http()
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8",
               "Cookie": "SESSION=" + session}
    url = "/api/asset/accounts/switch/position"
    data = {"positionId": positionId}
    http.set_url(url)
    http.set_headers(headers)
    http.set_data(data)
    r = http.putWithJson()
    status = r.status_code
    rt = r.text
    r_json = r.json()
    log.info("访问switch_position接口response：%s" % rt)
    return r_json
