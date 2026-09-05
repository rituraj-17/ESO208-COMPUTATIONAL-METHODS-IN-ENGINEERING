import numpy as np

A = np.array([
    [7, 2, -3],
    [2, 5, -3],
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

A_inv = np.zeros((n, n))

for col in range(n):
    B = np.zeros(n)
    B[col] = 1

    Y = np.zeros(n)

    for i in range(n):
        Y[i] = B[i]
        for j in range(i):
            Y[i] -= L[i, j] * Y[j]
        Y[i] /= L[i, i]

    X = np.zeros(n)

    for i in range(n - 1, -1, -1):
        X[i] = Y[i]
        for j in range(i + 1, n):
            X[i] -= U[i, j] * X[j]
        X[i] /= U[i, i]

    A_inv[:, col] = X

print("A inverse =")
print(A_inv)