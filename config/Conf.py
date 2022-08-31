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

# 定义data目录的路径
_data_path = BASE_DIR + os.sep + "data"

# 定义db_conf.yml路径
_db_config_file = _config_path + os.sep + "db_conf.yml"


def get_data_path():
    return _data_path


def get_db_config_file():
    return _db_config_file


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def gei_log_path():
    return _log_path


# 2.读取配置文件
class ConfigYaml:
    def __init__(self):
        """定义方法获取需要信息"""
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    def get_excel_file(self):
        """获取excel文件名"""
        return self.config["BASE"]["test"]["case_file"]

    def get_excel_sheet(self):
        """获取excel内sheet的名称"""
        return self.config["BASE"]["test"]["case_sheet"]

    def get_conf_url(self):
        """获取配置文件内的url"""
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        """获取日志级别"""
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        """获取文件扩展名"""
        return self.config["BASE"]["log_extension"]

    def get_db_conf_info(self, db_alias):
        """获取数据库基本信息"""
        return self.db_config[db_alias]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    # # print(conf_read.get_conf_url())
    # # print(conf_read.get_conf_log())
    # # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_conf_info("db_1"))
    print(conf_read.get_excel_file())
    print(conf_read.get_excel_sheet())
