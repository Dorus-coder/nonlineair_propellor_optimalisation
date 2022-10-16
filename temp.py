#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 16:08:45 2022

@author: dorus

This module prints the properties of the propellor.
J and P/D have a manual input!

"""
import numpy as np
from WageningenB import WageningenB_opt, J
from parameters import ship



    
n_ = J(3.5, 5.4, 1.24)
j = 1.24
pd = 1.4
K_t, K_q, eta_O = WageningenB_opt([j, pd])[0], WageningenB_opt([1.24, 1.4])[1], WageningenB_opt([1.24, 1.4])[2]

print(f"K_t: {round(K_t, 2)}")
print(f"K_q: {round(K_q, 2)}")
print(f"eta_O: {round(eta_O, 2)}")
print("for parameters: ")
print(f"EAR:  {ship['parameter']['expanded_area_ratio']}")
print(f"number of blades: {ship['parameter']['number_of_blades']}")
print(f"speed of advance: {j}")
print(f"P/D: {pd}")
print()
print("n: " + str(round(n_.n(), 2)) + " rps")
print("n: " + str(round(n_.n() * 60)) + " rpm")
print("pitch: " + str(round(n_.pitch(1.4), 2)) + " m.")

