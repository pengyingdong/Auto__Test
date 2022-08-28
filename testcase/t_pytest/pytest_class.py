import pytest


class TestClass:
    def setup_class(self):
        print("---setup_class---")

    def teardown_class(self):
        print("---teardown_class---")

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")


if __name__ == '__main__':
    pytest.main()
