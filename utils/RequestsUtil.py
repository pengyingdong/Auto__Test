import requests
from utils.LogUtil import my_log


class Requests:

    def __init__(self):
        self.log = my_log("Reqiests")

    def requests_api(self, url, params=None, data=None, json=None, headers=None, cookies=None, method="get"):
        # 定义公共方法
        if method == "get":
            # 如果method是gte执行下面的代码
            self.log.debug("发送get请求")
            a = requests.get(url, params=params, headers=headers, cookies=cookies)
        elif method == "post":
            # 如果method是post执行下面的代码
            self.log.debug("发送post请求")
            a = requests.post(url, data=data, json=json, headers=headers, cookies=cookies)
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

    def get(self, url, **kwargs):
        # 定义方法
        return self.requests_api(url, method="get", **kwargs)
        # 调用公共方法

    def post(self, url, **kwargs):
        # 定义方法
        return self.requests_api(url, method="post", **kwargs)
        # 调用公共方法
    # def requests_get(url, params):
    #     # 定义requests_get封装方法
    #     a = requests.get(url, params=params)
    #     # 发起gte请求
    #     code = a.status_code
    #     # 获取code码
    #     try:
    #         json = a.json()
    #     except Exception as e:
    #         json = a.text
    #     # 判断返回的结果是json或者是text
    #     r = dict()
    #     r["code"] = code
    #     r["json"] = json
    #     # 将返回的结果放到一个空字典里
    #     return r
    #
    #
    # def requests_post(url, data=None, json=None):
    #     # 定义requests_post封装方法
    #     a = requests.post(url, data=data, json=json)
    #     # 发起post请求
    #     code = a.status_code
    #     # 获取code码
    #     try:
    #         json = a.json()
    #     except Exception as e:
    #         json = a.text
    #     # 判断返回的结果是json或者是text
    #     r = dict()
    #     r["code"] = code
    #     r["json"] = json
    #     # 将返回的结果放到一个空字典里
    #     return r
