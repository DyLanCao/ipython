from pytlv.TLV import *
import json

data = {"Username":"dylan","age":16}
jsondata = json.dumps(data)
print(jsondata)
tlv = TLV(['89ABCDEF', '9F04'])
test = '1234567890' + repr(jsondata)
print(len(test))
print(test)
data = tlv.build({'89ABCDEF': test})
print(data)
text = tlv.parse(data)
print(text)

'''
test1 = 'Ab0000'
print(len(test1))
data1 = tlv.build({'9f04': test1 + jsondata})
print(data1)
text1 = tlv.parse(data1)
print(text1)
'''
