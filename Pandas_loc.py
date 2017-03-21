#Testing which option is faster to replace values in a pandas dataframe

import pandas as pd
import timeit

data = pd.read_csv("./Data Sets/amazon_baby.csv") #File is a dataframe 183531*5 size

def loc():
    data.loc[data.rating < 3,"Eval"] = 0

def pasloc():
    data["test"] = data["rating"].apply(lambda rating: 0 if rating <3 else 1)
    
timeit.timeit(loc, number=100)
# Returns : 0.2 s

timeit.timeit(pasloc,number=100)
# Returns : 5.98 s

# DataFrame.loc should be used for better performance
