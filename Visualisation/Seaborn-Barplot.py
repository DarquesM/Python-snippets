"""
Exemple de barplots avec Seaborn, avec une solution pour que la palette de couleur soit proportionnelle à la hauteur des barres
"""

import pandas as pd
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt

# Données = taux de participation aux élections législatives sous la Veme république
data = pd.DataFrame()
data['Année'] = [1958, 1962, 1967, 1968, 1973, 1978, 1981, 1986, 1988, 1993, 1997, 2002, 2007, 2012, 2017]
data['Participation'] = [77.1, 68.7, 80.9, 80, 81.2, 82.8, 70.7, 78.5, 65.7, 68.9, 67.9, 64.4, 60.4, 57.2, 48.7]

# Ci dessous, code pour avoir une palette proportionnelle à la hauteur
# La palette doit contenir autant de couleurs que d'éléments dans data.participation
pal = sns.color_palette("Greens_d", len(data))  #https://seaborn.pydata.org/generated/seaborn.color_palette.html
# data.Participation doit être un array numpy pour appliquer argsort deux fois (1er pour obtenir l'odre, 2nd pour classer)
rank = np.array(data["Participation"]).argsort().argsort()   # http://stackoverflow.com/a/6266510/1628638

sns.set_context('poster')
plt.ylabel("Participation")
sns.barplot(x=data['Année'], y=data['Participation']) #Pour utiliser la palette classique
sns.barplot(x="Année", y="Participation", data=data, palette=np.array(pal[::-1])[rank])
plt.show()
