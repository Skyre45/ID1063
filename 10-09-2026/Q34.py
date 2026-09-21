import matplotlib.pyplot as plt
import numpy as np

# System: 2x + 3y = 6
#         4x + 6y = 3k
# Find k for which the system has at least one solution (consistent).

A = np.array([[2, 3],
              [4, 6]])

# Check both k = 4 and k = 6 for comparison
for k in [4, 6]:
    b = np.array([[6],
                   [3 * k]])

    Ab = np.hstack((A, b))   # augmented matrix [A|b]

    rank_A = np.linalg.matrix_rank(A)
    rank_Ab = np.linalg.matrix_rank(Ab)

    print(f"k = {k}")
    print("A =\n", A)
    print("A|b =\n", Ab)
    print("rank(A)  =", rank_A)
    print("rank(A|b)=", rank_Ab)

    if rank_A == rank_Ab:
        print("=> Consistent: at least one solution exists")
    else:
        print("=> Inconsistent: no solution")
    print("-" * 40)


x = np.linspace(-5, 10, 400)

y1 = (6-2*x)/3

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

for ax, k in zip(axes, [4, 6]):
    # Equation 2: 4x + 6y = 3k  ->  y = (3k - 4x) / 6
    y2 = (3 * k - 4 * x) / 6

    ax.plot(x, y1, label='2x + 3y = 6', color='tab:blue', linewidth=2)
    ax.plot(x, y2, label=f'4x + 6y = {3*k} (k={k})', color='tab:red',
             linewidth=2, linestyle='--')

    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.set_xlim(-5, 10)
    ax.set_ylim(-5, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True, alpha=0.3)

    if k == 4:
        ax.set_title('k = 4: Lines coincide\n(Infinitely many solutions)')
    else:
        ax.set_title('k = 6: Lines are parallel\n(No solution)')

plt.tight_layout()
plt.savefig("Plot.png")


