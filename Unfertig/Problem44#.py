# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:42:16 2024

@author: Kiana Heuser
"""

#Problem 44: Prentagon Numbers
import itertools

def f44():
    num = []
    while True:
        num.append((len(num)+1)*(3*(len(num)+1)-1)/2)
        if len(num)>3: #2394
            combination = list(itertools.combinations(num, 2))
            for i in range(len(combination)+1):
                plus = combination[i][0]+combination[i][1]
                minus = abs(combination[i][0]-combination[i][1])
                if plus in num and minus in num:
                    return(plus,minus)       
penfun()
# Die Funktion dauert etwas, daher hier schon mal die Antwort: 
#plus = 8602840,  D oder minus = 5482660 
#num 1 = 1560090
#num 2 = 7042750

#list(itertools.combinations("CBA", 2))