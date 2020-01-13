import numpy as np

x = np.array[[3,4],[4,5]]
y = 5
z = np.linalg.norm(x,ord=1)
#dest = lambda x, y: np.linalg.norm(x - y, ord=1)
#print(dest(2,3))
print(z)

