from matplotlib.pyplot import polar, xticks
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10, 0.1)
y = x**2
plt.xlim(-10, 10)
plt.ylim(0, 100)
#plt.plot(x, y)
# plt.show()

x = np.linspace(-np.pi, np.pi)
y1 = np.cos(x)
xticks(np.linspace(-np.pi, np.pi, 5))
#plt.plot(x, y1)
# plt.show()

alpha=1
theta=np.linspace(0,2*np.pi, 500)
r=np.sqrt(2*(alpha**2)*np.cos(2*theta))
plt.axes(polar=True)
plt.plot(theta,r)
plt.show()

