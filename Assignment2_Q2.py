import math
def flow_equation(y):
    Q = 5.0
    B = 20.0
    S = 0.0002
    n = 0.03    
    numerator = math.sqrt(S) * (B * y)**(5/3)
    denominator = n * (B + 2 * y)**(2/3)
    Q_calc = numerator / denominator
    return Q_calc - Q
def flow_derivative(y):
    B = 20.0
    S = 0.0002
    n = 0.03
    constant = math.sqrt(S) / n
    u = (B * y)**(5/3)
    du_dy = (5/3) * (B * y)**(2/3) * B
    v = (B + 2 * y)**(2/3)
    dv_dy = (2/3) * (B + 2 * y)**(-1/3) * 2
    derivative = constant * ((du_dy * v - u * dv_dy) / (v**2))
    return derivative
def newton_raphson_method(func, dfunc, x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        fx = func(x) 
        if abs(fx) < tol:
            return x
        dfx = dfunc(x)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero. Method fails.")
        x = x - (fx / dfx)
    return x
try:
    initial_guess = 1.0
    flow_depth = newton_raphson_method(flow_equation, flow_derivative, initial_guess)
    print(f"Q2: The flow depth for Q = 5 m^3/s is approx {flow_depth:.4f} m")
except ZeroDivisionError as e:
    print(e)