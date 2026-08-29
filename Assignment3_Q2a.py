import numpy as np
def gauss(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    aug = np.column_stack((A, b))
    for k in range(n - 1):
        p = k + np.argmax(abs(aug[k:, k]))
        aug[[k, p]] = aug[[p, k]]
        for i in range(k + 1, n):
            factor = aug[i, k] / aug[k, k]
            aug[i] = aug[i] - factor * aug[k]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (aug[i, -1] - np.sum(aug[i, i + 1:n] * x[i + 1:n])) / aug[i, i]
    return x
A = [[2, -6, -1],
     [-3, -1, 7],
     [-8, 1, -2]]
b = [-38, -34, -20]
x = gauss(A, b)
print("Solution:")
for i in range(len(x)):
    print(f"x{i + 1} =", x[i])