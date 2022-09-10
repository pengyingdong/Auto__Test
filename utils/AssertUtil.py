import json

from utils.LogUtil import my_log


# 1.定义封装类
class AssertUtil:
    # 2.初始化数据，日志
    def __init__(self):
        self.log = my_log("AssertUtil")

    # 3.code相等
    def assert_code(self, code, expected_code):
        """
        验证返回状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert int(code) == int(expected_code)
            return True
        except:
            self.log.error("code error,code is %s,expected_code is %s" % (code, expected_code))
            raise

    # 4.body相等
    def assert_body(self, body, expected_body):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except:
            self.log.error(f"body与expected_body不相等，实际返回的是：{body}预期返回是：{expected_body}")

    # 5.body包含
    def assert_in_body(self, body, expected_body):
        """
        验证返回结果是否包含预期的结果
        :param body:
        :param expected_body:
        :return:
        """
        try:
            # body = json.dumps(body)
            assert expected_body in body
        except:
            self.log.error(f"不包含body或者body是错误，body是：{body}expected_body是：{expected_body}")
            raise
