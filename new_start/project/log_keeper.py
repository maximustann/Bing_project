#!/bin/env python
import time
import datetime

def write_log(error_message):
    fd = None
    my_time = None
    fd = open("../Database/log/log.txt", "a")
    my_time = str(time.strftime("%Y-%m-%d-%I:%M", time.localtime(time.time())))
    print >> fd, error_message, my_time
    fd.close()
