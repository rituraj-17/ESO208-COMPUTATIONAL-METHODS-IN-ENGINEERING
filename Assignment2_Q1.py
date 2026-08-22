import math
def oxygen_equation(T):
    Ta = T + 273.15 
    #terms of the equation
    term1 = -139.34411
    term2 = (1.575701e5) / Ta
    term3 = (6.642308e7) / (Ta**2)
    term4 = (1.243800e10) / (Ta**3)
    term5 = (8.621949e11) / (Ta**4)
    ln_Osf = term1 + term2 - term3 + term4 - term5 
    return ln_Osf - math.log(10)
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        raise ValueError("Root is not bracketed by the interval [a, b].")
    for _ in range(max_iter):
        c = (a + b) / 2.0
        if abs(func(c)) < tol or (b - a) / 2.0 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return c
try:
    temperature = bisection_method(oxygen_equation, 0, 40)
    print(f"Q1: The freshwater temperature for Osf = 10 mg/L is approx {temperature:.4f} °C")
except ValueError as e:
    print(e)