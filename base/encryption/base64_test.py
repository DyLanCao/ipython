# -*- coding: utf-8 -*-
# coding=utf-8
import base64

print("example one")
encode = base64.b64encode(b'I love you')

print(encode)

decode = base64.b64decode(encode)

print(decode)

print("example two")

encode = base64.b64encode(b'I love you$$$$$$$$$$$$$$$$$$$$$$$$$$$$@@@@@@@@@@@@@@@@@@@@@MMMMMMMMMMMMMMMMMMM')

print(encode)

decode = base64.b64decode(encode)

print(decode)


