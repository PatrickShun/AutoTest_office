#! /usr/bin/env python
import os

from models.getconfig import Configure
from models.account import Account
from models.compare import Compare
import utils as utils

config = Configure()

'''Login case模板1
|- args:
   case_desc: <str> 类型\t方法名;
   username: <str> 用户名;
   password: <str> 密码；
   er_result: <str>, <list>[1, 2, 3], <dict>{1:[1,2,3], 2:4, 'k':'value'} 期望结果；
|- returns: 无
   将测试结果写入log文件中
'''


def template_1(case_desc, username, password, verifi_code, er_result):
    account = Account(username, password, verifi_code)
    tr_result = account.get_login_message()
    cmp = Compare(er_result, tr_result)
    result, comment = cmp.cmp_result()
    run_data = f'{utils.time_stamp()}\t{case_desc}\t{result}\t{comment}'
    print(run_data)
    log_file = os.path.join(config.log_path, case_desc.split('\t')[0])
    utils.write_Run_Log(log_file, run_data)

