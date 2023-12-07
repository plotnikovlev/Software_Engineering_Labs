import numpy as np


def f(x, y):
    return x + y


def x(z):
    return pow(np.cos(5), 2)


def y(z):
    return pow(z, 3) - 1


print(f(x(2), y(3)))
