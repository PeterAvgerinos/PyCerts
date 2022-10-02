import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    data = np.array(list, [3,3])
    print(data)

data = np.array(list)
data = data.reshape((3,3))
print(data)
