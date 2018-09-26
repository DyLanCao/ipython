def average(seq): 
	return float(sum(seq)) / len(seq)

def MaxMinNormalization(x,Max,Min):  
    x = (x - Min) / (Max - Min);  
    return x;  

def Z_ScoreNormalization(x,mu,sigma):  
    x = (x - mu) / sigma;  
    return x;  

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

### two
import numpy as np
from sklearn.preprocessing import normalize

x = np.random.rand(1000)*10
#print(MaxMinNormalization(x,10,0))
#print(Z_ScoreNormalization(x, 5, 0))
print(average(x))
print(x.mean())

norm1 = x / np.linalg.norm(x)
#print norm1
norm2 = normalize(x[:,np.newaxis], axis=0).ravel()
#print norm2
print np.all(norm1 == norm2)
# True



