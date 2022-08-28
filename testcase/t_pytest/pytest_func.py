import pytest


# 1.定义类
class TestFunc:
    # 2.创建测试方法test开头
    # 创建setup，teardpwn
    def setup(self):
        print("---setup---")

    def teardown(self):
        print("---teardown---")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")


# 3.创建setup，teardown

# 4.运行查看结果
