import json
from config.Conf import ConfigYaml
import os
from common.ExcelData import Data
from utils.LogUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Requests

# 1.初始化信息
# 1.初始化测试用例文件
case_file = os.path.join("../data", ConfigYaml().get_excel_file())
# 2.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
# 3.获取运行测试用例列表
run_list = Data(case_file, sheet_name).get_run_data()
# 4.日志
log = my_log()


# 2.编写测试用例方法，参数化运行
class TestExcel:
    # 1.初始化信息，url,data
    def test_run(self):
        data_key = ExcelConfig.DataConfig
        url = ConfigYaml().get_conf_url() + run_list[0][data_key.url]
        params = run_list[0][data_key.params]
        case_id = run_list[0][data_key.case_id]
        case_model = run_list[0][data_key.case_model]
        case_name = run_list[0][data_key.case_name]
        pre_exec = run_list[0][data_key.pre_exec]
        method = run_list[0][data_key.method]
        params_type = run_list[0][data_key.params_type]
        params = run_list[0][data_key.params]
        expect_result = run_list[0][data_key.expect_result]
        actual_result = run_list[0][data_key.actual_result]
        is_run = run_list[0][data_key.is_run]
        headers = run_list[0][data_key.headers]
        cookies = run_list[0][data_key.cookies]
        code = run_list[0][data_key.code]
        db_verify = run_list[0][data_key.db_verify]

        # 2.接口请求
        requests = Requests()
        if len(str(params).strip()) is not 0:
            """验证params有没有内容"""
            params = json.loads(params)
            """把params转义json"""
        if str(method).lower() == "get":
            res = requests.get(url, params=params)
        elif str(method).lower() == "post":
            res = requests.post(url, data=params)
        else:
            log.error(f"错误请求method：{method}")
        print(res)


TestExcel().test_run()
