#Opérations basiques sur les dictionnaires
#Toujours défini entre accolades

d = {'Mike' : 38, 'Vincent' : 0}
print("Est-ce que 'Mike' est dans le dictionnaire?",'Mike' in d)      #Mike est bien dans le dicionnaire donc "True"
print('Mike' not in d)  #Mike n'est pas dans d donc "False"
print('La longueur du dictionnaire est:',len(d))
print("L'âge de Mike est",d['Mike'])
print("L'ensemble des clefs est:",d.keys())
print("Les valeurs sont:",d.values())
#Pour avoir la liste des tuples clef/valeurs
print("Les tuples clefs/valeurs sont:",d.items())

#Pour afficher les items : i parcours les clefs, j les éléments associés
for i,j in d.items(): print(i,j)
