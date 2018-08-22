# -*- coding: utf-8 -*-
# coding=utf-8
#from Cryptodome.Cipher import DES
#from Crypto import DES


from Crypto.Cipher import DES

import binascii

key = b'abcdefgh'

des = DES.new(key, DES.MODE_ECB)

text = 'python example hhhh'
text = text + (8 - (len(text) % 8)) * '='

encrypto_text = des.encrypt(text.encode())
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)


