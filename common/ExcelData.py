from utils.ExcelUtil import ExcelReader
from common.ExcelConfig import DataConfig


class Data:
    # 1.使用excel工具类，获取结果list
    def __init__(self, testcase_file, sheet_name):
        self.reader = ExcelReader(testcase_file, sheet_name)
        # 2.列是否运行内容，y

    def get_run_data(self):
        run_list = list()
        for line in self.reader.data():
            if str(line[DataConfig().is_run]).lower() == "y":
                # print(line)
                # 3.保存要执行结果，放到新的列表
                run_list.append(line)
        return run_list


