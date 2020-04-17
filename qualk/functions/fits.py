import numpy as np


def inverse_power_fit(x, a, b, c):
    return (a / np.power(x, b)) + c


def power_fit(x, a, b, c):
    return a * np.power(x, b) + c