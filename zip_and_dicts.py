'''
TRANSFORM
['orange', 'apple', 'orange', 'orange', 'apple', 'tomato']
INTO
[{'count': 1, 'flavor': 'tomato'},
 {'count': 2, 'flavor': 'apple'},
 {'count': 3, 'flavor': 'orange'}]
'''

import pandas as pd

# Create a DataFrame
df = pd.DataFrame()
df["Fruits"] = ['orange', 'apple', 'orange', 'orange', 'apple', 'tomato']

# Create a dictionnary from value counts
dico = df.Fruits.value_counts(ascending=True)

# Transform to the desired dictionnary shape
z = zip(dico.index, dico.values)
dic = [dict(flavor=a, count=b) for a,b in z]
