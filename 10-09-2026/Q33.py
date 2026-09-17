import matplotlib.pyplot as plt
import numpy as np

def f(x):
    y = np.exp(x)-2
    return y

x_vals = np.linspace(-2,2,500)
y_vals=f(x_vals)

plt.plot(x_vals, y_vals)
plt.grid(True)

xV=[np.log(2)]
yV=[0]

plt.plot(xV, yV, 'ro')
plt.text(np.log(2), 0, "(ln(2),0)")

plt.savefig('figure33.png')


