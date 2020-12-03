import numpy as np
import math

a1 = np.ndarray([1, 2, 3])
#a2 = np.ndarray([1, 2, 3], [4, 5, 6])
a3 = np.ndarray([])

d1 = np.dtype([('name', 'S20'), ('age', 'i1'), ('mark', 'f4')])
t1 = np.array([('abc', 18, 80)], dtype=d1)
print(t1)

#reshape与原array公用一个内存,非拷贝副本
a = np.arange(24)
print(a)
a = a.reshape(4, 6)
print(a)
a = a.reshape(3, 2, 4)
print(a)
print(a.shape)



