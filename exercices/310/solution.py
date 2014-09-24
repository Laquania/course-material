# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 18:58:27 2014

@author: Amaury
"""

f = open('words', 'r')
a = f.read()
#print(a)
c = 0
for i in range(len(a)):
    if a[i] == 'e':
        c = c + 1
print(c)

