# -*- coding: utf-8 -*-
"""
Created on Mon May  2 08:12:28 2016

@author: Michaël

Essais divers de compréhension de YIELD (generator)

"""

from matplotlib import pyplot as plt
import itertools

#%%
def addition(a):
    print(a[0]+a[1]+a[2])
    
#%%
A = [1,2,3]
B = [1,2,3]
C = [1,2,3]

repeat = itertools.product(A,B,C)
#print(list(repeat))
#%%
for truc in repeat:
    addition(next(repeat))



#%%
#Définition de mon generator 
def gensquare(N):
    for i in range(N):
        yield i**2      #Retourne le carré
        
a=gensquare(5)          #"a" est un generator, pas une variable. Si print(a) il ne retourne pas de valeur

"""Pour afficher les valeurs, je peux faire un next(a). A chaque fois, il itère dans
a"""

print(next(a))          #Retourne 0
print(next(a))          #Retourne 1
print(next(a))          #Retourne 4
print(next(a))          #Retourne 9
print(next(a))          #Retourne 16
try:
    print(next(a))
except:
    print("Erreur")     #Erreur, car je n'ai que 5 objets dans mon générateur


#%%

n = 2
d = 3

def visit(*indices):
    print(indices)
    
# Equivalent using itertools.product
for indices in itertools.product(*([range(n)] * d)):
    visit(*indices)
