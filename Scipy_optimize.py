
"""
Created on Wed Oct 12 21:35:46 2022

https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.differential_evolution.html#scipy.optimize.differential_evolution
rand2exp has the least iterations (34).


@author: dorus
"""
from scipy.optimize import differential_evolution, NonlinearConstraint
from WageningenB import WageningenB_O, WageningenB_Kt, WageningenB_Kq
import numpy as np

desired_optimization = 1

if desired_optimization == 0:
    """
    The best theoretical choice from the Wageningen B propellors.
    bounds = [speed of advance, P/D, expanded area ratio, number of propellors]
    """
    bounds = [(0, 1.40), (0.4, 1.4), (0.3, 1.05), (2, 6)]
    
    
elif desired_optimization == 1:
    """
    Number of blades and EAR predetermined.
    bounds = [speed of advance, P/D]
    """
    bounds = [(0, 1.40), (0.4, 1.4)]


con1 = lambda para: WageningenB_Kt(para)
con2 = lambda para: WageningenB_Kq(para)

nlc1 = NonlinearConstraint(con1, 0, np.inf)
nlc2 = NonlinearConstraint(con2, 0, np.inf)

strategies = ['best1bin',
              'best1exp',
              'rand1exp',
              'randtobest1exp',
              'currenttobest1exp',
              'best2exp',
              'rand2exp',
              'randtobest1bin',
              'currenttobest1bin',
              'best2bin',
              'rand2bin',
              'rand1bin']

D = {}

for idx in range(len(strategies)):
    D[strategies[idx]] = differential_evolution(WageningenB_O, bounds, strategy=strategies[idx], constraints=nlc1)

best_strategy = D[strategies[0]]


for strategy in D:
    if best_strategy.nit < D[strategy].nit:
        best_strategy = D[strategy]
        name = strategy
        
print(f"best strategy is: {name}")

print(best_strategy)
