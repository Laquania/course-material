# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 17:40:49 2014

@author: Amaury
"""

def draw_n_squares(n):
    for i in range(n):
        a = n+1
        print(a*"+ --- ", "+ ")
        print(a*"|     ", "|")
        print(a*"+ --- ", "+ ")

draw_n_squares(10)

