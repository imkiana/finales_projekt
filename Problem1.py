# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 08:29:25 2024

@author: Kiana Heuser
"""
#Problem 1: faktor von 3 oder 5
import numpy as np


def f(n):
    ausgabe = []
    for i in range(n-1): # numbers BELOW n
       ausgabe.append([b if b % 3 == 0 else b if b % 5 == 0 else 0 for b in [i+1]])
    return(np.cumsum(ausgabe)[n-2]) # sum hat nicht funktioniert
    
f(1000)