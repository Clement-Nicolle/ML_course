# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    # ***************************************************
    # INSERT YOUR CODE HERE
    # TODO: compute loss by MSE / MAE
    e=y-tx@w
    return 1/(2*len(y)) * np.transpose(e)@e
    # ***************************************************
    raise NotImplementedError