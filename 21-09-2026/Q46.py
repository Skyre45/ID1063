import matplotlib.pyplot as plt
import numpy as np

x1=np.linspace(-10,0,500)
x2=np.linspace(0,10,500)
y2=np.sin(2*x2)
y1=2*x1

plt.ylim(-5, 5)


plt.plot(x1, y1)
plt.plot(x2, y2)
plt.grid(True)
plt.legend
plt.savefig('Q46.png')

