import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(21)

T = [0] * 21
T[0] = 1

for i in range(20):
    T[i+1] = 2*T[i] + (i+1) * 2**(i+1)

Z = np.power(2.0, x) + x*(x+1)*np.power(2.0, x-1)

plt.plot(x, T, color="red", label="recurrence")
plt.plot(x, Z, "--", color="green", label="closed form")
plt.legend()
plt.savefig("fig.png")

print(np.allclose(T, Z))
