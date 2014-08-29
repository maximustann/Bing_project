#!/bin/env python
import time
import datetime
import inspect

def lineno():
    return inspect.currentframe().f_back.f_lineno
def write_log(error_message, line_no):
    fd = None
    my_time = None
    line_no = "|" + str(line_no) + "|"
    fd = open("../Database/log/log.txt", "a")
    my_time = str(time.strftime("%Y-%m-%d-%I:%M", time.localtime(time.time())))
    print >> fd, error_message, line_no, my_time
    fd.close()
