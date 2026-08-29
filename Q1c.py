import numpy as np
def f(x):
    return np.exp((x - 1)**2) - 1
def secant(x1, x2):
    tol = 1e-6
    for i in range(100):
        x3 = x2 - f(x2) * (x2 - x1) / (f(x2) - f(x1))
        print(f"Iteration {i + 1}: x = {x3:.10f}")
        if abs(x3 - x2) < tol:
            return x3, i + 1
        x1 = x2
        x2 = x3
    return x2, 100
def modified_secant(x):
    delta = 0.001
    tol = 1e-6
    for i in range(100):
        x_new = x - (delta * f(x)) / (f(x + delta) - f(x))
        print(f"Iteration {i + 1}: x = {x_new:.10f}")
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return x, 100
root1, iterations1 = secant(-0.5, 0)
print("\nSecant Method")
print("Root =", root1)
print("Number of iterations =", iterations1)
root2, iterations2 = modified_secant(0)
print("\nModified Secant Method")
print("Root =", root2)
print("Number of iterations =", iterations2)