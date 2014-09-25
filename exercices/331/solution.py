# -*- coding: utf-8 -*-
"""
Created on Thu Sep 25 09:49:06 2014

@au
"""

import json
F = open("velib.json")
a = json.load(F)

for i in a:
    add = str(i["address"])
    c = add.split('- ')
    if len(c) > 2:
        dsecond = c[1]
        b = c[2]
        dprime = c[0]
        d = dprime+' - '+dsecond
        e = b.split(' ')
        f = e[0]
        g = e[1]
        i["address"] = str.strip(str(d))
        i["codezip"] = f
        i["city"] = g
    else:
        b = c[1]
        d = c[0]
        e = b.split(' ')
        f = e[0]
        g = e[1]
        i["address"] = str.strip(str(d))
        i["codezip"] = f
        i["city"] = g
    add2 = str(i["name"])
    c2 = add2.split(' - ')
    if len(c2) > 2:
        d2prime = c2[1]
        d2second = c2[2]
        d2 = d2prime+' - '+d2second
        i["name"] = d2
    else:
        d2 = c2[1]
        i["name"] = d2

F.close()
F = open('solution_velib.json', 'w')
F.write(json.dumps(a))
F.close()