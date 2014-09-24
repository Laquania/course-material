# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:20:30 2014

@author: Amaury
"""

import numpy as N
u = N.zeros(11)
u[0] = 1
u[1] = 2
u[2] = 3

for i in range(3, 10):
    u[i] = u[i-1] + u[i-2]

print(u[0], ', ', u[1], ', ', u[2], ', ', u[3], ', ', u[4], ', ', u[5], ', ', u[6], ', ', u[7], ', ', u[8], ', ', u[9])



