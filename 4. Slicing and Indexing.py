import numpy as np

a = np.array([3,4,5])
print(a[0:2])
print(a[-1])

print("----------------------------")

a = np.array([[6,7,8],[1,2,3],[9,3,2]])
print(a[-1])
print(a[1,2])   # 1st row , 2nd column
print(a[0:2,2])     # row=0,1 | colunm=2
print(a[-1,0:2])

print("----------------------------")

print(a[:,1:3])

print("----------------------------")

for row in a:
    print(row)
for cell in a.flat:
    print(cell)

print("----------------------------")

b = np.arange(30).reshape(2,15)
print(b)
result = np.hsplit(b,3)
print(result[0])
print(result[1])
print(result[2])

print("----------------------------")

result = np.vsplit(b,2)
print(result[0])
print(result[1])

print("----------------------------")

c = np.arange(12).reshape(3,4)
d = c > 4
print(d)
print(c[d])
c[d]=-1
print(c)