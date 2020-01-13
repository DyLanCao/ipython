import json

f = open('stus.json',encoding='utf-8')
user_dic = json.load(f)
print(user_dic)
