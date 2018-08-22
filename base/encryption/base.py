# -*- coding: utf-8 -*-
# coding=utf-8
import time
from datetime import datetime   #这个要from引用，否则 datetime.fromtimestamp 会报错
dt = time.time()        # 获取当前的时间戳         1507384502.2770934
t0 = time.gmtime()       # 将时间戳转换成结构化时间元组（UTC时区）伦敦时区    time.struct_time(tm_year=2017, tm_mon=10, tm_mday=7, tm_hour=14, tm_min=0, tm_sec=39, tm_wday=5, tm_yday=280, tm_isdst=0)
t1 = time.localtime()    # 将时间戳转换成结构化时间元组（UTC+8时区）北京时区      time.struct_time(tm_year=2017, tm_mon=10, tm_mday=7, tm_hour=22, tm_min=0, tm_sec=39, tm_wday=5, tm_yday=280, tm_isdst=0)
print(dt)
print(t0)
print(t1)
print(datetime.fromtimestamp(dt))           #2017-10-07 22:00:39.674642
print(time.strftime('%Y-%m-%d %H:%M:%S'))   #2017-10-07 22:00:39
print(time.gmtime(1498488176.3209014))  #time.struct_time(tm_year=2017, tm_mon=6, tm_mday=26, tm_hour=14, tm_min=42, tm_sec=56, tm_wday=0, tm_yday=177, tm_isdst=0)
