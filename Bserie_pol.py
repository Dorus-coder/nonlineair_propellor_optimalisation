# -*- coding: utf-8 -*-
"""
Read the kt and kq powers from the Wageningen B polinomials.
The Bserie.txt file is just for information and not used in this script. There is a hidden copy
to prevent changes to the file.
"""

import numpy as np

with open('.txt') as terms:
    bserie = terms.readlines()
    
kt_co = np.empty(39)  
kt_pow = np.empty((len(kt_co), 4))
kq_co = np.empty(47)
kq_pow = np.empty((len(kq_co), 4))
kt_strings = ""
kq_strings = ""
terms_a = []
kt_u = np.empty_like(kt_co)

for idx in range(len(kt_co)):
    kt_co[idx] = bserie[idx + 1]

for idx in range(len(kq_co)):
    kq_co[idx] = bserie[idx + 42]
  
for elem in bserie[91:130]:
    kt_strings += elem
    
for elem in bserie[132:179]:
    kq_strings += elem

kt_strings = kt_strings.replace("\n", "")
kt_strings = kt_strings.replace(" ", "")
kq_strings = kq_strings.replace("\n", "")
kq_strings = kq_strings.replace(" ", "")

counter = 0

for idx in range(len(kt_pow)):
    for i in range(len(kt_pow[idx])):
         kt_pow[idx][i] = kt_strings[counter]
         counter += 1
         
counter = 0       

for idx in range(len(kq_pow)):
    for i in range(len(kq_pow[idx])):
         kq_pow[idx][i] = kq_strings[counter]
         counter += 1


    
    