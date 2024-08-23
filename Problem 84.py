# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:19:48 2024

@author: Kiana Heuser
"""


#Problem 84: Monopoly Odds
import random as rdm #----
from collections import Counter
import matplotlib.patches as patches
import numpy as np
import matplotlib.pyplot as plt



class Monopoly:
    def __init__(self, dice_dn=4):
        self.dice_dn = dice_dn
        
        
    def fun(self, n=100_000, plotten = True):
        feld = 1
        ausgabe = list()
        for i in range(1,n):
            feld = (feld + np.random.randint(1,self.dice_dn+1) - 1) % 40 + 1
            if feld in [3,18,34]: #CC
                karte = rdm.choice([1,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0]) #2/16 
                if karte > 0:
                    feld = karte
            if feld in [8,23,37]: #CH  #"Next" vertanden als "next clockwise" 
                karte = rdm.choice([1,11,12,25,40,6,feld//10*10+6,feld//10*10+6,"U",feld-3,0,0,0,0,0,0]) #10/16
                if karte == "U":
                    if feld//10 < 13:
                        feld = 13
                    if feld//10 >= 13:
                        feld = 29
                
                else:
                    if karte > 0:
                        feld = karte
                        
                
            ausgabe.append(feld)
        counts = Counter(ausgabe)
        feldernum = list(counts.keys())
        values = list(counts.values())
        fürausgabe = list(zip(values, feldernum))
        fürausgabe.sort(reverse=True)
        fürausgabeval, fürausgabenum = zip(*fürausgabe[:3])
        fürausgabenum = list(fürausgabenum)
        if any(a<10 for a in fürausgabenum): #any(fürausgabenum<10) warum geht das nicht
            fürausgabenum = [("0" + str(b) if b < 10 else str(b)) for b in fürausgabenum]
            lösung = str(fürausgabenum[0])+str(fürausgabenum[1])+str(fürausgabenum[2])
        else:
            lösung = str(fürausgabenum[0])+str(fürausgabenum[1])+str(fürausgabenum[2])
        fürausgabeval = list(fürausgabeval)
        for k in range(3):
            fürausgabeval[k] = fürausgabeval[k]/n*1000//1/10
        print(f"Die Felder {fürausgabenum} haben mit {fürausgabeval}% die höchsten Wahrscheinlichkeiten.\nDaher lautet die Antwort auf das Problem: {lösung}")
        combined = list(zip(feldernum, values))
        combined.sort()
        feldernum_sorted, values_sorted = zip(*combined)
        feldernum_sorted = list(feldernum_sorted)
        values_sorted = list(values_sorted)
        for j in range(40):
            values_sorted[j] = values_sorted[j]/n*1000//1/10 #verbessern
        if plotten == True:
            fig, ax = plt.subplots() #was macht das 
        
            for i in range(11):
                rectleft = patches.Rectangle((0.16, 0.08*(i+1)), 0.06, 0.08, edgecolor='k', facecolor='white', lw=1.3)
                plt.text(y=.102+(0.08*i), x=.168, s=f'{values_sorted[i]}', fontsize=10, color='darkslategrey')
                ax.add_patch(rectleft)
            for j in range(11):
                rectright = patches.Rectangle((0.76, 0.08*(j+1)), 0.06, 0.08, edgecolor='k', facecolor='white', lw=1.3)
                plt.text(x=0.768, y=0.902-(0.08*(j)), s=f'{values_sorted[j+20]}', fontsize=10, color='darkslategrey')
                ax.add_patch(rectright)
            for k in range(9):
                rectbot = patches.Rectangle((0.22+(0.06*k), 0.08), 0.06, 0.08, edgecolor='k', facecolor='white', lw=1.3)
                plt.text(x=0.708-(0.06*k), y=0.102, s=f'{values_sorted[k+31]}', fontsize=10, color='darkslategrey')
                ax.add_patch(rectbot)
            for m in range(9):
                recttop = patches.Rectangle((0.22+(0.06*m), 0.88), 0.06, 0.08, edgecolor='k', facecolor='white', lw=1.3)
                plt.text(x=0.228+(0.06*m), y=0.902, s=f'{values_sorted[m+11]}', fontsize=10, color='darkslategrey')
                ax.add_patch(recttop)
                
            plt.text(.05, .1, 'Start', fontsize=10, color='k')
            plt.text(0, .91, 'Gefängnis', fontsize=10, color='k')
            plt.text(.38, .5, 'Zahlen in %', fontsize=12, color='k')

            # Achsen ausblenden
            ax.axis('off')

            # Anzeigen der Grafik
            plt.show()
        
        
        
test2 = Monopoly()
test2.fun()



