import pytest
from utils.RequestsUtil import Requests

login_data = [{"url": "http://apis.juhe.cn/simpleWeather/query",
               "data": {"city": "项城",
                        "key": "2dadd5618a277d261b4eb0733fb956c9"}},
              {"url": "http://apis.juhe.cn/simpleWeather/query",
               "data": {"city": "上海",
                        "key": "ec6c4a9c755ba57c4b9ef5572e452dca"}}
              ]


@pytest.mark.parametrize("login", login_data)
def test_1(login):
    url = login["url"]
    data = login["data"]
    print("测试用例中login的值:%s%s" % (url, data))
    response = Requests()
    res = response.post(url, data=data)
    print("请求结果：%s" % res)


if __name__ == '__main__':
    pytest.main()
