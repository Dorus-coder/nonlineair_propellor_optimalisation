#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:11:10 2022

@author: dorus

Waarschijnlijk is er
"""

import nlopt
from WageningenB import WageningenB_O, WageningenB_pol, WageningenB_Kt, WageningenB_Kq
import numpy as np




algorithms = ["NLOPT_LD_SLSQP", "NLOPT_LN_NEWUOA_BOUND", "NLOPT_AUGLAG", "NLOPT_GN_DIRECT_L_RAND"]
# Number of optimizations parameters
# rps, pd, EAR, z
n         = 2

lb = [0, 0.4]
ub = [5, 1.5]

nlopt = nlopt.opt(algorithms[-1], n)

nlopt.set_lower_bounds(lb)
nlopt.set_upper_bounds(ub)

nlopt.set_max_objective(WageningenB_O)
# Stopping criteria: stops when an objective value of at least n is found
#nlopt.set_ftol_abs(0.8)
nlopt.add_inequality_constraint(lambda para, grad: WageningenB_Kt(para, grad))
nlopt.add_inequality_constraint(lambda para, grad: WageningenB_Kq(para, grad))

# initial gues
x = nlopt.optimize([1, 1.2])

maxf = nlopt.last_optimum_value()

print("optimum at ", x[0], x[1])
print("minimum value = ", maxf)
print("result code = ", nlopt.last_optimize_result())







