import json
from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Requests
import pytest
from common import Base

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

    def run_api(self, url, method, params=None, header=None, cookie=None):
        """发送请求"""
        requests = Requests()
        if len(str(params).strip()) is not 0:
            """验证params有没有内容"""
            params = json.loads(params)
            """把params转义json"""
        if str(method).lower() == "get":
            res = requests.get(url, params=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = requests.post(url, data=params, headers=header, cookies=cookie)
        else:
            log.error(f"错误请求method：{method}")
        return res

    def run_pre(self, pre_case):
        """初始化数据"""
        url = ConfigYaml().get_conf_url() + pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]
        # 转义headers
        header = Base.json_parse(headers)
        cookie = Base.json_parse(cookies)
        res = self.run_api(url, method, params, header, cookie)
        print(res)

    # 1.初始化信息，url,data

    # 1.增加pytest
    @pytest.mark.parametrize("case", run_list)
    # 把run_list列表内的每条用例赋值给case这样会执行所有可执行的用例
    # 2.修改方法参数
    def test_run(self, case):
        """执行可以执行接口测试用例"""
        # 3.重构函数内容
        data_key = ExcelConfig.DataConfig
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
        if headers:
            # 转义headers
            header = json.loads(headers)
        else:
            header = headers
        if cookies:
            # 转义cookies
            cookie = json.loads(cookies)
        else:
            cookie = cookies
        # 验证前置条件
        if pre_exec:
            pass

            pre_case = data_init.get_case_pre(pre_exec)
            print(f"前置条件为：{pre_case}")
            self.run_pre(pre_case)
            # 前置条件用例
        # 2.接口请求
        requests = Requests()
        if len(str(params).strip()) is not 0:
            """验证params有没有内容"""
            params = json.loads(params)
            """把params转义json"""
        if str(method).lower() == "get":
            res = requests.get(url, params=params, headers=headers, cookies=cookie)
        elif str(method).lower() == "post":
            res = requests.post(url, data=params, headers=header, cookies=cookie)
        else:
            log.error(f"错误请求method：{method}")
        print(res)


# TestExcel().test_run()
# 4.pytest.main
if __name__ == '__main__':
    pytest.main()