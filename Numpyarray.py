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
a = random.normalvariate(0, 1)
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

# numpy.linspace等差数组 np.linspace(start, stop, num=50, endpoint=True 是否包含终值, retstep=False True显示间距, dtype=None)
a = np.linspace(10, 20, 10)
print(a)

# numpy.logspace等比数组 np.logspace(start, stop, num=50, endpoint=True, base=10.0 对数的底, dtype=None)
a = np.logspace(1.0, 2.0, 10)  # start 和 stop 也都以base为底
print(a)

# 切片和索引
# slice生成切片数组 再对ndarray切片
a = np.arange(1, 10)
print(a)
s = slice(2, 7, 2)
print(a[s])
print(type(a))
# 一维数组索引
a = np.arange(1, 10, 1)
print(a)
print(a[2])
print(a[2:])
print(a[2:5])
# 多维数组索引
a = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
print(a)
print(a[1])
print(a[1:])
print(a[..., 1])
print(a[1, ...])
print(a[..., 1:])
# 整数数组切片
a = np.array([[1, 2], [3, 4], [5, 6]])
b = a[[0, 1, 2], [0, 1, 0]]
print(b)

print('\n')
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print ('我们的数组是：' )
print (x)
print ('\n')

rows = np.array([[0,0],[3,3]]) 
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols]  
print  ('这个数组的四个角元素是：')
print (y)

a = np.arange(6).reshape(2,3)
print(a.T)
for x in np.nditer(a.T):
    print (x, end=", " )
print ('\n')
 
for x in np.nditer(a.T.copy(order='C')):
    print (x, end=", " )
print ('\n')