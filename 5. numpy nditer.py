import numpy as np

a = np.arange(12).reshape(3,4)
print(a)

print("----------------------------")

for x in np.nditer(a, order='C'):   # C order
    print(x)

print("----------------------------")

for x in np.nditer(a, order='F'):   # Fortran order
    print(x)

print("----------------------------")

for x in np.nditer(a, order='F', flags=['external_loop']):
    print(x)

print("----------------------------")

for x in np.nditer(a,op_flags=['readwrite']):
    x[...] = x*x
print(a)

print("----------------------------")

b = np.arange(3,15,4).reshape(3,1)
print(b)
for x,y in np.nditer([a,b]):
    print(x,y)