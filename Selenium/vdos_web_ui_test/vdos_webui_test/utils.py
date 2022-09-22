#! /usr/bin/env python
import datetime
import warnings


def setup():
    warnings.simplefilter("ignore", ResourceWarning)
    warnings.simplefilter("ignore", OSError)


def time_stamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_Run_Log(log_path, data):
    f = open(log_path, 'a', encoding='utf-8')
    f.write(data + '\n')
    f.close()


