import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
phases = [1/4, 1/3, 1/2]

plt.figure(figsize=(10, 6))
for i, phi in enumerate(phases):
    plt.plot(x, np.sin(x + phi), label=f'sin(x + {phi})', color=plt.cm.tab10(i))

plt.plot(x, np.cos(x), '--', label='cos(x)')
plt.plot(x, np.cos(x + phases[0]), '--', label=f'cos(x + {phases[0]})')
plt.legend()
plt.grid()
plt.show()