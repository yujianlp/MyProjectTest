# coding=utf-8
from Business.Login import Login
import unittest
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class TCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # 定义正确登陆的测试用例
    def test_001(self):
        log = Login()
        # 用账号密码登录
        log.login('laopi', '123456')
        # 获取登录之后的用户名
        data = log.get_text('class', 'loginfo')
        # print(data)
        # 断言，判断登录后的用户名是否和预期用户名相同
        self.assertEqual('laopi您好，欢迎您来到iwebshop购物！[安全退出]', data)

    # # 账号密码都不输入，直接登录
    # def test_002(self):
    #     log = Login()
    #     # 用账号密码登录
    #     log.login('', '')
    #     # 获取登录之后的用户名
    #     data = log.get_text('css', '.invalid-msg')
    #     # print(data)
    #     # 断言，判断登录后的用户名是否和预期用户名相同
    #     self.assertEqual('填写用户名或邮箱', data)
    #
    # # 只输入账号不输入密码，直接登录
    # def test_003(self):
    #     log = Login()
    #     # 用账号密码登录
    #     log.login('laopi', '')
    #     # 获取登录之后的用户名
    #     data = log.get_text('css', '.invalid-msg')
    #     # print(data)
    #     # 断言，判断登录后的用户名是否和预期用户名相同
    #     self.assertEqual('填写密码', data)
    #
    # # 只输入账号不输入密码，直接登录
    # def test_004(self):
    #     log = Login()
    #     # 用账号密码登录
    #     log.login('laopi', '')
    #     # 获取登录之后的用户名
    #     data = log.get_text('css', '.invalid-msg')
    #     # print(data)
    #     # 断言，判断登录后的用户名是否和预期用户名相同
    #     self.assertEqual('请输入密码11111', data)

if __name__ == '__main__':
    unittest.main()
