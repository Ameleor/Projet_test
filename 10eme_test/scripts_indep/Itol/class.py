import pandas as pd
import sys

list = pd.read_csv("results/lists_PGC/list_family_for_species_tree.csv")

import pandas as pd

# Boucle à travers chaque ligne du DataFrame
for index, row in list.iterrows():
    col0_value = row[0]
    col1_value = row[17]
    
    if col1_value == 'Alphaproteobacteria':
        print(f"{col0_value},#0000FF,Alphaproteobacteria")
    elif col1_value == 'Betaproteobacteria':
        print(f"{col0_value},#00FF00,Betaproteobacteria")
    elif col1_value == 'Gammaproteobacteria':
        print(f"{col0_value},#FFFF00,Gammaproteobacteria")
