# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    a,b=tx.shape
    eye = np.eye(b)
    w = np.linalg.solve(2*a*lambda_*eye + tx.transpose()@tx, tx.transpose()@y)
    e = y - tx @ w
    mse = 1/(2*len(y)) * e.transpose() @ e
    return mse, w
