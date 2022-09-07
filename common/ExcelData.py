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

    def get_case_list(self):
        """获取全部测试用例"""
        run_list = list()
        for line in self.reader.data():
            run_list.append(line)
        return run_list

    def get_case_pre(self, pre):
        """在所有用例里根据前置条件获取用例，如果没有就返回None"""
        run_list = self.get_case_list()
        # 获取全部测试用例赋值给run_list
        for line in run_list:
            # 遍历列表内的用例赋值给line
            if pre in dict(line).values():
                # 如果pre（调用传的参数）是line这条用例里的values返回这条用例
                return line
        # 如果pre不是line这条用例里的values就返回空
        return None


if __name__ == '__main__':
    a = Data("../data/testdata.xls", "天气查询").get_case_pre("ABC")
    print(a)