import requests


def requests_get(url, params):
    # 定义requests_get封装方法
    a = requests.get(url, params=params)
    # 发起gte请求
    code = a.status_code
    # 获取code码
    try:
        json = a.json()
    except Exception as e:
        json = a.text
    # 判断返回的结果是json或者是text
    r = dict()
    r["code"] = code
    r["json"] = json
    # 将返回的结果放到一个空字典里
    return r


def requests_post(url, data=None, json=None):
    # 定义requests_post封装方法
    a = requests.post(url, data=data, json=json)
    # 发起post请求
    code = a.status_code
    # 获取code码
    try:
        json = a.json()
    except Exception as e:
        json = a.text
    # 判断返回的结果是json或者是text
    r = dict()
    r["code"] = code
    r["json"] = json
    # 将返回的结果放到一个空字典里
    return r
