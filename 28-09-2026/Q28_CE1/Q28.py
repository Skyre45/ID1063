import numpy as np

# Each line a*x + b*y + c = 0 as a vector (a, b, c)
l1 = np.array([1, 1, -7], dtype=float)     # x + y - 7
l2 = np.array([3, 1, -13], dtype=float)    # 3x + y - 13

# (l1.X)^2 + (l2.X)^2 with X = (x, y, 1)  ->  X^T M X, M = l1 l1^T + l2 l2^T
M = np.outer(l1, l1) + np.outer(l2, l2)
V, u, f = M[:2, :2], M[:2, 2], M[2, 2]

print("V =\n", V)
print("u =", u, "  f =", f)
print("M =\n", M)

# Singularity test
print("\ndet(M)  =", round(np.linalg.det(M), 10))
print("rank(M) =", np.linalg.matrix_rank(M))
print("det(V)  =", round(np.linalg.det(V), 10))
print("eigenvalues of V:", np.linalg.eigvalsh(V))

# Center: V c = -u
c = np.linalg.solve(V, -u)
print("\nCenter:", c)
X = np.append(c, 1)
print("X^T M X at center:", round(X @ M @ X, 10))

# Complex lines: l1 + i*l2 and l1 - i*l2
print("\nLine 1 coefficients (a, b, c):", l1 + 1j*l2)
print("Line 2 coefficients (a, b, c):", l1 - 1j*l2)

# Why V must be symmetric
M_bad = M.copy()
M_bad[0, 1], M_bad[1, 0] = 8, 0
print("\ndet(M) with non-symmetric V:", round(np.linalg.det(M_bad), 6), "(wrongly nonzero)")

