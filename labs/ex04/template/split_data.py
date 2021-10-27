# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    # INSERT YOUR CODE HERE
    # split the data based on the given ratio: TODO
    np.random.shuffle(x)
    np.random.seed(seed)
    np.random.shuffle(y)
    n = ratio * len(y)
    n = int(n)
    return x[:n], y[:n], x[n:], y[n:]
    # ***************************************************
