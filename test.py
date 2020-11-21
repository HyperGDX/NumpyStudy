import random

# 生成呈正态分布的随机数
# print("normalvariate: ", random.normalvariate(0, 1))

# 产生一组满足正太分布的随机数
walk = []
for _ in range(1000):
    walk.append(random.normalvariate(0, 1))

# 画成直方图
import matplotlib.pyplot as plt  # 导入模块

plt.hist(walk, bins=30)  # bins直方图的柱数
plt.show()
print(walk)