#! /usr/bin/env python
import os

from models.xlsx_write import XlsxWrite
from models.getconfig import Configure
import common as cons

config = Configure()
result_sheet = ['sum', 'cases']
sum_head = ['test_suite', 'PASS', 'FAIL', 'TOTAL', 'Passrate']
cases_head = ['test_suite', 'test_case', 'result', 'comment', 'time']


class Reporter(object):
    def __init__(self, dir_result, dir_log):
        self.dir_result = dir_result
        self.dir_log = dir_log
        if os.path.exists(self.dir_result):
            os.remove(self.dir_result)

    def write_result(self):
        summary = self.analysis_log()
        for test_suite, data in summary.items():
            pass_num, fail_num, total_num = 0, 0, 0
            for test_case, element in data.items():
                wb = XlsxWrite(self.dir_result, result_sheet[1], 1)
                wb.write_head(cases_head)
                wb.write_row_data([test_suite, test_case] + element)
                wb.save()
                if element[0] == cons.PASS_TAG:
                    pass_num += 1
                elif element[0] == cons.FAIL_TAG:
                    fail_num += 1
                total_num += 1
            passrate = str('%.2f'%float((pass_num / total_num) * 100)) + '%'
            wb = XlsxWrite(self.dir_result, result_sheet[0], 0)
            wb.write_head(sum_head)
            wb.write_row_data([test_suite, pass_num, fail_num, total_num, passrate])
            wb.save()

    def analysis_log(self):
        summary = {}
        for file in os.listdir(self.dir_log):
            dir_file = os.path.join(self.dir_log, file)
            f = open(dir_file, 'r', encoding='utf-8')
            for line in f.readlines():
                test_time, test_suit, test_case, result, comment = \
                    line.replace('\n', '').split('\t')
                data = [result, comment, test_time]
                if test_suit not in summary.keys():
                    summary.setdefault(test_suit, {}). \
                        setdefault(test_case, data)
                else:
                    if test_case not in summary[test_suit].keys():
                        summary[test_suit].setdefault(test_case, data)
                    else:
                        summary[test_suit][test_case] = data

        return summary


if __name__ == "__main__":
    reporter = Reporter(config.dir_result, config.log_path)
    reporter.write_result()
