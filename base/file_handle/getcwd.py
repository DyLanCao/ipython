#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys

# 切换到 "/var/www/html" 目录
os.chdir("/Users/caoyin/Documents/igihub/ipython/base/file_handle" )

# 打印当前目录
print("当前工作目录 : %s" % os.getcwd())

# 打开 "/tmp"
fd = os.open( "/Users/caoyin/Documents/igihub/ipython/base", os.O_RDONLY )

# 使用 os.fchdir() 方法修改目录
os.fchdir(fd)

# 打印当前目录
print("当前工作目录 : %s" % os.getcwd())

# 关闭文件
os.close( fd )
