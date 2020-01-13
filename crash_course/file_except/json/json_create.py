
import json

numbers = [2,3,4,5,6,13]

filename = 'numbers.json'

with open(filename, 'w') as file_object:
    json.dump(numbers,file_object)

