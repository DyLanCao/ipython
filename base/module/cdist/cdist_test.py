from scipy.spatial.distance import cdist 
from numpy import array, zeros, argmin, inf, equal, ndim
from sklearn.metrics.pairwise import manhattan_distances
dist_fun = manhattan_distances
import numpy as np

r = 10
c = 10
D0 = zeros((r + 1, c + 1),dtype=np.int)
#D0 = zeros((r + 1, c + 1))
D0[0, 1:] = 32767
D0[1:, 0] = 1000
x = [0, 0, 1, 1, 2, 4, 2, 1, 2, 0]
y = [1, 1, 1, 2, 2, 2, 2, 3, 2, 0]
#x = [10, 1, 10, 5, 5, 4]
#y = [1, 2, 3, 4, 5, 5]
D1 = D0[1:, 1:] # view
for i in range(r):
    for j in range(c):
        D0[i+1, j+1] = abs(x[i] - y[j])

for i in range(r):
    for j in range(c):
        D1[i, j] += min(D0[i, j], D0[i, j+1], D0[i+1, j])
        print "D1:%d min:%d" % (D1[i,j],min(D0[i,j],D0[i,j+1],D0[i+1,j]))

print "D1"
print D0
print D1
print D1[-1][-1]
#print sum(D1.shape)
#print D1[-1, -1] / sum(D1.shape)

