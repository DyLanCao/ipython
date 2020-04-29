import json

file = open('stus.json',encoding='utf-8')
file_lines =file.read()
file.close()

file_json = json.loads(file_lines)

json_txt = []
print(file_json)
file_json["xiaohei"] = str("ssid")
print(file_json)


