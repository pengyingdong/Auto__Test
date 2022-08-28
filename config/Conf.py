# 1.获取项目基本目录
import os
from utils.YamlUtil import YamlReader

# 获取当前项目的绝对路径
current = os.path.abspath(__file__)  # abspath当前文件
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)
# 定义config目录的路径   变量前加_是私有变量
_config_path = BASE_DIR + os.sep + "config"

# 定义conf.yml文件的路径
_config_file = _config_path + os.sep + "conf.yml"

# 定义logs文件路径
_log_path = BASE_DIR + os.sep + "logs"


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def gei_log_path():
    return _log_path


# 2.读取配置文件
class ConfigYaml:
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()

    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    print(conf_read.get_conf_log())
    print(conf_read.get_conf_log_extension())