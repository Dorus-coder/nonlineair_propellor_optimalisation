# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:51:42 2022

@author: dorus
"""
import wageningen_b as wb
import numpy as np

def thrust(R, t):
    """
    R = total resistance
    t = thrust deduction factor
    returns the required thrust to overcome a certain resistance
    """
    return R / (1 - t)

# blz 99

h = 4.725  # height of centerline proppellor to waterline

pd = 0.8   # pitch /diameter
ae = 0.6 
z = 3

for j in np.arange(0, 1.8, 0.01):
    print(wb.wageningenB(j, pd, ae, z))


