import numpy as np
import matplotlib.pyplot as plt

# Parameters
T = 10.0 
t = np.linspace(0.001 * T, 0.999 * T, 1000)

# Condition number
theta = (2 * np.pi / T) * t
condition_number = np.abs(theta * (1.0 / np.tan(theta)))

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(
    t, condition_number, label=r"Condition Number $C(t)$", color="b", linewidth=2
)
plt.title(
    r"Condition Number of $y(t) = \sin\left(\frac{2\pi}{T}t\right)$", fontsize=12
)
plt.xlabel("Time ($t$)", fontsize=11)
plt.ylabel("Condition Number $C(t)$", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xlim(0, T)
plt.ylim(0, max(condition_number[~np.isinf(condition_number)]) * 1.1)
plt.legend()
plt.savefig("condition_number_plot.png", dpi=300, bbox_inches="tight")
plt.show()