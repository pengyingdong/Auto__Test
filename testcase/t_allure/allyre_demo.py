import pytest
import allure
# 测试方法
import pytest


@allure.feature("这是一个模块")
# 定义一个模块下面用story
class AllureCase:
    @allure.title("测试用例test1")
    # 定义用例的标题/方法名
    @allure.description("test1这条用例是打印内容")
    # 定义测试用例的详细说明
    @allure.story("这是模块下的一个功能")
    # 定义模块下的小功能,如果这个装饰器内容一样两个方法会归到同一个小模块内
    @allure.severity(allure.severity_level.BLOCKER)
    # 定义用例级别，主要有BLOCKER,CRITICAL,MINOR,NORMAL,TRIVIAL默认是NORMAL
    def test_1(self):
        print("test1")

    @allure.title("测试用例test2")
    @allure.description("test2这条用例是打印内容")
    @allure.story("这是模块下的一个功能")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test2")

    @allure.title("测试用例test2")
    @allure.description("test2这条用例是打印内容")
    @allure.story("这是模块下的一个功能")
    @allure.severity(allure.severity_level.NORMAL)
    def test_3(self):
        print("test3")

    @pytest.mark.parametrize("case", ["case1", "case2"])
    def test_4(self, case):
        print(case)
        allure.dynamic.title(case)
        # 动态设置相关配置，这条用例的标题会产生两个


if __name__ == '__main__':
    pytest.main(["allure_demo.py"])
