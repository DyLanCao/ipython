import numpy as np

r = 10
c = 10

#D0 = np.zeros((11,11))
D0 = np.zeros((11,11),dtype=int)

D0[0, 1:] = 32767
D0[1:, 0] = 32767

for i in range(r):
        for j in range(c):
            D0[i + 1, j + 1] = 1 
print D0
