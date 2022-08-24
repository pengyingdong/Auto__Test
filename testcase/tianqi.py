import requests
from utils.RequestsUtil import requests_get
from utils.RequestsUtil import requests_post
import json


def get_weather():
    url = "http://apis.juhe.cn/simpleWeather/query"
    data = {"city": "上海",
            "key": "2dadd5618a277d261b4eb0733fb956c9"
            }
    jsons = json.dumps(data)
    response = requests_post(url, json=jsons)
    # 发起get请求
    print(response)
    # 打印结果


if __name__ == '__main__':
    get_weather()
    # 调用方法
