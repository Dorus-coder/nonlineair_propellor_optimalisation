#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:11:10 2022

@author: dorus
"""

import nlopt
from wageningen_b import wageningenB as WB


algorithms = ["NLOPT_LD_SLSQP", "NLOPT_LN_NEWUOA_BOUND", "NLOPT_AUGLAG" ]
# Number of optimizations parameters
# rps, pd, EAR, z
n         = 4  

lb = [0, 0.4, 0.3, 2]
ub = [5, 1.5, 1.05, 6]

nlopt = nlopt.opt(algorithms[2], n)
nlopt.set_lower_bounds(lb)
nlopt.set_upper_bounds(ub)

nlopt.set_max_objective(WB)
# Stopping criteria: stops when an objective value of at least n is found
#nlopt.set_ftol_abs(0.8)

# initial gues
x = nlopt.optimize([1, 0.5, 0.6, 3])


maxf = nlopt.last_optimum_value()

print("optimum at ", x[0], x[1], x[2], x[3])
print("minimum value = ", maxf)
print("result code = ", nlopt.last_optimize_result())

def constraint1():
    """
    Make a functions that constraints on rps

    Returns
    -------
    None.

    """
    pass



def constraint2():
    """
    Make a functions that contrains on EAR

    Returns
    -------
    None.

    """
    pass



def constraint3():
    """
    Make a function that constrains PD

    Returns
    -------
    None.

    """
    pass
