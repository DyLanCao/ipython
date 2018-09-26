#!/usr/bin/env python3
#with open('somefile.txt','rt') as f:
    #print('hello world', file=f)
    #f.write('hello world')
# Read the entire file as a single string
import os
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
        print('File already exists!')
