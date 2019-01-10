# coding=utf-8
# --author='fangfang'

from models.httpTool import Http
from models.logger import Logger

log = Logger(logger="asset_login").getlog()


def switch_position(session, position):
    # 根据岗位判断岗位编号
    position_data = {'营业部': '252', '运营部': '253', '风控部': '254', '服务部': '255', '财务部': '256', '发标部': '257', '管理员': '258'}
    positionId = position_data[position]
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
