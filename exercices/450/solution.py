# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 09:52:26 2014

@author: Amaury
"""

def caesar_cypher(S, key, method):
    a = list(S)
    b = 0
    d = list(method)
    for i in range(len(a)-1):
        e = 0
        f = 0
        for k in range(len(a)):
            if k+97 == ord(a[i]):
                print(k)
                for j in range(len(d)):
                    e = e+ord(d[j])
                    if e == 757:     #forward
                        b = i+key
                    elif e == 831:   #backward
                        b = i-key
                    if b > 122 and b <= 147:
                        f = b-25
                    elif b > 147 and b <= 172:
                        f = b-50
                    elif b > 172 and b <= 197:
                        f = b-75
                    else:
                        f = b
                    print(f)
                    a[i] = chr(f)
        print(a)   #.decode('utf-8')

caesar_cypher('laquania', 5, 'forward')
caesar_cypher('qfvzfsnf', 5, 'backward')
