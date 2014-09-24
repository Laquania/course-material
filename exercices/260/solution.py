# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:57:23 2014

@author: Amaury
"""

def np_euclidean(a, b):
    import numpy as N
    c = len(a)
    d = 0
    for i in range(c):
        d = d + (b[i]-a[i])**2
    print(N.sqrt(d))

#a = [1, 5, 7]
#b = [2, 8, 3]
#
#euclidean(a, b)

def opt_euclidean(a, b):
    import math as M
    c = len(a)
    d = 0
    for i in range(c):
        d = d + (b[i]-a[i])**2
    print(M.sqrt(d))


def euclidean(a, b):
    c = len(a)
    d = 0
    for i in range(c):
        d = d + (b[i]-a[i])**2
    print((d)**(0.5))    

