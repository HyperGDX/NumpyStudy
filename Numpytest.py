from random import randint
import numpy as np
import math
import random

# arrange创建数组
a1 = np.arange(20)
a2 = np.arange(10, 20)
a3 = np.arange(10, 20, 2)
a4 = np.arange(10, 20, 2, dtype=np.float)
print(a1, a2, a3, a4)

# 创建正太数组？？
a = random.normalvariate(0,1)
print(a)

# 创建随机分布数组？？
a = random.randint(2, 3)
print(a)

# shape,reshape
a = np.arange(24)
a = a.reshape(3, 8)
print(a)
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
print(b.shape)


# empty创建空数组
a = np.empty(10, dtype=np.int)
print(a)

# zeros创建全0数组
a = np.zeros(5)
print(a)
a = np.zeros(5, dtype=np.int)
print(a)
a = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(a)

# ones创建全1数组
a = np.ones((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(a)

