# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    # ***************************************************
    optimal = np.linalg.solve(tx.transpose()@tx, tx.transpose()@y)
    e = y - tx @ optimal
    mse = 1/(2*len(y)) * e.transpose() @ e
    return mse, optimal


