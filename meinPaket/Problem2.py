# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:40:49 2024

@author: Kiana Heuser
"""

#Problem 2: gerade Fib nummern
import math 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class Fibonacci:
    '''Klasse zur darstellung gerade Fibonacci Zahlen'''
    def __init__(self, maximal=4_000_000, startzahl=1):
        self.maximal = maximal
        self.startzahl = startzahl
    
    def fun(self, plotten = True):
        '''Summiert alle geraden Fibonacci Zahlen von Fibonacci Zahl n = startzahl bis maximal'''
        fi = round((1.6180339887**(self.startzahl+1)-(1.6180339887)**-(self.startzahl+1))/np.sqrt(5)) #erstellt start fibonacci nummer
        ausgabe = list()
        fibefore = round((1.6180339887**(self.startzahl)-(1.6180339887)**-(self.startzahl))/np.sqrt(5)) #vorherige fibonacci zahl der startzahl um die die reihe effizient zu erweitern
        while fi < self.maximal:
            if fi % 2 == 0:
                ausgabe.append(1)
            else:
                ausgabe.append(0) 
            buffer = fi
            fi = fi + fibefore
            fibefore = buffer
        print(f"Insgesamt gab es {sum(ausgabe)} gerade Zahlen, bis zur Zahl {fibefore}.") #Ausgabe
        if plotten == True: #plotten
            df = pd.DataFrame({
                "x": range(len(np.cumsum(ausgabe))),
                "y": np.cumsum(ausgabe)
            })
            colors = ["firebrick" if b == 1 else "teal" for b in ausgabe]
            ax = sns.barplot(data=df, x="x", y="y", palette=colors, hue= "x", legend=False) 
            plt.xlabel("Index ab Startzahl")
            plt.ylabel("Kumulierte Anzahl gerader Zahlen")
            plt.title("Verteilung der geraden Fibonacci-Zahlen")
            ticks = range(0, len(ausgabe), math.ceil(len(ausgabe)/20))
            ax.set_xticks(ticks)
            plt.show()
            
#test = Fibonacci()
#test.fun()
