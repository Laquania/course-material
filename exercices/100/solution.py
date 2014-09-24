# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 17:27:09 2014

@author: Amaury
"""

station = {
 'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET',
 'number': 31705,
 'latitude': 48.8645278209514,
 'name': 'CHAMPEAUX (BAGNOLET)',
 'longitude': 2.416170724425901
}

for element in ('latitude','longitude','number','name','address'):
    print(element,station[element])


