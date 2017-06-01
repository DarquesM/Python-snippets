# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:43:36 2016

@author: m.darques

Code pour tester différentes manières de réaliser des fits
On arrive au même résultat qu'avec le code least squares
Plus pratique pour ce genre de fonctions, on n'a pas besoin de donnerla forme de la solution pour les essais
"""
import numpy as np 
import matplotlib.pyplot as plt
#from scipy import optimize 
from numpy.polynomial import Polynomial

import numpy.polynomial.polynomial as poly

x=np.array([1.0,2.5,3.5,4.0,1.1,1.8,2.2,3.7])
y=np.array([6.008,15.722,27.130,33.772,5.257,9.549,11.098,28.828])

#On peut utiliser directement la fonction de fit polynomial
#x,y et le degré du polynome
p = Polynomial.fit(x,y,8)
print(p)
#Attention ce fit utilise des valeurs shiftées et scalées (stabilité numérique)
#Pour afficher les coefs "normaux", on fait comme suit :
print(p.convert(domain=(-1,1)))
#Plus directement on pouvait écrire : p = Polynomial.fit(x,y,1,domain=(-1,1))

#Autre manière de procéder
#plt.figure(1)
coefs, r = poly.polyfit(x,y,2,full=True)
#RSS
print("Coefs:", coefs,"r:",r)
RSS = np.sum((np.polyval(np.polyfit(x, y, 1), x) - y)**2)
print("RSS=", RSS)
ffit = poly.polyval(x,coefs)
#plt.plot(x,y,'o')
#plt.plot(x,ffit)
#plt.plot(x,ffit-y,'*')

plt.figure(2)
plt.plot(*p.linspace())
plt.plot(x,y,'o')
plt.show()
#plt.figure
#plt.plot(x,y,'o')
#plt.plot(xx1,yy1)

#np.polynomial.polynomial.polyfit returns coefficients [A, B, C] to A + Bx + Cx^2 + ..., while np.polyfit returns: ... + Ax^2 + Bx + C. 
