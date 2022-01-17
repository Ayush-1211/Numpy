import numpy as np
import time

SIZE = 10000000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

# Python list
start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]
print("Python list took: ", (time.time()-start)*1000, "ms")

# Numpy array
start = time.time()
result = a1 + a2
print("Numpy array took: ", (time.time()-start)*1000, "ms")