# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:42:16 2024

@author: Kiana Heuser
"""

#Problem 44: Prentagon Numbers
import itertools

def f44():
    '''Löst das Problem 44 von Project Euler'''
    num = []
    while True:
        num.append((len(num)+1)*(3*(len(num)+1)-1)/2) #Nummer der Reihe zu num hinzufügen
        if len(num)>3: #2394
            combination = list(itertools.combinations(num, 2)) #alle kombinationen für plus und minus erstellen
            for i in range(len(combination)):
                plus = combination[i][0]+combination[i][1]
                minus = abs(combination[i][0]-combination[i][1])
                if plus in num and minus in num:
                    return(plus,minus)       
#f44()
# Die Funktion dauert etwas, daher hier schon mal die Antwort: 
#plus = 8602840,  D oder minus = 5482660 
#num 1 = 1560090
#num 2 = 7042750