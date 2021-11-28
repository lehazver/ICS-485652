from numpy import *
import matplotlib.pyplot as plt
x = linspace(0,5,500)
y = x**(1/2)*sin(10*x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('2D Графік Функції')

plt.show()