#!/usr/bin/python
import json

jsonData = '{"hello":1,"b2":2,"c":"test","d":4,"e":5}';

text = json.loads(jsonData)
print text
