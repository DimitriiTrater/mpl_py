import numpy as np
from scipy.special import legendre
import matplotlib
import matplotlib.pyplot as plt


def P(leg, chi):
    polynom = legendre(leg)
    return polynom(chi)


CHI = np.arange(-1, 1, 0.01)

matplotlib.use("Qt5Agg")
for order in range(7):
    plt.plot(CHI, P(order, CHI), label=f"n={order}")

fig = plt.gcf()
fig.canvas.manager.set_window_title("Полиномы Лежандра")
fig.legend()
plt.show()
