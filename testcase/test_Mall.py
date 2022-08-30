import json
import pytest
from utils.RequestsUtil import Requests
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
from common.Base import init_db


def test_weather():
    # url = "http://apis.juhe.cn/simpleWeather/query"
    urls = ConfigYaml()
    url = urls.get_conf_url() + "/simpleWeather/query"
    data = {"city": "上海",
            "key": "2dadd5618a277d261b4eb0733fb956c9"
            }
    response = Requests()
    r = response.post(url, data=data)
    # 发起get请求-
    print(r)
    # 打印结果
    code = r["code"]
    AssertUtil().assert_code(code, 200)
    # assert code == 200
    body = (r["json"])
    AssertUtil().assert_in_body(body, '"error_code": 0')
    # assert "'reason': '查询成功!'" in body
    conn = init_db("db_1")
    a_db = conn.fetchone("select id from student where name = '涛涛'")
    print(f"查询结果id：{a_db}")
    user_name = body["error_code"]
    print(user_name)
    assert user_name != a_db


if __name__ == '__main__':
    pytest.main()

    # 调用方法
