
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:47:06 2021


@author: Ole Vermeer and Dorus Boogaard

@author: Ole Vermeer en Dorus Boogaard

"""

from matplotlib import pyplot as plt
import numpy as np
import math
from parameters import ship


def wageningenB(para, grad=None):
    pd = 1.24
    n = para
    z = 3
    ae = 0.7
    va = ship["parameters"]["speed_of_advance"]
    d = ship["parameters"]["propellor_diameter"]
    j = va / (n * d)
    if grad:
        """
        Compute the partial derivates of the objective function.
        This is only needed for gradient based algorithms.
        """
        grad[0] = 0
        grad[1] = 0
        grad[2] = 0
        grad[3] = 0

        
        
    kt_terms = np.array(
        [[0.00880496000000000, -0.204554000000000, 0.166351000000000, 0.158114000000000, -0.147581000000000,
          -0.481497000000000, 0.415437000000000, 0.0144043000000000, -0.0530054000000000,
          0.0143481000000000,
          0.0606826000000000, -0.0125894000000000, 0.0109689000000000, -0.133698000000000,
          0.00638407000000000, -0.00132718000000000, 0.168496000000000, -0.0507214000000000,
          0.0854559000000000, -0.0504475000000000,
          0.0104650000000000, -0.00648272000000000, -0.00841728000000000, 0.0168424000000000,
          -0.00102296000000000, -0.0317791000000000, 0.0186040000000000, -0.00410798000000000,
          -0.000606848000000000, -0.00498190000000000, 0.00259830000000000, -0.000560528000000000,
          -0.00163652000000000, -0.000328787000000000, 0.000116502000000000,
          0.000690904000000000, 0.00421749000000000, 5.65229000000000e-05, -0.00146564000000000],
         [0, 1, 0, 0, 2, 1, 0, 0, 2, 0, 1, 0, 1, 0, 0, 2, 3, 0, 2, 3, 1, 2, 0, 1, 3, 0, 1, 0, 0, 1, 2, 3, 1,
          1, 2,
          0, 0, 3, 0],
         [0, 0, 1, 2, 0, 1, 2, 0, 0, 1, 1, 0, 0, 3, 6, 6, 0, 0, 0, 0, 6, 6, 3, 3, 3, 3, 0, 2, 0, 0, 0, 0, 2,
          6, 6,
          0, 3, 6, 3],
         [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 2, 2, 2, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 0,
          0, 0,
          1, 1, 1, 2],
         [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
          2, 2,
          2, 2, 2, 2]])
    
    kq_terms = np.array(
        [[0.00379368000000000, 0.00886523000000000, -0.0322410000000000, 0.00344778000000000, -0.0408811000000000,
          -0.108009000000000, -0.0885381000000000, 0.188561000000000, -0.00370871000000000, 0.00513696000000000,
          0.0209449000000000,
          0.00474319000000000, -0.00723408000000000, 0.00438388000000000, -0.0269403000000000, 0.0558082000000000,
          0.0161886000000000,
          0.00318086000000000, 0.0158960000000000, 0.0471729000000000, 0.0196283000000000, -0.0502782000000000,
          -0.0300550000000000,
          0.0417122000000000, -0.0397722000000000, -0.00350024000000000, -0.0106854000000000, 0.00110903000000000,
          -0.000313912000000000,
          0.00359850000000000, -0.00142121000000000, -0.00383637000000000, 0.0126803000000000,
          -0.00318278000000000, 0.00334268000000000,
          -0.00183491000000000, 0.000112451000000000, -2.97228000000000e-05, 0.000269551000000000,
          0.000832650000000000,
          0.00155334000000000, 0.000302683000000000, -0.000184300000000000, -0.000425399000000000,
          8.69243000000000e-05,
          -0.000465900000000000, 5.54194000000000e-05],
         [0, 2, 1, 0, 0, 1, 2, 0, 1, 0, 1, 2, 2, 1, 0, 3, 0, 1, 0, 1, 3, 0, 3, 2, 0, 0, 3, 3, 0, 3, 0, 1, 0, 2, 0,
          1, 3, 3, 1, 2, 0, 0, 0, 0, 3, 0, 1],
         [0, 0, 1, 2, 1, 1, 1, 2, 0, 1, 1, 1, 0, 1, 2, 0, 3, 3, 0, 0, 0, 1, 1, 2, 3, 6, 0, 3, 6, 0, 6, 0, 2, 3, 6,
          1, 2, 6, 0, 0, 2, 6, 0, 3, 3, 6, 6],
         [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1, 1, 2, 2, 2, 2,
          0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]])
    
    kt_empty = []
    kt_empty.clear()
    c = kt_terms[0]
    s = kt_terms[1]
    t = kt_terms[2]
    u = kt_terms[3]
    v = kt_terms[4]
    for i in range(len(c)):
        T = c[i] * j ** s[i] * pd ** t[i] * ae ** u[i] * z ** v[i]

        if T > 0: kt_empty.append(T)

        kt_empty.append(T)

    Kt = sum(kt_empty)
    kq_empty = []
    kq_empty.clear()
    c = kq_terms[0]
    s = kq_terms[1]
    t = kq_terms[2]
    u = kq_terms[3]
    v = kq_terms[4]
    for i in range(len(c)):
        Q = c[i] * j ** s[i] * pd ** t[i] * ae ** u[i] * z ** v[i]

        if Q > 0: kq_empty.append(Q)

        kq_empty.append(Q)

    Kq = sum(kq_empty)
    Rn = 2*pow(10, 6) * ae * (1 / z) 
    if Rn >= 2 * pow(10, 6):
        """
        polynomials for Reynolds number effect (above Reynolds = 2*10^6)
        on Kt and Kq. 
        DKT = delta Kt
        DKQ = delta Kq
        """
        A1  = pow(ae, 1)
        A2  = pow(ae, 2)
        J2  = pow(j, 2)
        P1  = pd
        J1  = j
        lR1 = (math.log10(Rn) - 0.301)
        lR2 = pow((math.log10(Rn) - 0.301), 2)
        P6  = pow(pd, 6)
        P3  = pow(pd, 3)
        P2  = pow(pd, 2)
        Z1  = z
        Z2  = pow(z, 2)
        DKT = 0.000353485
        -0.00333758*A1*J2
        -0.00478125*A1*P1*J1
        +0.000257792*lR2*A1*J2
        +0.0000643192*lR1*P6*J2
        -0.0000110636*lR2*P6*J2
        -0.0000276305*lR2*Z1*A1*J2
        +0.0000954*lR1*Z1*P1*J1
        +0.0000032049*lR1*Z2*A1*P3*J1
    
        DKQ = -0.000591412
        +0.00696898*P1
        -0.0000666654*Z1*P6
        +0.0160818*A2
        -0.00093809*lR1*P1
        -0.00059593*lR1*P2
        +0.0000782099*lR2*P2
        +0.0000052199*lR1*Z1*A1*J2
        -0.00000088528*lR2*Z1*A1*P1*J1
        +0.0000230171*lR1*Z1*P6
        -0.00000184341*lR2*Z1*P6
        -0.00400252*lR1*A2
        +0.000220915*lR2*A2
    else:
        DKT = 0
        DKQ = 0

        

    

    Kt += DKT
    Kq += DKQ
    if j != 0:
        eta_o = j / (2 * math.pi) * Kt / Kq
    else:
        eta_o = 0
    # kt, kq left out for optimalisation of eta_o
    print(f"Kt: {Kt}, Kq: {Kq}, eta_o:{eta_o}, input: n {n}")
    return eta_o * -1



def aufmKeller(z, T, D, rho=1025, g=9.81, k=0.15, patm=1*10**5, pv=1706):
    """
    z  = number of blades
    T  = thrust
    D  = propellor diameter
    k = 0.15 for E.S.S propellors from CuNiAl
    rho = 1025 kg/m**3  density of the water
    patm = 1*10**5 Pa   atmosferic pressure
    pv = 1706 Pa vapour pressure @ 15 degrees celcius
    
    returns the minimum expanded area ratio of a propellor to be free of cavitation. 
    """
    return (1.3 + 0.3 * z) * T / ((patm - pv) * D ** 2) + k
    


def lijnenplot(ae,z):
    Kt = []
    Kq = []
    Eta_o = []
    Jt = []
    Jq = []
    Je = []
    start = 0.4
    stop = 1.5
    plt.figure(figsize =(10,5),dpi = 100)
    for pd in np.arange(start, stop, 0.1):
        for j in np.arange(0, 1.7, 0.001):
            kt,kq,eta_o = wageningenB(j,pd,ae,z)
            kq = kq *10 

    start = 0.4   # First P/D value
    stop = 1.6    # last + 1 P/D value
    plt.figure(figsize =(10,5),dpi = 100)
    for pd in np.arange(start, stop, 0.1):
        for j in np.arange(0, 1.7, 0.001):
            kt, kq, eta_o = wageningenB(j,pd,ae,z)
            kq *= 10

            if kt > 0:
                Jt.append(j)    
                Kt.append(kt)
            if kq > 0 :
                Jq.append(j)    
                Kq.append(kq)
            if 0 < eta_o < 1:
                Eta_o.append(eta_o)
                Je.append(j)
        plt.plot(Jt,Kt,color = "red",label = "Kt")
        plt.plot(Jq,Kq, color = "black", label = "Kq")
        plt.plot(Je,Eta_o, color = "green", label = "Eta_o")
        Kt.clear()
        Kq.clear()
        Eta_o.clear()
        Jt.clear()
        Jq.clear()
        Je.clear()
    plt.ylabel("Kt, 10Kq, Eta_o")
    plt.xlabel("J [-]")

    plt.suptitle(f"P/D from {start/10} to {(stop-1)/10}")

    plt.suptitle(f"P/D from {start} to {(stop - 0.1)}")

    plt.title("Diagram of B" + str(z) + "-" + str(ae))
    plt.grid()
    plt.show()
    plt.clf() 
    Kt.clear()
    Kq.clear()
    Eta_o.clear()
    Jt.clear()
    Jq.clear()

    Je.clear()


    Je.clear()
    


