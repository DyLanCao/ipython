import json

file = open('stus.json',encoding='utf-8')
file_lines =file.read()

file_json = json.loads(file_lines)

json_txt = []
print(file_json)
file_json["xiaohei"] = str("ssid")

file.write(str(file_json))
print(file_json)

file.close()

