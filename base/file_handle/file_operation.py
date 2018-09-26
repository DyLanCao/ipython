#!/usr/bin/env python3
#with open('somefile.txt','rt') as f:
    #print('hello world', file=f)
    #f.write('hello world')
# Read the entire file as a single string
file = open('testfile.txt','w') 
 
file.write("Hello World\n\t") 
file.write("This is our new text file\n\t") 
file.write("and this is another line.\n\t") 
file.write("Why? Because we can.\n\t") 
  
file.close() 
