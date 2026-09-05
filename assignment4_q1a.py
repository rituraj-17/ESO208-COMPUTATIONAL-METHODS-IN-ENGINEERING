import numpy as np
A = np.array([
    [7,  2, -3],
    [2,  5, -3],
    [1, -1, -6]
], dtype=float)
n = len(A)
L = np.eye(n)
U = np.zeros((n, n))
for i in range(n):
    for j in range(i, n):
        U[i, j] = A[i, j]
        for k in range(i):
            U[i, j] -= L[i, k] * U[k, j]
    for j in range(i + 1, n):
        L[j, i] = A[j, i]

        for k in range(i):
            L[j, i] -= L[j, k] * U[k, i]

        L[j, i] /= U[i, i]
print("L =")
print(L)
print("\nU =")
print(U)
print("\nVerification L @ U =")
print(L @ U)