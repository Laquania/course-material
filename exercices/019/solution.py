# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 14:44:24 2014

@author: Amaury
"""


import sys

if len(sys.argv)>3:
    a=int(sys.argv[1]);
    b=int(sys.argv[2]);
    print(a+b)
    
else:
    print("usage: python3 solution.py OP1 OP2")




