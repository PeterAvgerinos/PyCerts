import numpy as np


a = np.zeros((7,7))
ones = np.ones((5,5))
ones[2,2] = 5
a[1:6,1:6] = ones
print(a)
