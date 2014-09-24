# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 11:41:31 2014

@author: Amaury
"""

#def is_prime(num):
#    
#    if num/2==int(num/2):
#        print("false")
#    elif num/3==int(num/3):
#        print("false")
#    elif num/5==int(num/5):
#        print("false")
#    elif num/7==int(num/7):
#        print("false")
#    elif num/11==int(num/11):
#        print("false")
#    elif num/13==int(num/13):
#        print("false")
#    elif num/17==int(num/17):
#        print("false")
#    elif num/19==int(num/19):
#        print("false")
#    elif num/23==int(num/23):
#        print("false")
#    elif num/29==int(num/29):
#        print("false")    
#    elif num/31==int(num/31):
#        print("false")
#    elif num/37==int(num/37):
#        print("false")
#    elif num/41==int(num/41):
#        print("false")
#    elif num/43==int(num/43):
#        print("false")
#    elif num/47==int(num/47):
#        print("false")
#    elif num/53==int(num/53):
#        print("false")
#    elif num/59==int(num/59):
#        print("false")
#    elif num/61==int(num/61):
#        print("false")
#    elif num/67==int(num/67):
#        print("false")
#    elif num/71==int(num/71):
#        print("false")
#    elif num/73==int(num/73):
#        print("false")
#    elif num/79==int(num/79):
#        print("false")
#    elif num/83==int(num/83):
#        print("false")
#    elif num/89==int(num/89):
#        print("false")
#    elif num/97==int(num/97):
#        print("false")
#    else:
#        print("true")
#        
#        
#import sys
#is_prime(int(sys.argv[1]))

def is_prime2(num):
    import numpy as N
    a = 0;
    if num == 1 | num == 0:
        return False
    else:
        for i in range(2, int(N.sqrt(num))+1):
            if num % i == 0:
                a = a+1;
        if a == 0:
            return True
        else:
            return False
