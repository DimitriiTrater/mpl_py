import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

matplotlib.use("Qt5Agg")


def calculate_wave(frequency, amplitude, t):
    return amplitude * np.sin(2 * np.pi * frequency * t)


def sum_of_waves(frequency1, amplitude1, frequency2, amplitude2, t):
    wave1 = calculate_wave(frequency1, amplitude1, t)
    wave2 = calculate_wave(frequency2, amplitude2, t)
    return wave1 + wave2


def update(var):

    freq1 = freq_slider1.val
    amp1 = amp_slider1.val
    freq2 = freq_slider2.val
    amp2 = amp_slider2.val

    t = np.linspace(0, 1, 1000)
    sum_wave = sum_of_waves(freq1, amp1, freq2, amp2, t)

    ax_sum_wave.clear()
    ax_sum_wave.plot(t, sum_wave, label='Сумма волн')
    ax_sum_wave.set_title('Сложение двух волн')
    ax_sum_wave.set_xlabel('Время')
    ax_sum_wave.set_ylabel('Амплитуда')

    plt.draw()


fig, (ax_freq1, ax_amp1, ax_freq2, ax_amp2, ax_sum_wave) =\
    plt.subplots(5, 1, figsize=(8, 14))


freq_slider1 = Slider(ax_freq1, 'Частота 1', 1, 10, valinit=1)
amp_slider1 = Slider(ax_amp1, 'Амплитуда 1', 0, 1, valinit=0)
freq_slider2 = Slider(ax_freq2, 'Частота 2', 1, 10, valinit=1)
amp_slider2 = Slider(ax_amp2, 'Амплитуда 2', 0, 1, valinit=0)


freq_slider1.on_changed(update)
amp_slider1.on_changed(update)
freq_slider2.on_changed(update)
amp_slider2.on_changed(update)


update(None)

plt.tight_layout()
plt.show()
