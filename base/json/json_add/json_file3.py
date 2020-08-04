import json

a_file = open("netconfig.json","r")
json_object = json.load(a_file)
a_file.close()


data = json.dumps(json_object)
print(data)



