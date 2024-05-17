import pandas as pd

# Charger le fichier CSV
list_full = pd.read_csv('../data/lists/list_modif.csv', index_col=0)

# Créer un nouveau DataFrame pour stocker les lignes correspondant à "Pseudomonadota" dans la colonne 'Organism Groups'
list_Pseudomonadota = list_full[list_full['phylum'].str.contains("Pseudomonadota")]

# This file contain: 20092 rows and 15 columns
list_Pseudomonadota.to_csv('../data/list_Pseudomonadota_modif.csv')

print(list_Pseudomonadota)
