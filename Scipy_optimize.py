# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 21:35:46 2022

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html#scipy.optimize.differential_evolution

@author: dorus
"""
from scipy.optimize import differential_evolution
from wageningen_b import wageningenB

bounds = [(0, 5), (0.4, 1.5), (0.3, 1.05), (2, 6)]

strategies = ["randtobest1exp", "rand2exp"]

result = differential_evolution(wageningenB, bounds, strategy=strategies[1])

print(result)