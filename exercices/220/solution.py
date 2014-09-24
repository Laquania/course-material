# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 12:39:27 2014

@author: Amaury
"""

def is_prime(num): 
    import numpy as N
    if num == 1 | num == 0:
        return False
    else:
        for i in range(2, int(N.sqrt(num))+1):
            if num % i == 0:
                return False
        print(a)
        return True


for i in range(10000,10050):
    is_prime(i)


