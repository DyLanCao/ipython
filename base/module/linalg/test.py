import numpy as np 
from numpy.linalg import norm
np.set_printoptions(threshold='nan')

a1 = np.array([1,2,3])
a2 = np.array([0,0,-3])
testa = np.array([[ 1.76405235,  0.40015721,  0.97873798],
    [ 2.2408932 ,  2.2677152 , -0.57712067],
    [ 0.95008842,  0.79873121, -0.68033952],
    [ 0.4105985 ,  0.55464207,  0.77393398]])
#dist=lambda x, y: norm(x - y, ord=1)
testb = np.array([[ 1.76405235,  0.40015721,  0.97873798],
    [ 2.2408932 ,  2.2677152 , -0.57712067],
    [ 0.95008842,  0.79873121, -0.68033952],
    [ 0.4105985 ,  0.55464207,  0.77393398]])
dist=lambda x, y: norm(x - y, ord=1)
#print(dist(testa,testb))
#print(dist(set(a1),set(a2)))
#print np.linalg.norm(2) # returns 2
print np.linalg.norm([2,-1,3,-4], np.inf) # returns 2,

print np.linalg.norm(a1 - a2, ord=1) # returns 2,
#print np.linalg.norm(a1, np.inf) # returns 3:
