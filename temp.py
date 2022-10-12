# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 20:51:42 2022

@author: dorus
"""
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
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


incr = 0.01
J = np.arange(0, 1.8, incr, dtype=float)
xline = np.full_like(J, 1)
yline = np.full_like(J, 1)
zline = np.full_like(J, 1)


L = []
for i in range(len(xline)):
    j = i * incr
    xline[i], yline[i], zline[i] = wb.wageningenB(j, pd, ae, z)

ax = plt.axes(projection='3d')
ax.plot3D(xline, yline, zline, 'green')

wb.lijnenplot(ae, z)