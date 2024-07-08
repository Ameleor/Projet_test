import pandas as pd
import sys

list = pd.read_csv("results/lists_PGC/list_family_for_species_tree.csv")

# Dictionnaire de familles avec couleurs associées
familles_couleurs = {
    'Hyphomicrobiales': '#FF0000',       # Rouge
    'Rhodospirillales': '#00FF00',       # Vert
    'Enterobacterales': '#0000FF',       # Bleu
    'Alteromonadales': '#FFFF00',        # Jaune
    'Oceanospirillales': '#FF00FF',      # Magenta
    'Burkholderiales': '#00FFFF',        # Cyan
    'Cellvibrionales': '#800000',        # Marron
    'Nitrosomonadales': '#808000',       # Olive
    'Chromatiales': '#800080',           # Pourpre
    'Neisseriales': '#008000',           # Vert foncé
    'Sphingomonadales': '#000080',       # Bleu marine
    'Thiotrichales': '#808080',          # Gris
    'Rickettsiales': '#C0C0C0',          # Argent
    'Xanthomonadales': '#FFA500',        # Orange
    'Holosporales': '#A52A2A',           # Brun
    'Rhodocyclales': '#8A2BE2',          # Bleu violet
    'Pseudomonadales': '#5F9EA0',        # Bleu cadet
    'Rhodobacterales': '#D2691E',        # Chocolat
    'Aeromonadales': '#FF7F50',          # Corail
    'Legionellales': '#6495ED',          # Bleu clair
    'Nevskiales': '#DC143C',             # Carmin
    'Cardiobacteriales': '#00FFFF',      # Aqua
    'Hyphomonadales': '#00008B',         # Bleu foncé
    'Ferrovales': '#008B8B',             # Cyan foncé
    'Orbales': '#B8860B',                # Or
    'Maricaulales': '#A9A9A9',           # Gris foncé
    'Acidiferrobacterales': '#006400',   # Vert foncé
    'Acidithiobacillales': '#BDB76B',    # Kaki foncé
    'Kordiimonadales': '#8B008B',        # Violet foncé
    'Kangiellales': '#556B2F',           # Olive foncé
    'Emcibacterales': '#FF8C00',         # Orange foncé
    'Moraxellales': '#9932CC',           # Violet foncé
    'Caulobacterales': '#8B0000',        # Rouge foncé
    'Pasteurellales': '#E9967A',         # Saumon foncé
    'Candidatus Pelagibacterales': '#8FBC8F', # Vert mer foncé
    'Methylococcales': '#483D8B',        # Bleu ardoise foncé
    'Parvularculales': '#2F4F4F',        # Gris ardoise foncé
    'Mariprofundales': '#00CED1',        # Turquoise foncé
    'Sneathiellales': '#9400D3',         # Violet foncé
    'Salinisphaerales': '#FF1493',       # Rose foncé
    'Immundisolibacterales': '#00BFFF',  # Bleu ciel
    'Magnetococcales': '#1E90FF',        # Bleu roi
    'Candidatus Comchoanobacterales': '#B22222', # Rouge feu
    'Casimicrobiaceae': '#FFD700'        # Or 
}

# Boucle à travers chaque ligne du DataFrame
for index, row in list.iterrows():
    col0_value = row[0]
    col1_value = row[17]
    
    # Vérification de la valeur et conversion en chaîne
    if pd.isna(col1_value):
        famille = 'Unknown'
    else:
        famille = ''.join([i for i in str(col1_value) if not i.isdigit()]).strip()
    
    # Vérification si la famille est dans le dictionnaire
    if famille in familles_couleurs:
        couleur = familles_couleurs[famille]
        print(f"{col0_value},{couleur},{famille}")
    else:
        # Si la famille n'est pas trouvée, on peut gérer cela ici (par exemple, utiliser une couleur par défaut)
        print(f"{col0_value},#FFFFFF,Unknown")
