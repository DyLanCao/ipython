import numpy as np
x=np.array([[1, 3], [2, 6]])

y=np.linalg.norm(x, ord=1)

print(y)
z=x/y
