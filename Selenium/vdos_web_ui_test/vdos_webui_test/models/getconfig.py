#! /usr/bin/env python

import configparser
import os

PWD = os.path.split(os.path.abspath(__file__))[0]
PPWD = os.path.dirname(PWD)
CONFIG_FILE = os.path.join(PPWD, 'config.ini')


class Configure(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(CONFIG_FILE, encoding='utf-8')

        # account info
        self.username_correct = self.conf.get("config", "username_correct")
        self.password_correct = self.conf.get("config", "password_correct")
        self.verification_code = self.conf.get("config", "verification_code")

        # path中的设置
        self.result_folder = os.path.join(PPWD, self.conf.get("path", "result_folder"))
        self.log_path = os.path.join(PPWD, self.conf.get("path", "log_folder"))
        self.dir_result = os.path.join(self.result_folder, 'result.xlsx')


