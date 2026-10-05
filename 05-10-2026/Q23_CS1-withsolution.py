import numpy as np
import matplotlib.pyplot as plt

k = float(input("Enter k: "))

# Rank test: x + ky = 1, kx + y = -1
A = np.array([[1, k], [k, 1]])
b = np.array([[1], [-1]])
Ab = np.hstack([A, b])
n = 2

rA = np.linalg.matrix_rank(A)
rAb = np.linalg.matrix_rank(Ab)

if rA < rAb:
    result = "No solution"
elif rA == n:
    sol = np.linalg.solve(A, b).ravel()
    result = f"Unique solution ({sol[0]:.2f}, {sol[1]:.2f})"
else:
    result = "Infinitely many solutions"

print(f"rank A = {rA}, rank [A|b] = {rAb} -> {result}")

# Plot
x = np.linspace(-20, 20, 400)

if k != 0:
    plt.plot(x, (1 - x)/k, label='x+ky=1', color='red')
else:
    plt.axvline(1, label='x+ky=1', color='red')  # k=0 gives x = 1 (vertical line)

plt.plot(x, -1 - k*x, label='kx+y=-1', color='blue', linestyle='--')

if rA == rAb == n:
    plt.plot(sol[0], sol[1], 'ko', label='solution')

plt.title(f'k = {k:g}: {result}')
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.grid(True)
plt.legend()
plt.savefig('fig.png')

