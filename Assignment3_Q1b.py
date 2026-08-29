import numpy as np
import matplotlib.pyplot as plt
import os

output_folder = os.path.dirname(os.path.abspath(__file__))

def u(x):
    t = x - 1
    result = (1 - np.exp(-t**2)) / (2 * t)
    result = np.where(np.abs(t) < 1e-10, 0.0, result)
    return result

def up(x):
    t = x - 1
    result = ((2 * t**2 + 1) * np.exp(-t**2) - 1) / (2 * t**2)
    result = np.where(np.abs(t) < 1e-5, 0.5, result)
    return result

x = np.linspace(-1, 3, 1000)

plt.figure(figsize=(8, 5))
plt.plot(x, u(x), label='u(x)')
plt.axhline(0, linewidth=0.8)
plt.axvline(1, linewidth=0.8)
plt.xlabel('x')
plt.ylabel('u(x)')
plt.title("u(x) = f(x) / f'(x)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(output_folder, 'u_plot.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(x, up(x), label="u'(x)")
plt.axhline(0, linewidth=0.8)
plt.axvline(1, linewidth=0.8)
plt.xlabel('x')
plt.ylabel("u'(x)")
plt.title("u'(x)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(output_folder, 'up_plot.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()

print("Plots saved in:", output_folder)