# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:04:14 2022

@author: dorus
Example from https://nlopt.readthedocs.io/en/latest/NLopt_Tutorial/#example-in-python
https://stackoverflow.com/questions/55113568/how-to-set-up-nlopt-with-multiple-inequality-constraints
"""

import nlopt
import numpy as np

def example_1():
    def myfunc(x, grad):
        if grad.size > 0:
            grad[0] = 0.0
            grad[1] = 0.5 / np.sqrt(x[1])
        return np.sqrt(x[1])
    
    
    def myconstraint(x, grad, a, b):
        if grad.size > 0:
            grad[0] = 3 * a * (a*x[0] + b)**2
            grad[1] = -1.0
        return (a*x[0] + b)**3 - x[1]
    
    
    opt = nlopt.opt(nlopt.LD_MMA, 2)
    
    opt.set_lower_bounds([-float('inf'), 0])
    
    opt.set_min_objective(myfunc)
    
    opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,2,0), 1e-8)
    opt.add_inequality_constraint(lambda x,grad: myconstraint(x,grad,-1,1), 1e-8)
    
    
    x = opt.optimize([1.234, 5.678])
    minf = opt.last_optimum_value()
    
    print("optimum at ", x[0], x[1])
    print("minimum value = ", minf)
    print("result code = ", opt.last_optimize_result())
    
def example_2():
    pass

example_1()