b = b'\x12\x34\x12\x23\x01\x02\x02'
bb = b[:4]
n = int.from_bytes(bb,byteorder='big',signed=False)
print("nn:0x%x" % n)
cc = b[5:8]
nn = int.from_bytes(cc,byteorder='big',signed=False)
print("cc:0x%x" % nn)
#b'\x12\x34'->4660
 
n = 4097
b = n.to_bytes(length=2,byteorder='big',signed=False)
print(b)
#4660->b'\x12\x34'

