import numpy as np
import matplotlib 

a = [3, 2, 1, 2, 3, 4, 5, 1, 2, 4, 5, 1, 2, 3, 2, 1]
b = a[:]
a = list(set(a))
print(a)
a = np.unique(a)
print(a, type(a))

print(np.bincount(b))


a = np.array([1.0, 0, -2, 1])
p = np.poly1d(a)
print(a)
print('--------------------------')

a1 = p.deriv()
print(a1)
print(a1.c)     #系数
print(a1.order) #最高项次方数
print(a1.coef)  #拿系数
print('--------------------------')
a2 = p.integ()
print(a2)
