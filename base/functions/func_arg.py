#!/usr/bin/env python3

def avg(first, *rest):
    return (first +sum(rest)) / (1 + len(rest))

print(avg(1,5))
print(avg(1,4,3,4))
'''
def recv(maxsize, *, block):
    'Receives a message'
    pass
'''
#recv(1024,True)
def mininum(*values, clip = None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1,5,2,-5,10)
