import numpy as np

def calculate(arr):
    if (len(arr) != 9) or not all(type(i) in [int, float] for i in arr):
        raise ValueError('List must contain nine numbers.')

    matr = np.reshape(arr, newshape=(3,3))
    
    def oper(fn):
        return [[fn(matr[:,i]) for i in range(3)],[fn(matr[i,:]) for i in range(3)], fn(arr)]
    
    
    return {
        'mean': oper(np.mean),
        'variance': oper(np.var),
        'standard deviation': oper(np.std),
        'max': oper(np.max),
        'min': oper(np.min),
        'sum': oper(np.sum)
    }