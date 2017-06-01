# -*- coding: utf-8 -*-
"""
Created on Wed May 10 14:21:54 2017

@author: Michael
"""
#%%
#Modules
import math
from matplotlib import pyplot as plt
#import scipy as sp
#from scipy import signal
from scipy import special 
import numpy as np
import time
import pandas as pd
import itertools


#Constants
gyro=2.0035
muB=9.2741*1e-24
h_planck=6.6262*1e-34
mu0=4*math.pi*1e-7
gamma = gyro*muB/h_planck*2*math.pi
k=1.3806e-23
kT=k*293
Ks=0.42e-3   #surface anisotropy (J/m2)
Aex=1e-11   #Exchange constant (J/m)
DMI=2e-3    #DMI parameter

#Sat Mag
#Bs = mu0*(1.2e6)
#Bs = mu0*(0.95e6)
#Ms=Bs/mu0
#Kd=Bs**2/2/mu0
#SatDemagEnergy=mu0*Ms**2/2  #Saturated Demag Energy (J/m3)
t=0.47e-9                    #Film thickness (m)
#gammaNeel=4*math.sqrt(Aex*(Ks/t-Kd))-math.pi*DMI #DW energy
#lc = gammaNeel/2/Kd         #Material Characteristic length
#NormEnergy=SatDemagEnergy*math.pi*t**3

#Applied Field
Ba=0.000005
Ha=Ba/mu0
start_diam, stop_diam, step_diam = 1e-10, 1000e-6, 1e-10 #Diametre
diametres = np.arange(start_diam,stop_diam,step_diam)
appField = (np.arange(0.00010,0.00095,0.000001)/mu0) #Ha = Ba/mu0
#bb = np.arange(1,4,1)
#energy2 = []
energy2 = np.zeros((5,3,500))
#t_init = time.clock()
range_Ms = np.arange(0.9e6,0.95e6,1e4)
range_Ks = np.arange(0.42e-3,0.45e-3,0.01e-3)

Ms = 0.9e6
Ks = 0.42e-3

diam = 1e-9
Kd=mu0*Ms**2/2
gammaNeel=4*np.sqrt(Aex*(Ks/t-Kd))-np.pi*DMI #DW energy
    
cte = -mu0*Ms**2*np.pi #Tout ce qui est dans la boucle et peut être calculé séparemment doit être sorti 
cte2 = mu0*2*Ms*Ha
cte3 = -2/3/math.pi
pii = np.pi

#%%
'''
Je lui passe un iterable, donc un seul paramètre en entrée
param[0] = diamètre
param[1] = Ba
'''
#Version pour faire varier 2 paramètres
def calc_total_energy_m(param): 
#    zeeman_energy = mu0*2*Ms*param[1]*((np.pi*param[0]**2/4)*t)
    zeeman_energy = cte2*param[1]*((pii*param[0]**2/4)*t)
    wall_energy = gammaNeel*(pii*param[0])*t
    d=param[0]/t
    u=np.sqrt((d)**2/(1+d**2))
    cc= u**2
    E = special.ellipe(cc) 
    K = special.ellipk(cc) 
#    Id=-2/3/math.pi*d*(d**2+(1-d**2)*E/u-K/u)
#    demag_energy = -mu0*Ms**2*np.pi*t**3*Id
    Id=cte3*d*(d**2+(1-d**2)*E/u-K/u)
    demag_energy = cte*t**3*Id
    total_energy = zeeman_energy+demag_energy+wall_energy
    return (total_energy,zeeman_energy)

def calc_total_energy(diam): 
    zeeman_energy = cte2*((pii*diam**2/4)*t)
    wall_energy = gammaNeel*(pii*diam)*t
    d=diam/t
    u=np.sqrt((d)**2/(1+d**2))
    cc= u**2
    E = special.ellipe(cc) 
    K = special.ellipk(cc) 
    Id=cte3*d*(d**2+(1-d**2)*E/u-K/u)
    demag_energy = cte*t**3*Id
    total_energy = zeeman_energy+demag_energy+wall_energy
    return (total_energy,zeeman_energy)

#%%
''' *** POUR FAIRE VARIER JUSTE LE DIAMETRE *** '''


t_init = time.clock()
#test = diametres.reshape(-1,1)
#r1 = np.apply_along_axis(calc_total_energy,1,test) #18 seconds

#totalEnergy = []
#zeemanEnergy = []
#Essai de multiprocessing
#from joblib import Parallel, delayed
#import multiprocessing
#from joblib.pool import has_shareable_memory # 4 jobs : 257 / 16 jobs :
#num_cores = multiprocessing.cpu_count()
#
#Parallel(n_jobs=16,max_nbytes=1e6)(delayed(has_shareable_memory)(calc_total_energy(d)) for d in diametres)
#Fin multiprocessing

energyTot = calc_total_energy(diametres)

#
#for d in diametres:  #5 seconds
#    res1,res2 = calc_total_energy(d)
#    totalEnergy.append(res1)
#    zeemanEnergy.append(res2)
#timeit.timeit(lambda :calc_total_energy(diametres),number=10) #119

t_final = time.clock()
print("Temps total d'exécution : ",t_final-t_init) #31 secondes

plt.plot(diametres,energyTot[0])

#%%
#''' *** POUR FAIRE VARIER PLUSIEURS PARAMETRES A LA FOIS *** '''
#repeat = itertools.product(diametres,appField)
#t_init = time.clock()
#
#for rep in repeat:
#    res1,res2 = calc_total_energy_m(next(repeat))
#
#t_final = time.clock()
#print("Temps total d'exécution : ",t_final-t_init) #31 secondes
#calc_total_energy(diametres) #○Si on veut loop uniquement sur le diamètre


#timeit.timeit(lambda :calc_total_energy(diametres),number=10)

#%%
#''' *** TEST DE VITESSE *** '''
#t_init = time.clock()
#for i in np.arange(0,len(range_Ms),1): #1000 fois ---> 0.71 seconde 5000fois --> 0.32 secondes               
#    for j in np.arange(0,len(range_Ks),1):           
##      ene = np.apply_along_axis(calc_total_energy,0,b)  #Je balaye une seule valeur de Ms et sur le range de diam
#       ene,zee = calc_total_energy(diametres) #ene = energie totale, zee = energie zeeman
#       Ms += 1e4
#       Ks += 0.01e-3
#    energy2[i][j] = ene
#    
#t_final = time.clock()
#print("Temps total d'exécution : ",t_final-t_init)
#
#
##%%
#max_local = np.zeros(5)
#min_local = []
#
#for i in np.arange(0,5,1) :
#    idx_max = sp.signal.argrelextrema(energy2[i],np.greater) #Maximum local
#    idx_min = sp.signal.argrelextrema(energy2[i],np.less) #Minimum local
#    print(all(idx_max))
#    
#    if all(idx_max):
##        max_local.append(0)
#        max_local[i] = np.float(energy2[i][idx_max])
##         max_local[i] = 0
#    else:
#        max_local[i] = 0
##        max_local[i] = np.float(energy2[i][idx_max])
##        np.append(max_local,energy2[i][idx_max])
##        max_local.append(energy2[i][idx_max])
#
#    
##Pour tester la fonction on peut aussi faire import timeit puis timeit.timeit(calc_total_energy,number=100)
##%%
#range_x = np.arange(start_diam,stop_diam,step_diam)
##plt.plot(range_x,total_energy)
#plt.plot(energy2[0][2][:])
#
#results = pd.DataFrame()  #Création d'un tableau avec Pandas
#results['Energie totale'] = ene #Création des colonnes et assignation d'une variable
#results['Energie Zeeman'] = zee
#       
##%%
#''' *** Essai de création de vecteur de paramètres pour vectorisation avec numpy *** '''
#
#def somme(p):
#    return(p[0]+p[1])
#
#A = np.array([1,2,3])
#B = np.array([1,2,3])
#
#parametres = itertools.product(A,B)
#C = np.array(list(parametres))
#
#D = np.apply_along_axis(somme,1,C)
