import math
def Q(t):

    return 8 + 5 * (math.cos(0.4 * t))**2
def c(t):
    return 5 * math.exp(-0.5 * t) + 3 * math.exp(0.15 * t)
def f(t):
    return Q(t) * c(t)
def romberg(a, b, tolerance=0.1, max_level=10):
    R = []
    R.append([
        (b - a) * (f(a) + f(b)) / 2
    ])
    for i in range(1, max_level + 1):
        h = (b - a) / (2**i)
        summation = 0
        for j in range(1, 2**(i - 1) + 1):
            x = a + (2*j - 1) * h
            summation += f(x)
        R_i0 = (
            0.5 * R[i-1][0]
            + h * summation
        )
        row = [R_i0]
        for j in range(1, i + 1):
            value = (
                row[j-1]
                + (
                    row[j-1] - R[i-1][j-1]
                ) / (4**j - 1)
            )
            row.append(value)
        R.append(row)
        error = abs(
            (row[i] - R[i-1][i-1])
            / row[i]
        ) * 100
        print(
            "Level =", i,
            "Romberg value =", row[i],
            "Error (%) =", error
        )
        if error < tolerance:
            return row[i], R, error
    return R[-1][-1], R, error
M, R, error = romberg(
    2,
    8,
    tolerance=0.1
)
print("\nFinal Result")
print("Mass transported =", M, "mg")
print("Estimated error =", error, "%")