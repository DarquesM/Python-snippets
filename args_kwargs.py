"""
Understanding *args and **kwargs
"""


def nom_prenom(nom, prenom):
    return(nom, prenom)


def mult(*args):
    ''' multiplies any number of values '''
    result = 1
    for _ in args:
        result *= _
    return result

# Dict to be passed to nom_prenom()
NAME_OPTIONS = dict(nom="Mike", prenom="Dark")

print(mult(2, 3, 2))
print(nom_prenom(**NAME_OPTIONS))
