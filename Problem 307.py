# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:06:23 2024

@author: Kiana Heuser
"""

#Problem 307: Chip Defects
import numpy as np
import math
import random as rdm #----



class Chips:
    def __init__(self, k=3, n=7):
        self.k=k
        self.n=n
    
    def fun(self, n = 10000):
        ausgabe = 0
        defekt = [0]
        for i in range(n):
            for j in range(1,3):
                defekt.append(rdm.choice(range(1,self.n)))
            for k in range(1,n):
                if defekt.count(k) >= 3: # count inperformant?
                    ausgabe = ausgabe + 1
            defekt = [0]
        return(ausgabe)
        
        
        
test4 = Chips(50,3)
test4.fun()
