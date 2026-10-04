import numpy as np
y = np.array([0, 2, 4, 6, 8, 10, 12, 14], dtype=float)
H = np.array([0, 1, 1.5, 3, 3.5, 3.2, 2, 0], dtype=float)
U = np.array([0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0], dtype=float)

HU = H * U
h = y[1] - y[0]

def trapezoidal(f, h):
    n = len(f)
    result = f[0] + f[n-1]

    for i in range(1, n-1):
        result += 2 * f[i]

    return (h / 2) * result

A = trapezoidal(H, h)
Q = trapezoidal(HU, h)
U_bar = Q / A

print("Area =", A, "m^2")
print("Discharge =", Q, "m^3/s")
print("Average velocity =", U_bar, "m/s")