import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as anim

FRAMES = 100

matplotlib.use("Qt5Agg")


def lf(a, b, t):
    delta = 0
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    return x, y


def update(frame):
    plt.clf()
    ax = plt.gca()

    ratio = frame / FRAMES
    a = 1
    b = ratio

    t = np.linspace(0, 2 * np.pi, 1000)
    x, y = lf(a, b, t)

    ax.grid()
    ax.plot(x, y)


ani = anim.FuncAnimation(plt.gcf(), update, frames=FRAMES,
                         interval=100, repeat=True)

plt.show()
