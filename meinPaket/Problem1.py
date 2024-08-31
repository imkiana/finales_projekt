# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 08:29:25 2024

@author: Kiana Heuser
"""
#Problem 1: faktor von 3 oder 5
import numpy as np


def f1(n):
    '''Summiert alle Faktoren von 3 und 5 von 0 bis n'''
    ausgabe = []
    for i in range(0,n-int(n/abs(n)),int(n/abs(n))): # numbers BELOW n
       ausgabe.append([b if b % 3 == 0 else b if b % 5 == 0 else 0 for b in [i+int(n/abs(n))]])
    return(np.cumsum(ausgabe)[abs(n)-2]) # sum hat nicht funktioniert
    
f1(100)
