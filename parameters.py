#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:25:38 2022

@author: dorus
"""


ship = {"metadata": {
            "units": "SI",
            "resistance": "kN"
            
        },
        "parameter": {
            "name" :"",
            "design_speed": 7.72,
            "speed_of_advance": 5.4,
            "Resistance": 250,
            "wake_factor": 0.3,
            "thrust_de_factor":0.18,
            "number_of_blades": 4,
            "propellor_diameter": 3.5,
            "expanded_area_ratio": 0.6
        },
        "constraints":{
            "rps": [0, 5],
            "EAR": [0.3, 1.05],
            "PD" : [0.4, 1.5]
            }
        }
        


