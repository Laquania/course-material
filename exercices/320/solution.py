# -*- coding: utf-8 -*-
"""
Created on Wed Sep 24 19:03:10 2014

@author: Amaury
"""

F = open('words', 'r')
A = F.read()

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
q = 0
r = 0
s = 0
t = 0
u = 0
v = 0
w = 0
x = 0
y = 0
z = 0
ù = 0
ä = 0
â = 0
ï = 0
î = 0
ë = 0
ê = 0
ö = 0
ô = 0
ü = 0
û = 0
è = 0
é = 0
à = 0
B = len(A)

for ii in range(len(A)):
    if A[ii] == 'a':
        a = a+1
    elif A[ii] == 'b':
        b = b+1
    elif A[ii] == 'c':
        c = c+1
    elif A[ii] == 'd':
        d = d+1
    elif A[ii] == 'e':
        e = e+1
    elif A[ii] == 'f':
        f = f+1
    elif A[ii] == 'g':
        g = g+1
    elif A[ii] == 'h':
        h = h+1
    elif A[ii] == 'i':
        i = i+1
    elif A[ii] == 'j':
        j = j+1
    elif A[ii] == 'k':
        k = k+1
    elif A[ii] == 'l':
        l = l+1
    elif A[ii] == 'm':
        m = m+1
    elif A[ii] == 'n':
        n = n+1
    elif A[ii] == 'o':
        o = o+1
    elif A[ii] == 'p':
        p = p+1
    elif A[ii] == 'q':
        q = q+1
    elif A[i] == 'r':
        r = r+1
    elif A[ii] == 's':
        s = s+1
    elif A[ii] == 't':
        t = t+1
    elif A[ii] == 'u':
        u = u+1
    elif A[ii] == 'v':
        v = v+1
    elif A[ii] == 'w':
        w = w+1
    elif A[ii] == 'x':
        x = x+1
    elif A[ii] == 'y':
        y = y+1
    elif A[ii] == 'z':
        z = z+1
    elif A[ii] == 'ù':
        ù = ù+1
    elif A[i] == 'à':
        à = à+1
    elif A[ii] == 'é':
        é = é+1
    elif A[ii] == 'è':
        è = è+1
    elif A[ii] == 'û':
        û = û+1
    elif A[ii] == 'ü':
        ü = ü+1
    elif A[ii] == 'ô':
        ô = ô+1
    elif A[ii] == 'ö':
        ö = ö+1
    elif A[ii] == 'ê':
        ê = ê+1
    elif A[ii] == 'ë':
        ë = ë+1
    elif A[ii] == 'î':
        î = î+1
    elif A[i] == 'ï':
        ï = ï+1
    elif A[ii] == 'â':
        â = â+1
    elif A[ii] == 'ä':
        ä = ä+1
#print(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u,v , w, x, y, z, ù, à, é, è, û, ü, ô, ö, ê, ë, î, ï, â, ä)

print(a/B, b/B, c/B, d/B, e/B, f/B, g/B, h/B, i/B, j/B, k/B, l/B, m/B, n/B, o/B, p/B, q/B, r/B, s/B, t/B, u/B, v/B, w/B, x/B, y/B, z/B)



