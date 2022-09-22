#! /usr/bin/env python

from models.getconfig import Configure
import common as cons

config = Configure()


class Compare(object):
    def __init__(self, er, tr):
        self.er = er
        self.tr = tr

    ''' 对比结果
    |- args:
       er:  str, list[1,2,3], dict{1:[1,2,3], 2:4, 'k':'value'}类型;
       tr:  str, list[1,2,3], dict{1:[1,2,3], 2:4, 'k':'value'}类型;
    |- return:
       set：result, comment;
    '''
    def cmp_result(self):
        er , tr = '', ''
        if isinstance(self.er, list):
            er = self.__list_to_str(self.er)
            tr = self.__list_to_str(self.tr)
        elif isinstance(self.er, dict):
            er = self.__dict_to_str(self.er)
            tr = self.__dict_to_str(self.tr)
        elif isinstance(self.er, str):
            er = self.er.replace('\n', '').replace(' ', '')
            tr = self.tr.replace('\n', '').replace(' ', '')
        if er:
            if er == tr:
                result, comment = cons.PASS_TAG, f'{er} = {tr}'
            else:
                result, comment = cons.FAIL_TAG, f'{er} != {tr}'
        else:
            print("不支持的结果类型，请检查后重试....")
            result, comment = '', ''
        return result, comment

    # list转str
    def __list_to_str(self, l):
        return ''.join([str(element) for element in l])

    # dict转str
    def __dict_to_str(self, d):
        for k, v in d.items():
            if isinstance(v, list):
                return str(k) + self.__list_to_str(v)
            elif isinstance(v, str):
                return str(k) + v
            elif isinstance(v, int):
                return str(k) + str(v)


if __name__ == "__main__":
    er = {1: [1, 2, 3], 2: 3, 'k': 'v'}
    tr = {1: [2, 2, 3], 2: 3, 'k': 'v'}
    cmp = Compare(er, tr)
    result, comment = cmp.cmp_result()
    print(result, comment)