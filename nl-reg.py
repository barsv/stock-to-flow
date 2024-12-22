import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Данные
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 8, 21, 56, 148])

# Модель
def model(x, a, b):
    return a * np.exp(b * x)

# Подбор параметров
params, _ = curve_fit(model, x, y)

# Предсказание
a, b = params
y_pred = model(x, a, b)

# График
plt.scatter(x, y, label='Данные')
plt.plot(x, y_pred, label=f'Модель: y = {a:.2f} * exp({b:.2f} * x)')
plt.legend()
plt.show()
