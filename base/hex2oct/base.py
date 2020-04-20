#!/usr/bin/python3

aa='\xa5\x5a'
print(aa.encode())
bb=int("0x1234567890", 0)
print(bb)
cc=int("1234567890", 16)
print(cc)
#print(int("fe43", 16))
print(bytes.fromhex('7370616d'))    # b'spam'
print(bytes.hex(b'spam'))    # b'spam'
