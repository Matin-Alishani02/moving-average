import numpy as np

def moving_average(data_list, window_size):
    x = np.cumsum(data_list, dtype=float)
    x[window_size:] = x[window_size:] - x[:-window_size]
    return x[window_size - 1:] / window_size
    
data_list = np.array([1,5,3,4,4])
window_size = 3
result = moving_average(data_list , window_size)
print (result)