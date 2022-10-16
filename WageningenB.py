#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:45:36 2022

This script contains the Wageningen B function and class J.
class J contains methods that return the parameters that of the speed of advance.

@author: dorus
"""

from Bserie_pol import kt_co, kt_pow, kq_co, kq_pow
import numpy as np
from parameters import ship

def WageningenB_opt(para):
    if len(para) == 4:
        j, pd, EAR, z_ = para
        z = int(round(z_, 0))
    elif len(para) == 2:
        j, pd = para
        z = ship["parameter"]["number_of_blades"]
        EAR = ship["parameter"]["expanded_area_ratio"]

    kt_s, kt_t, kt_u, kt_v = kt_pow[:,0], kt_pow[:,1], kt_pow[:,2],kt_pow[:,3]
    kq_s, kq_t, kq_u, kq_v = kq_pow[:,0], kq_pow[:,1], kq_pow[:,2],kq_pow[:,3]
    
    K_sub_T = 0
    for idx in range(len(kt_co)):
        K_sub_T += kt_co[idx] * j ** kt_s[idx] * pd ** kt_t[idx] * EAR ** kt_u[idx] * z ** kt_v[idx]
    
    K_sub_Q = 0 
    for idx in range(len(kq_co)):
        K_sub_Q += kq_co[idx] * j ** kq_s[idx] * pd ** kq_t[idx] * EAR ** kq_u[idx] * z ** kq_v[idx]

    eta_O = j * K_sub_T / (K_sub_Q * 2 * np.pi)
    
    #print(K_sub_T, K_sub_Q, eta_O)
   
    return K_sub_T, K_sub_Q, eta_O

    
def WageningenB_Kt(para):
    return WageningenB_opt(para)[0]

def WageningenB_Kq(para):
    return WageningenB_opt[1]

def WageningenB_O(para):
    return WageningenB_opt(para)[2] * -1

    
class J:
    def __init__(self, diameter, va, J):
        self.d = diameter
        self.va = va
        self.j = J

    def J(self, n):
        return self.va / (n * self.d)
    
    def n(self):
        return self.va / (self.j * self.d)
    
    def d(self, n):
        return self.va / (self.j * n)
    
    def pitch(self, pd):
        return pd * self.d
        
        
    
