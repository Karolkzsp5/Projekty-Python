import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

x_data = np.array([...])
y_data = np.array([...])

def model(x, a, b, c):
    return a * np.log(x + b) + c

params, _ = curve_fit(model, x_data, y_data)
a, b, c = params

plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label='Dane')
plt.plot(x_data, model(x_data, a, b, c), 'r-', label='Model')
plt.legend()
plt.grid()
plt.show()