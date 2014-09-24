# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 09:11:52 2014

@author: Amaury
"""

import sys

if len(sys.argv)>3:
    if sys.argv[2]=='-':
        print(int(sys.argv[1])-int(sys.argv[3]))
    elif sys.argv[2]=='+':
        print(int(sys.argv[1])+int(sys.argv[3]))
    elif sys.argv[2]=='x':  #python vs windows ----> utiliser 'x' et non '*'
        print(int(sys.argv[1]) * int(sys.argv[3]))
    elif sys.argv[2]=='/':
        if sys.argv[3]!=0:
            print(int(sys.argv[1])/int(sys.argv[3]))
        else:
            print("input error")
    elif sys.argv[2]=='^': 
        print(int(sys.argv[1]) ** int(sys.argv[3]))
    elif sys.argv[2]=='%':
        if sys.argv[3]!=0:
            print(int(sys.argv[1])%int(sys.argv[3]))
        else:
            print("input error")
else:
    print("usage: python3 ./solution.py a_number (an_operator +-*/%^) a_number")
