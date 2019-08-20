#!/usr/bin/env python3
#with open('somefile.txt','rt') as f:
    #print('hello world', file=f)
    #f.write('hello world')
# Read the entire file as a single string
file = open('test5.txt','w') 
 
for cnt in range(0,1000):
	file.write(hex(ord('2'))[2:]+" ") 

file.close() 
