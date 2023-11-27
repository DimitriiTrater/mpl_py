
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


def lf(a, b):
    delta = np.pi/2
    t = np.arange(0, 4 * np.pi / 2, 0.001)
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


matplotlib.use("Qt5Agg")
plt.subplot(2, 2, 1)
plt.plot(*lf(3, 2))
plt.subplot(2, 2, 2)
plt.plot(*lf(3, 4))
plt.subplot(2, 2, 3)
plt.plot(*lf(5, 4))
plt.subplot(2, 2, 4)
plt.plot(*lf(5, 6))
plt.show()
