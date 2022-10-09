import json
import re
import subprocess

from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
from utils.AssertUtil import AssertUtil
from utils.LogUtil import my_log
from utils.EmailUtil import SendEmail

p_data = '\${(.*)}\$'
log = my_log()


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


def assert_db(db_name, result, db_verify):
    assert_util = AssertUtil()
    # 1.初始化数据库
    # sql = init_db("db_1")
    db_res = sql = init_db(db_name)
    # 2.查询sql，excel内容
    db_res = sql.fetchone(db_verify)
    log.debug(f"数据库查询结果:{str(db_res)}")
    # 3.数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        # res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)


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


def allure_report(report_path, report_html):
    """生成allure报告"""
    allure_cmd = f"allure generate {report_path} -o {report_html} --clean"
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查一下测试环境相关配置")
        raise


def send_mail(report_html_path="", content="", title="测试"):
    """发送邮件"""
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.semd_mail()


if __name__ == '__main__':
    # init_db("db_1")
    print(res_find('{"city": "${city}$","key": "2dadd5618a277d261b4eb0733fb956c9"}'))

    print(res_sub('{"city": "${city}$"}', "上海"))
