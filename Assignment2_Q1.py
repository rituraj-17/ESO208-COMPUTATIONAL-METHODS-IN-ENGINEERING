import math

def oxygen_equation(T):
    # Absolute temperature conversion
    Ta = T + 273.15
    
    #terms of the equation
    term1 = -139.34411
    term2 = (1.575701e5) / Ta
    term3 = (6.642308e7) / (Ta**2)
    term4 = (1.243800e10) / (Ta**3)
    term5 = (8.621949e11) / (Ta**4)
    
    # ln(Osf)
    ln_Osf = term1 + term2 - term3 + term4 - term5
    
    # We want to find T where Osf = 10 mg/L. 
    # The root occurs when ln_Osf - ln(10) = 0
    return ln_Osf - math.log(10)

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    Finds the root of a function using the Bisection Method.
    """
    if func(a) * func(b) >= 0:
        raise ValueError("Root is not bracketed by the interval [a, b].")
    
    for _ in range(max_iter):
        c = (a + b) / 2.0
        
        # Checking if we have reached the desired tolerance
        if abs(func(c)) < tol or (b - a) / 2.0 < tol:
            return c
        
        # Narrowing the interval here
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
            
    return c

# Executing bisection method in the valid range 0 <= T <= 40
try:
    temperature = bisection_method(oxygen_equation, 0, 40)
    print(f"Q1: The freshwater temperature for Osf = 10 mg/L is approx {temperature:.4f} °C")
except ValueError as e:
    print(e)