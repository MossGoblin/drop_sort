import numpy as np

def get_rand_set(min: int, max: int, size: int):
    set = np.random.randint(min, max, size=size)
    set = set.tolist()
    return set
