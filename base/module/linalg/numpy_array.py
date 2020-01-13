#coding=utf-8

import numpy as np
a = np.array([1,2,3,4,5])
print a
b = np.zeros((20,30))
print sum(b.shape)
c = np.arange(10)
print c
d = np.arange(2,10,dtype=np.float)
print d
e = np.linspace(1.0,4.0,6)
print e
f = np.indices((3,3))
print f
a = []
a.append((1,2,4))
a.append((2,3,4))
a = np.array(a)
a.flatten()
