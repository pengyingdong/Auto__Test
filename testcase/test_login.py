from config import Conf
import os
from utils.YamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Requests
from utils.AssertUtil import AssertUtil

# 1.获取测试用例内容list
# 获取testlogin.yml文件路径
test_file = os.path.join(Conf.get_data_path(), "testlogin.yml")
# 使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()
print(data_list)


# 2.参数化执行测试用例
@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    # 初始化url,data
    url = ConfigYaml().get_conf_url() + login["url"]
    data = login["data"]
    # post请求
    requests = Requests()
    res = requests.post(url, data=data)
    # 打印结果
    print(res)
    r = res["code"]
    a = AssertUtil()
    a.assert_code(r, login["expect"]['code'])
