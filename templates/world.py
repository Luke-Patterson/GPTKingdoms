import numpy as np
import sys
from scipy.ndimage.interpolation import zoom
from templates.region import region_symbols
import pandas as pd
import random


class World():
    def __init__(self):
        self.regions = None
        self.map = None

    def generate_map(self, extrapolate_val: int, x_start: int, y_start: int, terrain_probs: dict):
        '''

        :param extrapolate_val: multiplier to x and y length
        :param x_start: starting length of x axis
        :param y_start: starting length of y axis
        :param terrain_probs: probability of each terrain type. Should be a dict with one character keys
        :return: None
        '''

        arr = np.random.uniform(size=(x_start, y_start))
        arr = zoom(arr, extrapolate_val)
        arr = np.where(arr < 0 , 0, arr)
        arr = np.where(arr > 1 , 1, arr)


        assert np.isclose(sum(terrain_probs.values()), 1), 'terrain probabilities do not sum to 1'
        assert all([i in region_symbols.values() for i in terrain_probs.keys()]), 'invalid terrain probability symbols in keys'

        prob_val = 0
        arr_mod = arr.copy()
        for t in terrain_probs.keys():
            loc = (prob_val <= arr) & (arr <= prob_val + terrain_probs[t])
            arr_mod = np.where(loc, t, arr_mod)
            prob_val += terrain_probs[t]

        self.map = pd.DataFrame(arr_mod)


