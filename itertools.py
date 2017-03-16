#This snippet is used to create list of variables for scientific computing
#Instead of nesting for loops it is used to create a proper list to be fed to a function

#Example below
import itertools

A = [1,2,3]
B = [1,2,3]
pairs = itertools.product(A,B) # is <itertools.product at 0x4383ab0>

#To visualise the list : 
print list(pairs)
# [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)] 
#Yay I can cycle through all values of my parameters

#Example function :
def func(a,b):
    print a,b
    
[func(a,b) for a,b in pairs]
