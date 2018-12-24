# coding=utf-8
# --author='fangfang'

from models.httpTool import Http


def switch_position(session, positionId):
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
    if status == 200:
        if r_json["success"] is True:
            print("切换岗位成功：" + rt)
        else:
            print("切换岗位失败：" + rt)
    else:
        print("切换岗位失败：" + rt)
