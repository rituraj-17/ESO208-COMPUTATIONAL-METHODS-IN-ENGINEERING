import numpy as np

y = np.array([0, 2, 4, 6, 8, 10, 12, 14], dtype=float)
H = np.array([0, 1, 1.5, 3, 3.5, 3.2, 2, 0], dtype=float)
U = np.array([0, 0.1, 0.12, 0.2, 0.25, 0.3, 0.15, 0], dtype=float)

HU = H * U
h = y[1] - y[0]

def simpson_38(f0, f1, f2, f3, h):
    return (3 * h / 8) * (f0 + 3*f1 + 3*f2 + f3)

def simpson_13(f0, f1, f2, f3, f4, h):
    return (h / 3) * (f0 + 4*f1 + 2*f2 + 4*f3 + f4)

A_38 = simpson_38(H[0], H[1], H[2], H[3], h)
A_13 = simpson_13(H[3], H[4], H[5], H[6], H[7], h)
A = A_38 + A_13

Q_38 = simpson_38(HU[0], HU[1], HU[2], HU[3], h)
Q_13 = simpson_13(HU[3], HU[4], HU[5], HU[6], HU[7], h)
Q = Q_38 + Q_13

U_bar = Q / A

print("Simpson's Rule")
print("Area =", A, "m^2")
print("Discharge =", Q, "m^3/s")
print("Average velocity =", U_bar, "m/s")