import json

a_file = open("netconfig.json","r")
json_object = json.load(a_file)
a_file.close()
print(json_object)

json_object["ssid"] = "vision"

a_file=open("netconfig.json","w")
json.dump(json_object,a_file)
a_file.close()

