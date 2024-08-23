# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:06:23 2024

@author: Kiana Heuser
"""

#Problem 307: Chip Defects
import random as rdm #----



class Chips:
    def __init__(self, k=3, n=7):
        self.k=k
        self.n=n
    
    def fun(self, it = 1000):
        ausgabe = 0
        defekt = []
        for i in range(it):
            stop = False
            for j in range(self.k):
                defekt.append(rdm.choice(range(1,self.n+1)))
            print(defekt)
            for k in range(self.n):
                if defekt.count(k) >= 3: # count funktioniert nicht? 
                    ausgabe = ausgabe + 1
                    stop = True
                if stop == True:
                    break
            defekt = []
        return(ausgabe/it)
        
        
        
test4 = Chips()
test4.fun()
