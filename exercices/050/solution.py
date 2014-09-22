# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 16:45:53 2014

@author: Amaury
"""

a=0;

for i in range(1001):
    if i/3==int(i/3):
        a=a+i;
    if i/5==int(i/5):
        a=a+i;
        
print(a)


