#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:11:10 2022

@author: dorus
"""

import nlopt
import numpy as np

algorithm = "NLOPT_LD_SLSQP"
n         = 3  #


nlopt = nlopt.opt(algorithm, n)

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
