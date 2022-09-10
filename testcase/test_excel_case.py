import json
from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Requests
import pytest
from common import Base
from utils.AssertUtil import AssertUtil
import re
from common.Base import init_db

# 1.初始化信息
# 1.初始化测试用例文件
case_file = os.path.join("../data", ConfigYaml().get_excel_file())
# 2.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 3.获取运行测试用例列表
data_init = Data(case_file, sheet_name)
run_list = data_init.get_run_data()
# 4.日志
log = my_log()

# 初始化
data_key = ExcelConfig.DataConfig


# 2.编写测试用例方法，参数化运行
class TestExcel:

    def run_api(self, url, method, param=None, header=None, cookie=None):
        """发送请求"""
        requests = Requests()
        # if len(str(params).strip()) is not 0:
        #     """验证params有没有内容"""
        #     params = json.loads(params)
        #     """把params转义json"""
        if str(method).lower() == "get":
            res = requests.get(url, params=param, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = requests.post(url, data=param, headers=header, cookies=cookie)
        else:
            log.error(f"错误请求method：{method}")
        # print(res)
        return res

    def run_pre(self, pre_case):
        """初始化数据"""
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]
        # 转义headers
        param = Base.json_parse(params)
        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, param, header, cookie)
        print(f"前置用例执行{res}")
        return res

    # 1.初始化信息，url,data

    # 1.增加pytest
    @pytest.mark.parametrize("case", run_list)
    # 把run_list列表内的每条用例赋值给case这样会执行所有可执行的用例
    # 2.修改方法参数
    def test_run(self, case):
        """执行可以执行接口测试用例"""
        # 3.重构函数内容
        url = ConfigYaml().get_conf_url() + case[data_key.url]
        params = case[data_key.params]
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        actual_result = case[data_key.actual_result]
        is_run = case[data_key.is_run]
        headers = case[data_key.headers]
        cookies = case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]
        # if headers:
        #     # 转义headers
        #     header = json.loads(headers)
        # else:
        #     header = headers
        # if cookies:
        #     # 转义cookies
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies

        # 验证前置条件
        if pre_exec:
            pre_case = data_init.get_case_pre(pre_exec)
            print(f"前置条件为：{pre_case}")
            pre_res = self.run_pre(pre_case)
            headers, cookies, params = self.get_correlation(headers, cookies, params, pre_res)
        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        param = Base.json_parse(params)
        res = self.run_api(url, method, param, header, cookie)
        print(f"测试用例执行{res}")

        # 断言验证
        # 状态码，返回结果内容，数据库相关的结果验证
        # 状态码
        assert_util = AssertUtil()
        assert_util.assert_code(int(res["code"]), int(code))
        assert_util.assert_in_body(str(res["body"]), str(expect_result))
        Base.assert_db("db_1", res["body"], db_verify)
        # 数据库结果断言
        # # 1.初始化数据库
        # sql = init_db("db_1")
        # # 2.查询sql，excel内容
        # db_res = sql.fetchone(db_verify)
        # log.debug(f"数据库查询结果:{str(db_res)}")
        # # 3.数据库的结果与接口返回的结果验证
        # # 获取数据库结果的key
        # verify_list = list(dict(db_res).keys())
        # # 根据key获取数据库结果，接口结果
        # for line in verify_list:
        #     res_line = res["body"][line]
        #     res_db_line = dict(db_res)[line]
        #     # 验证
        #     assert_util.assert_body(res_line, res_db_line)
        # 前置条件用例
        # 2.接口请求
        # requests = Requests()
        # if len(str(params).strip()) is not 0:
        #     """验证params有没有内容"""
        #     params = json.loads(params)
        #     """把params转义json"""
        # if str(method).lower() == "get":
        #     res = requests.get(url, params=params, headers=headers, cookies=cookie)
        # elif str(method).lower() == "post":
        #     res = requests.post(url, data=params, headers=header, cookies=cookie)
        # else:
        #     log.error(f"错误请求method：{method}")
        # print(res)

    def get_correlation(self, headers, cookies, params, pre_res):
        """关联"""
        headers_para, cookies_para, params_para = Base.params_find(headers, cookies, params)
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
            headers = Base.res_sub(headers, headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            cookies = Base.res_sub(cookies, cookies_data)
        if len(params_para):
            params_data = pre_res["body"]["result"][params_para[0]]
            params = Base.res_sub(params, params_data)
        return headers, cookies, params


if __name__ == '__main__':
    pass
    # str1 = '{"Authorization":"JWT ${token}$"}'
    # if "${" in str1:
    #     print(str1)
    # pattern = re.compile("\${.*}\$")
    # # 正则表达式获取\${.*}\$里的内容
    # re_res = pattern.findall(str1)
    # # 查找str1内和\${.*}\$匹配的内容
    # print(re_res[0])
    # # 打印一条
    # token = "123"
    # res = re.sub(pattern, token, str1)
    # # 替换token内容
    # print(res)
    pytest.main()
