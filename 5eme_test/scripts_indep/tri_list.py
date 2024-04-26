import pandas as pd

# Charger le fichier CSV
list_full = pd.read_csv('../data/list_modif.csv', index_col=0)

# Créer une nouvelle DataFrame pour stocker les lignes correspondant à "Pseudomonadota" dans la colonne 'Organism Groups'
list_Pseudomonadota = list_full[list_full['Organism Groups'].str.contains("Pseudomonadota")]

# This file contain: 20092 rows and 15 columns
#list_Pseudomonadota.to_csv('../data/list_Pseudomonadota_modif.csv')

print(list_Pseudomonadota)
