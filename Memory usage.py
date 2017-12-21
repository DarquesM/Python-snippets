# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

sys.getsizeof() will return the size of the object 
To get the size of the object and all included objects, use pympler
"""
import sys
from pympler.asizeof import asizeof

A = "a"
liste = []

print("Memory usage of a single char :{0}".format(asizeof(A)))
print("Memory usage of an empty list :{0}".format(asizeof(liste)))

for i in ["a","a","a","a","a","a","a","a","a","a","a","a"]:
    liste.append(i)
    print("Memory usage of a list containing {0} char: {1}".format\
          (len(liste), asizeof(liste)))
    print("The size of a list object is {0} bytes".format\
      (sys.getsizeof(liste)))
    
