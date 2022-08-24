import requests
from utils.RequestsUtil import Requests


def get_weather():
    url = "http://apis.juhe.cn/simpleWeather/query"
    data = {"city": "上海",
            "key": "2dadd5618a277d261b4eb0733fb956c9"
            }
    response = Requests()
    r = response.post(url, data=data)
    # 发起get请求
    print(r)
    # 打印结果


if __name__ == '__main__':
    get_weather()
    # 调用方法
