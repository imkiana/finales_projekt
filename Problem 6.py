# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:36:14 2024

@author: Kiana Heuser
"""

#Problem 6:
import pandas as pd
import seaborn as sns

def f(n = 100, plotten = True):
    plot = []
    for j in range(n):
        a=list(range(j+1))
        b=sum(range(j+1))**2
        for i in range(len(a)):
            a[i] = a[i]**2
        print(f"Für n={j} die Differenz ist {abs(b-sum(a))}")
        plot.append(abs(b-sum(a)))
    if plotten == True:
        df = pd.DataFrame({
            "x": range(len(plot)),
            "y": plot
            })
        ax = sns.barplot(data=df, x="x", y="y") 
        plt.xlabel("n")
        plt.ylabel("Differenz")
        plt.title("Differnez von (n+n-1+n-2...n>=0)^2 und n^2+(n-1)^2+(n-2)^2...n>=0")
        ticks = range(0, len(plot), int(len(plot)/20))
        ax.set_xticks(ticks)
        plt.show()
    
f(20)