import numpy as np
import matplotlib.pyplot as plt
T = np.array([0, 8, 16, 24, 32, 40], dtype=float)
O = np.array([14.621, 11.843, 9.870, 8.418, 7.305, 6.413])
n = len(T)

#Q1 a
def newton_coeffs(x, y):
    m = len(x)
    F = np.zeros((m, m))
    F[:, 0] = y
    for j in range(1, m):
        for i in range(m - j):
            F[i, j] = (F[i + 1, j - 1] - F[i, j - 1]) / (x[i + j] - x[i])
    return F[0, :], F          # b0..b5 are the top row

def newton_eval(b, x, xq):
    p = b[-1] * np.ones_like(xq)
    for k in range(len(b) - 2, -1, -1): 
        p = b[k] + (xq - x[k]) * p
    return p
b, F = newton_coeffs(T, O)
print("Q1(a) Divided-difference table:")
for i in range(n):
    print("  ", "  ".join(f"{F[i, j]: .6e}" for j in range(n - i)))
print("\nNewton coefficients:")
for k, bk in enumerate(b):
    print(f"  b{k} = {bk: .6e}")
# Q1 b + c
m = n - 1                 
N = 3 * m
A = np.zeros((N, N))
r = np.zeros(N)
row = 0

for i in range(m):
    for x, y in ((T[i], O[i]), (T[i + 1], O[i + 1])):
        A[row, 3*i:3*i+3] = [x**2, x, 1.0]
        r[row] = y
        row += 1

for i in range(m - 1):
    x = T[i + 1]
    A[row, 3*i:3*i+2] = [2*x, 1.0]
    A[row, 3*(i+1):3*(i+1)+2] = [-2*x, -1.0]
    row += 1

A[row, 0] = 1.0
row += 1
def gauss_elim(A, b):
    """Naive Gauss elimination with partial pivoting + back substitution."""
    A = A.astype(float).copy(); b = b.astype(float).copy()
    N = len(b)
    for k in range(N - 1):
        p = k + np.argmax(np.abs(A[k:, k]))     # partial pivoting
        if p != k:
            A[[k, p]] = A[[p, k]]; b[[k, p]] = b[[p, k]]
        for i in range(k + 1, N):
            f = A[i, k] / A[k, k]
            A[i, k:] -= f * A[k, k:]
            b[i] -= f * b[k]
    x = np.zeros(N)
    for i in range(N - 1, -1, -1):
        x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
    return x

coef = gauss_elim(A, r)
print("\nQ1(c) Quadratic spline coefficients:")
for i in range(m):
    a_, b_, c_ = coef[3*i:3*i+3]
    print(f"  Interval {i+1} [{T[i]:.0f},{T[i+1]:.0f}]:  a = {a_: .6e},  b = {b_: .6e},  c = {c_: .6f}")

def spline_eval(xq):
    out = np.zeros_like(xq)
    for j, x in enumerate(xq):
        i = min(np.searchsorted(T, x, side='right') - 1, m - 1)
        i = max(i, 0)
        a_, b_, c_ = coef[3*i:3*i+3]
        out[j] = a_*x**2 + b_*x + c_
    return out

# Q1 d
Tq = np.linspace(0, 40, 401)
plt.figure(figsize=(8, 5))
plt.plot(Tq, newton_eval(b, T, Tq), 'b-', label="Newton's 5th-order polynomial")
plt.plot(Tq, spline_eval(Tq), 'r--', label='Quadratic spline')
plt.plot(T, O, 'ko', ms=7, label='Data points')
plt.xlabel('Temperature T (°C)'); plt.ylabel('Dissolved oxygen O (mg/L)')
plt.title('Dissolved oxygen vs temperature')
plt.grid(alpha=0.3); plt.legend()
plt.tight_layout(); plt.savefig('q1_plot.png', dpi=200)
print("\nPlot saved: q1_plot.png")