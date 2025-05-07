import numpy as np
import matplotlib.pyplot as plt
from scipy.differentiate import derivative

def tangent_line(f, x0, x):
    deriv = derivative(f, x0, dx=1e-6)
    return f(x0) + deriv * (x - x0)

x = np.linspace(-3, 2, 100)
y = x**2
points = [-2, 0, 1]

plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x²')

for p in points:
    tan = tangent_line(lambda x: x**2, p, x)
    plt.plot(x, tan, '--', label=f'Styczna w x={p}')

plt.title('Funkcja kwadratowa i jej styczne')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()