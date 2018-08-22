# -*- coding: utf-8 -*-
# coding=utf-8
import hashlib

print("example one")
str = "this is a md5 test"

h1 = hashlib.md5()

h1.update(str.encode(encoding='utf-8'))

print("MD5 ency before:" + str)
print("MD5 ency after:" + h1.hexdigest())


print("example two")
str = "this is a md5 testQQQQQQQQQQQQQQQQQQQQQQqAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

h1 = hashlib.md5()

h1.update(str.encode(encoding='utf-8'))

print("MD5 ency before:" + str)
print("MD5 ency after:" + h1.hexdigest())

