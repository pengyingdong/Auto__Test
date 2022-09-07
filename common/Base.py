import json
import re
from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql

p_data = '\${(.*)}\$'


# 1.定义init_db
def init_db(db_alias):
    # 2.初始化数据库信息，通过配置
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    charset = db_info["db_charset"]
    port = int(db_info["db_port"])

    # 3.初始化mysql对象
    conn = Mysql(host, user, password, db_name, charset, port)
    print(conn)
    return conn


def json_parse(data):
    """格式化字符，转换json"""
    return json.loads(data) if data else data


def res_find(data, pattern_data=p_data):
    """查询headers内的token"""
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res


def res_sub(data, replace, pattern_data=p_data):
    """查询headers内的token替换到下个用例的请求里"""
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data, replace, data)
    return re_res


def params_find(headers, cookies, params):
    """验证请求中是否有${}$需要结果关联的"""
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    if "${" in params:
        params = res_find(params)
    return headers, cookies, params


if __name__ == '__main__':
    # init_db("db_1")
    print(res_find('{"city": "${city}$","key": "2dadd5618a277d261b4eb0733fb956c9"}'))

    print(res_sub('{"city": "${city}$"}', "上海"))
