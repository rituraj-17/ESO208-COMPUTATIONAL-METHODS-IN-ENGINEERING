import numpy as np
import matplotlib.pyplot as plt
import os

output_folder = os.path.dirname(os.path.abspath(__file__))

def f(x):
    return np.exp((x - 1)**2) - 1

def fp(x):
    return 2 * (x - 1) * np.exp((x - 1)**2)

def fpp(x):
    return (2 + 4 * (x - 1)**2) * np.exp((x - 1)**2)

x = np.linspace(-1, 3, 1000)

plt.figure(figsize=(8, 5))
plt.plot(x, f(x), label='f(x)')
plt.axhline(0, linewidth=0.8)
plt.axvline(1, linewidth=0.8)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x)')
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(output_folder, 'f_plot.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(x, fp(x), label="f'(x)")
plt.axhline(0, linewidth=0.8)
plt.axvline(1, linewidth=0.8)
plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title("f'(x)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(output_folder, 'fp_plot.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()

plt.figure(figsize=(8, 5))
plt.plot(x, fpp(x), label="f''(x)")
plt.axhline(0, linewidth=0.8)
plt.axvline(1, linewidth=0.8)
plt.xlabel('x')
plt.ylabel("f''(x)")
plt.title("f''(x)")
plt.grid(True)
plt.legend()
plt.savefig(os.path.join(output_folder, 'fpp_plot.png'), dpi=300, bbox_inches='tight')
plt.show()
plt.close()

print("Plots saved in:", output_folder)