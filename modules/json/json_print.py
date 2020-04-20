# coding= utf-8
#!/usr/bin/python
import json
import sys

data = {"username":"测试","age":16}

#jsondata = json.dumps(data,ensure_ascii=False)
jsondata = json.dumps(data)
print("data convert to json")
print type(json)
text = json.loads(jsondata)
print("json convert to data")
print text["username"]
print text["age"]

