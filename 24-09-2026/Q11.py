import numpy as np

# Define matrix P
P = np.array([
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
], dtype=float)

# Option (A): Trace(P) == sum of eigenvalues
trace_P = np.trace(P)
eigenvalues = np.linalg.eigvals(P)
sum_eig = np.sum(eigenvalues)
is_a_true = np.isclose(trace_P, sum_eig)

# Option (B): P^T P is an identity matrix
I = np.eye(3)
PtP = P.T @ P
is_b_true = np.allclose(PtP, I)

# Option (C): P is skew-symmetric (P^T == -P)
is_c_true = np.allclose(P.T, -P)

# Option (D): Absolute magnitude of each eigenvalue is 1
eig_mags = np.abs(eigenvalues)
is_d_true = np.allclose(eig_mags, 1.0)

print(f"(A) Trace == Sum of Eigenvalues: {is_a_true}  (Trace: {trace_P}, Sum: {sum_eig})")
print(f"(B) P.T @ P == I:                {is_b_true}")
print(f"(C) P.T == -P:                   {is_c_true}")
print(f"(D) All |Eigenvalue| == 1:       {is_d_true}  (Magnitudes: {eig_mags})")

