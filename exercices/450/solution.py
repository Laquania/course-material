# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 09:52:26 2014

@author: Amaury
"""

def caesar_cypher(S, key, method):
    import string
    a = list(S)
    b = 0
    c = string.ascii_lowercase
    for i in range(len(a)):
        b = i+key
        if b <= 25:
            a[i] = c[b]
        elif b <= 51 and b > 25:
            a[i] = c[b-25]
        elif b <= 77 and b > 51:
            a[i] = c[b-51]
        elif b <= 103 and b > 77:
            a[i] = c[b-77]
        elif b <= 129 and b > 103:
            a[i] = c[b-103]
    print(a)


import turtle
caesar_cypher('laquania', 5, turtle.forward)
caesar_cypher('qfvzfsnf', 5, turtle.backward)

# qfvzfsnf