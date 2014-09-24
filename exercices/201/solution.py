# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 10:13:07 2014

@author: Amaury
"""

def is_alpha(input):
    a=list(input);
    b=len(a);
    for i in range(b):
        if a[i]=='0':
            a[i]='1';
        elif a[i]=='1':
            a[i]='1';
        elif a[i]=='2':
            a[i]='1';
        elif a[i]=='3':
            a[i]='1';
        elif a[i]=='4':
            a[i]='1';
        elif a[i]=='5':
            a[i]='1';
        elif a[i]=='6':
            a[i]='1';
        elif a[i]=='7':
            a[i]='1';
        elif a[i]=='8':
            a[i]='1';
        elif a[i]=='9':
            a[i]='1';
        elif a[i]=='+':
            a[i]='1';
        elif a[i]=='-':
            a[i]='1';
        elif a[i]=='*':
            a[i]='1';
        elif a[i]=='/':
            a[i]='1';
        elif a[i]=='!':
            a[i]='1';
        elif a[i]=='=':
            a[i]='1';
        elif a[i]=='§':
            a[i]='1';
        elif a[i]==':':
            a[i]='1';
        elif a[i]==';':
            a[i]='1';
        elif a[i]=='.':
            a[i]='1';
        elif a[i]==',':
            a[i]='1';
        elif a[i]=='?':
            a[i]='1';
        elif a[i]=='<':
            a[i]='1';
        elif a[i]=='>':
            a[i]='1';
        elif a[i]=='%':
            a[i]='1';
        elif a[i]=='$':
            a[i]='1';
        elif a[i]=='£':
            a[i]='1';
        elif a[i]=='¤':
            a[i]='1';
        elif a[i]=='}':
            a[i]='1';
        elif a[i]==']':
            a[i]='1';
        elif a[i]=='°':
            a[i]='1';
        elif a[i]=='@':
            a[i]='1';
        elif a[i]=='^':
            a[i]='1';
        elif a[i]=='¨':
            a[i]='1';
        elif a[i]=='`':
            a[i]='1';
        elif a[i]=='|':
            a[i]='1';
        elif a[i]=='[':
            a[i]='1';
        elif a[i]=='{':
            a[i]='1';
        elif a[i]=='#':
            a[i]='1';
        elif a[i]=='~':
            a[i]='1';
        else:
            pass
    
    
    c=0;
    for i in range(b):
        if a[i]=='1':
            c=c+1;
            
    if c !=0:
        print(c)
        print("False")
    else:
        print("True")


#import sys
#is_alpha(sys.argv[1])

   