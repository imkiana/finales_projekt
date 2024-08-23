# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:33:34 2024

@author: Kiana Heuser
"""

#Problem 340: Crazy Function 
class CrazyFunction:
    def __init__(self, a=50, b=2000, c=40):
        self.a = a
        self.b = b
        self.c = c

    def Function(self, n):
        '''Basisfunktion der Crazy Function'''
        if n > self.b:
            return n - self.c
        else:
            return self.Function(self.a + self.Function(self.a + self.Function(self.a + self.Function(self.a + n))))

    def S(self):
        '''Summiert die Basisfunktion von n=0 bis b'''
        ausgabe = 0
        for i in range(0, self.b):
            ausgabe += self.Function(i)
        return(ausgabe)


#test3 = CrazyFunction(21**7, 7**21, 12**7) RecursionError: maximum recursion depth exceeded
test3 = CrazyFunction()
test3.S()

#ich wüsste nicht wie ich 3 Dimensionen an Variation darstellen soll. 
