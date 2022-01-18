import numpy as np

a = np.array([1,2,3])
print(a[1])
print(a.ndim)
a = np.array([[1,2],[3,4],[5,6]])
print(a.ndim)

print("----------------------------")

print("Size of each element is: ",a.itemsize," bytes")
print(a.dtype)

print("----------------------------")

a = np.array([[1,2],[3,4],[5,6]], dtype=float)
print("Size of each element is: ",a.itemsize," bytes")
print(a.size)
print(a.shape)

print("----------------------------")

a = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(a)

print("----------------------------")

print(np.zeros((3,4)))
print(np.ones((3,4)))

print("----------------------------")

print(np.arange(1,5))
print(np.arange(1,5,2))

print("----------------------------")

print(np.linspace(1,5,10))
print(np.linspace(1,5,5))

print("----------------------------")

print(a.reshape(2,3))
print(a.ravel())

print("----------------------------")

print(a.min())
print(a.max())
print(a.sum())

print("----------------------------")

print(a.sum(axis=0))
print(a.sum(axis=1))

print("----------------------------")

print(np.sqrt(a))
print(np.std(a))

print("----------------------------")

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("----------------------------")

print(a.dot(b))     # Matrix Product