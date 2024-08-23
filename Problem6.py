# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:36:14 2024

@author: Kiana Heuser
"""

#Problem 6 Differenzen:
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def f(n = 100, plotten = True):
    '''Berechnet die Differenz der Summe der Quadrate der Zahl n und dem Quadrat der Summe und Plottet dies von 1 bis n'''
    plot = []
    for j in range(1,n+1):
        a=list(range(j+1))
        b=sum(range(j+1))**2
        for i in range(len(a)):
            a[i] = a[i]**2
        plot.append(abs(b-sum(a)))
    print(f"Für n={j} die Differenz ist {abs(b-sum(a))}")
    if plotten == True:
        df = pd.DataFrame({
            "x": range(1,len(plot)+1),
            "y": plot
            })
        ax = sns.barplot(data=df, x="x", y="y") 
        plt.xlabel("n")
        plt.ylabel("Differenz")
        plt.title("Differnez von (n+n-1+n-2...n>=0)² und n²+(n-1)²+(n-2)²...n>=0")
        ticks = range(0, len(plot), math.ceil(len(plot)/20))
        ax.set_xticks(ticks)
        plt.show()
    
f(5)