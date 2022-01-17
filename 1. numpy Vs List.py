import numpy as np
import sys

l = range(1000)     # 1000 elements
print(sys.getsizeof(5)*len(l))

array = np.arange(1000)         # arange is similar to range
# array.size = 1000
# array.itemsize = size of 1 element
print(array.size*array.itemsize)
