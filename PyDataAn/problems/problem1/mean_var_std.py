import numpy as np

list = [0,1,2,3,4,5,6,7,8]

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    data = np.array(list)
    data = data.reshape((3,3))
    calculations = {}
    mean = [np.mean(data, axis=0, dtype=np.float32), np.mean(data, axis=1, dtype=np.float32), np.mean(data, dtype=np.float32)]
    variance = [np.var(data, axis=0, dtype=np.float32), np.var(data, axis=1, dtype=np.float32), np.var(data, dtype=np.float32)]
    standard_deviation = [np.std(data, axis=0, dtype=np.float32), np.std(data, axis=1, dtype=np.float32), np.std(data, dtype=np.float32)]
    maximum = [np.max(data, axis=0), np.max(data, axis=1), np.max(data)]
    minimum = [np.min(data, axis=0), np.min(data, axis=1), np.min(data)]
    total = [np.sum(data, axis=0, dtype=np.int32), np.sum(data, axis=1, dtype=np.int32), np.sum(data, dtype=np.int32)]
    calculations = {'mean' : mean,
            'variance' : variance,
            'standard_deviation' : standard_deviation,
            'maximum' : maximum,
            'minimum' : minimum,
            'total' : total}
    return calculations

print(calculate(list))
