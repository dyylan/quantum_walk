import numpy as np


def inverse_power_fit(x, a, b, c):
    return (a / np.power(x, b)) + c


def power_fit(x, a, b, c):
    return a * np.power(x, b) + c


# def power_fit_over_log(x, a, c):
#     return a * np.power(x, 0.75) / np.power(np.log(x), 0.25) + c

def power_fit_over_log(x, a, b, c):
    return a * np.power(x, b) / np.power(np.log(x), 0.25) + c