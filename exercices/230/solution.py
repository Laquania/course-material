# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


def is_prime2(num):
    import numpy as N
    a = 0
    if num == 1 | num == 0:
        return False
    else:
        for i in range(2, int(N.sqrt(num))+1):
            if num % i == 0:
                a = a+1
        if a == 0:
            return num
        else:
            return 'r'

b = []
for i in range(100000000, 100000200):
    if is_prime2(i) != 'r':
        b = b + [is_prime2(i)]

print(b[0])



