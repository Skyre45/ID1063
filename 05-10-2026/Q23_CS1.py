import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-20, 20, 400)

for i, k in enumerate([1, -1, 2], start=1):
    plt.subplot(2, 2, i)
    plt.title(f'When k = {k}')
    plt.plot(x, (1 - x)/k, label='x+ky=1', color='red')
    plt.plot(x, -1 - k*x, label='kx+y=-1', color='blue')
    plt.legend()

plt.tight_layout()
plt.savefig('fig.png')
