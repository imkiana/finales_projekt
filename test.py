# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:40:49 2024

@author: Kiana Heuser
"""

#Problem 2: gerade Fib nummern
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Fibonacci:
    def __init__(self, maximal=4_000_000, startzahl=1):
        self.maximal = maximal
        self.startzahl = startzahl
    
    def fun(self, plotten = True):
        fi = round((1.6180339887**(self.startzahl+1)-(1.6180339887)**-(self.startzahl+1))/sqrt(5))
        ausgabe = list()
        fibefore = round((1.6180339887**(self.startzahl)-(1.6180339887)**-(self.startzahl))/sqrt(5))
        while fi < self.maximal:
            if fi % 2 == 0:
                ausgabe.append(1)
            else:
                ausgabe.append(0) 
            buffer = fi
            fi = fi + fibefore
            fibefore = buffer
        print(f"Insgesamt gab es {sum(ausgabe)} gerade Zahlen, bis zur Zahl {fibefore}.")
        print(np.cumsum(ausgabe))
        if plotten == True:
            plt.hist(np.cumsum(ausgabe), bins=len(ausgabe), color=['blue'])
            plt.xlabel("Index ab Startzahl")
            plt.ylabel("Kumulierte Anzahl gerader Zahlen")
            plt.title("Verteilung der geraden Fibonacci-Zahlen")
            plt.show()
            
test = Fibonacci()
#test.fun()

#Problem 84: Monopoly Odds
#lösungsversuch 1 simulation
import random as rdm #----

class Monopoly:
    def __init__(self, dice_dn=4):
        self.dice_dn = dice_dn
        
        
    def fun(self):
        feld = 1
        ausgabe = list()
        for i in range(1, 10000):
            feld = (feld + np.random.randint(1,7) - 1) % 40 + 1
            if feld in [3,18,34]: #CC
                karte = rdm.choice([1,11])
                feld = karte
            if feld in [8,23,37]: #CH  #"Next" vertanden als "next clockwise" 
                karte = rdm.choice([1,11,12,25,40,6,feld//10*10+6,feld//10*10+6,"U",feld-3])
                if karte == "U":
                    if feld//10 < 13:
                        feld = 13
                    else:
                        feld = 29
            ausgabe.append(feld)
            #print(feld)
test2 = Monopoly()
test2.fun()






# Anzahl der Rechtecke
anzahl_rechtecke = 40

# Größe des Monopolyfelds
feldgroesse = 10

# Erstelle ein neues Diagramm
fig, ax = plt.subplots()

# Schleife zum Zeichnen der Rechtecke
for i in range(anzahl_rechtecke):
    x = i % feldgroesse
    y = i // feldgroesse
    rechteck = plt.Rectangle((x, y), 1, 1, color='blue', fill=False)
    ax.add_patch(rechteck)

# Achsenbeschriftungen und Titel
plt.axis('off')
#plt.title("Monopolyfeld")

# Zeige das Diagramm an
plt.show()