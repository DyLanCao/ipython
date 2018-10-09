#-*-coding:utf-8-*-

import numpy as np
np.shape(0)

print "......................."

print np.shape([[1],[2],[3]])

arraya = np.array([[ 1.,  0.,  0.],  
       [ 0.,  1.,  0.],  
       [ 0.,  0.,  1.]]) 

print "......................."
e = np.eye(3)
print e
print "......................."
print arraya
print "......................."
print np.ones((3,2))
print "......................."
print np.zeros((3,2,8))


print "......................."
n = np.arange(0,30,2) #start at o count up by 2 stop before 30
print n


print "......................."
n = n.reshape(3,5) #start at o count up by 2 stop before 30
print n

print "......................."
n = np.linspace(0,4,9) #start at o count up to 4 divided by 9
print n


print "......................."
n = n.reshape(3,3) #start at o count up by 2 stop before 30
print n
