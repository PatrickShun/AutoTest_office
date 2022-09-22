#! /usr/bin/env python
import sys
import unittest
import warnings

import case_template.login_case_template as template
from models.getconfig import Configure
import utils as utils

config = Configure()


class TestLoginPage(unittest.TestCase):

    def setUp(self):
        utils.setup()

    #输入空的username和正确的password登录
    def test_Null_Username_Correct_Password(self):
        case_desc = f'{self.__class__.__name__}\t{sys._getframe().f_code.co_name}'
        null_username = ''
        correct_password = config.password_correct
        er_message = '请输入账号'
        template.template_1(case_desc, null_username, correct_password, config.verification_code, er_message)

    #输入正确的username和空的password登录
    def test_Correct_Username_Null_Password(self):
        case_desc = f'{self.__class__.__name__}\t{sys._getframe().f_code.co_name}'
        correct_username = config.username_correct
        null_password = ''
        er_message = '请输入密码'
        template.template_1(case_desc, correct_username, null_password, config.verification_code, er_message)

    #输入空的username和空的password登录
    def test_Null_Username_Null_Password(self):
        case_desc = f'{self.__class__.__name__}\t{sys._getframe().f_code.co_name}'
        null_username = ''
        null_password = ''
        er_message = '请输入账号请输入密码'
        template.template_1(case_desc, null_username, null_password, config.verification_code, er_message)

    #输入正确的username和错误的password登录
    def test_Correct_Username_Wrong_Password(self):
        case_desc = f'{self.__class__.__name__}\t{sys._getframe().f_code.co_name}'
        correct_username = config.username_correct
        wrong_password = config.password_correct + '121'
        er_message = '用户名或密码错误'
        template.template_1(case_desc, correct_username, wrong_password, config.verification_code, er_message)

    #输入正确的username和password登录, 查看弹出框提示信息
    def test_Correct_Username_Correct_Password(self):
        case_desc = f'{self.__class__.__name__}\t{sys._getframe().f_code.co_name}'
        correct_username = config.username_correct
        correct_password = config.password_correct
        er_message = '''
        Need to verify your identity
        For your account security,please verify your identity
        135****6386
        SMS verification code
        Get Verification Code
        '''
        template.template_1(case_desc, correct_username, correct_password, config.verification_code, er_message)


if __name__ == "__main__":
    unittest.main()