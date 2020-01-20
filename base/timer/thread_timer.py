#! /usr/bin/python3
#! -*- conding: utf-8 -*-
import threading
import time
def fun_timer():
    print(time.strftime('%Y-%m-%d %H:%M:%S'))
    global timer
    timer = threading.Timer(2,fun_timer)
    timer.start();
timer = threading.Timer(1,fun_timer)
timer.start();
time.sleep(5)
timer.cancel()
print(time.strftime('%Y-%m-%d %H:%M:%S'))
