from pytlv.TLV import *

tlv = TLV(['12345678', '9F04'])
data = tlv.build({'12345678': '30001111111111111111222222222222222222222222223333333333'})
print(data)
text = tlv.parse(data)
print(text)
