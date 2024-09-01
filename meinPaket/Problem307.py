# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 19:06:23 2024

@author: Kiana Heuser
"""

#Problem 307: Chip Defects
import random as rdm



class Chips:
    '''Klasse zur Simulation fehlerhafter Chips'''
    def __init__(self, k=3, n=7):
        self.k=k
        self.n=n
    
    def fun(self, it = 1000):
        '''Simuliert die WSK für drei oder mehr der k Defekte, welche zufällig auf einen der n Chips verteilt werden.'''
        ausgabe = 0
        defekt = []
        for i in range(it):
            stop = False
            for j in range(self.k):
                defekt.append(rdm.choice(range(1,self.n+1)))
            for k in range(self.n):
                if defekt.count(k) >= 3: #nach 3 oder mehr gleichen zahlen suchen
                    ausgabe = ausgabe + 1
                    stop = True #wir wollen nur wissen ob es einen solchen fall gab, daher müssen wir die for schleife beenden
                if stop == True: #damit wir nicht doppelt zählen für fälle in denen mehrere chips 3 oder mehr defekte haben
                    break
            defekt = [] #defekt resetten für den nächsten durchlauf
        return(ausgabe/it)
        
        
        
#test4 = Chips()
#test4.fun()
