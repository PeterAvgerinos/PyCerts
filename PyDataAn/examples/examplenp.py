import numpy as np

a = np.array(([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
b = np.max(a, axis=1).sum()
c = a.reshape((5,2))
print(a)
print(c)
