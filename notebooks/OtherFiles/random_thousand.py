# imports here if necessary
import random.uniform
import numpy as np
# implement the generation function
def generate_values(float lower_bound = 0.0, float upper_bound = 1.0):
    """Generates a numpy array with 1000 floats within an lower_bound and an upper_bound

    Parameters
    ----------
    lower_bound: a float that determines the lower bound of values generated.
    upper_bound: a float that determines the upper bound of values generated.
    """
    if upper_bound <= lower_bound:
        raise ValueError("upper_bound less than or equal to lower_bound")
    # generate array
    rtn = np.random.default_rng().uniform(lower_bound, upper_bound, (1, 1000))
    return rtn