import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    data = np.array(list, [3,3])
    print(data)

try:
    data = np.array(list)
    data = data.reshape((3,3))
    data = data.reshape(9)
    print(data)
    calculations = {}
    mean = 

except ValueError:
    print("List must contain nine numbers.")
