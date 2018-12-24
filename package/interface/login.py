# coding=utf-8
# --author='fangfang'

from httpTool import Http


def asset_login(username, password):
    # 实例化http请求
    http = Http()
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8"}
    url = "/api/asset/login"
    datas = {"account": username, "identifier": password}
    http.set_url(url)
    http.set_headers(headers)
    http.set_data(datas)
    r = http.postWithJson()
    status = r.status_code
    rt = r.text
    r_json = r.json()
    if status == 200:
        if r_json["success"] is True:
            print("登录成功：" + rt)
        else:
            print("登录失败：" + rt)
    else:
        print("登录失败：" + rt)


def get_session(username, password):
    http = Http()
    headers = {"Connection": "keep-alive", "Content-Type": "application/json;charset=UTF-8"}
    url = "/api/asset/login"
    datas = {"account": username, "identifier": password}
    http.set_url(url)
    http.set_headers(headers)
    http.set_data(datas)
    r = http.postWithJson()
    session_id = r.cookies["SESSION"]
    status = r.status_code
    rt = r.text
    r_json = r.json()
    if status == 200:
        if r_json["success"] is True:
            print("登录成功：" + rt)
        else:
            print("登录失败：" + rt)
    else:
        print("登录失败：" + rt)
    return session_id


if __name__ == "__main__":
    print(get_session("18519030809", "1adbb3178591fd5bb0c248518f39bf6d"))

