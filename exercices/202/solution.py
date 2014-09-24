# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 11:14:45 2014

@author: Amaury
"""

def starts_with(A, B):
    
    a=list(A);
    b=list(B);
    
    if len(a)<=len(b):
        c=len(a);
    else:
        c=len(b);   
    d=0;
    for i in range(c):
        if a[i]==b[i]:
            d=d+1;
    if len(d)==c:
        print("True")
    else:
           print("False")
            
            
    

#"2nd way
#def starts_with2(A,B):
#    sA=A.split(B)
#    if sA[0] =='':
#        return True
#    return False        
    
#import sys
#A=sys.argv[1];
#B=sys.argv[2];
#starts_with(A,B)

