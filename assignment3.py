import numpy as np

def f(x, y):
    return x**2 + y**2

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
dx = x[1] - x[0]
dy = y[1] - y[0]
X, Y = np.meshgrid(x, y)
Z = f(X, Y)
volume = np.sum(Z) * dx * dy
print("Estimated Volume under Surface:", volume)
