import pandas as pd
import sys

list = pd.read_csv("results/lists/merged_with_taxonomy_GTDB.csv")

# Dictionnaire des classes avec couleurs associées
classe_couleurs = {
    'Alphaproteobacteria': '#FF0000',    # Rouge
    'Betaproteobacteria': '#00FF00',     # Vert
    'Gammaproteobacteria': '#0000FF',    # Bleu
}

Phototrophs = {
    'Phototroph': '#FF0000',    # Rouge
}

# Dictionnaire des ordres avec couleurs associées
ordres_couleurs = {
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
    'NouvelleFamille': '#FFD700'         # Or
}

ordres_couleurs_bis= {
    'Acetobacterales': '#aabbcc',       # Exemple de nouvelle couleur
    'Acidiferrobacterales': '#006400',  # Conservé
    'Acidithiobacillales': '#BDB76B',   # Conservé
    'Arenicellales': '#ddeeff',         # Exemple de nouvelle couleur
    'Azospirillales': '#112233',        # Exemple de nouvelle couleur
    'Beggiatoales': '#334455',          # Exemple de nouvelle couleur
    'Burkholderiales': '#00FFFF',       # Conservé
    'Caedimonadales': '#556677',        # Exemple de nouvelle couleur
    'Cardiobacteriales': '#00FFFF',     # Conservé
    'Caulobacterales': '#8B0000',       # Conservé
    'Chromatiales': '#800080',          # Conservé
    'Comchoanobacterales': '#889900',   # Exemple de nouvelle couleur
    'Competibacterales': '#aaccdd',     # Exemple de nouvelle couleur
    'Coxiellales': '#bbccdd',           # Exemple de nouvelle couleur
    'Diplorickettsiales': '#ccddee',    # Exemple de nouvelle couleur
    'Dongiales': '#ddeeff',             # Exemple de nouvelle couleur
    'Ectothiorhodospirales': '#eeddcc', # Exemple de nouvelle couleur
    'Enterobacterales': '#0000FF',      # Conservé
    'Ferrovibrionales': '#ffeedd',      # Exemple de nouvelle couleur
    'Francisellales': '#ffaa00',        # Exemple de nouvelle couleur
    'Granulosicoccales': '#aabb22',     # Exemple de nouvelle couleur
    'Halothiobacillales': '#22aabb',    # Exemple de nouvelle couleur
    'Holosporales': '#A52A2A',          # Conservé
    'Immundisolibacterales': '#00BFFF', # Conservé
    'Legionellales': '#6495ED',         # Conservé
    'Magnetococcales': '#1E90FF',       # Conservé
    'Mariprofundales': '#00CED1',       # Conservé
    'Methylococcales': '#483D8B',       # Conservé
    'Micavibrionales': '#aa33ff',       # Exemple de nouvelle couleur
    'Micropepsales': '#cc33aa',         # Exemple de nouvelle couleur
    'Minwuiales': '#ee99aa',            # Exemple de nouvelle couleur
    'Nevskiales': '#DC143C',            # Conservé
    'Nitrococcales': '#11aa22',         # Exemple de nouvelle couleur
    'Nitrosococcales': '#3344bb',       # Exemple de nouvelle couleur
    'Paracaedibacterales': '#55aa33',   # Exemple de nouvelle couleur
    'Parvibaculales': '#77cc99',        # Exemple de nouvelle couleur
    'Pelagibacterales': '#88ddbb',      # Exemple de nouvelle couleur
    'Piscirickettsiales': '#99aacc',    # Exemple de nouvelle couleur
    'Pseudomonadales': '#5F9EA0',       # Conservé
    'Puniceispirillales': '#aa3322',    # Exemple de nouvelle couleur
    'Reyranellales': '#bbaa22',         # Exemple de nouvelle couleur
    'Rhizobiales': '#ccbbaa',           # Exemple de nouvelle couleur
    'Rhodobacterales': '#D2691E',       # Conservé
    'Rhodospirillales': '#00FF00',      # Conservé
    'Rickettsiales': '#C0C0C0',         # Conservé
    'Sneathiellales': '#9400D3',        # Conservé
    'Sphingomonadales': '#000080',      # Conservé
    'Steroidobacterales': '#ccddaa',    # Exemple de nouvelle couleur
    'Thalassobaculales': '#22aabb',     # Exemple de nouvelle couleur
    'Thiohalobacterales': '#aa55cc',    # Exemple de nouvelle couleur
    'Thiomicrospirales': '#99aacc',     # Exemple de nouvelle couleur
    'Thiotrichales': '#808080',         # Conservé
    'Tistrellales': '#ccaa99',          # Exemple de nouvelle couleur
    'Woeseiales': '#66bbcc',            # Exemple de nouvelle couleur
    'Xanthomonadales': '#FFA500'        # Conservé
}



# Boucle à travers chaque ligne du DataFrame
for index, row in list.iterrows():
    # Colonne à varier en fonction des informations que l'on veut récupérer (ordre/classe/famille)
    col0_value = row[0] # Colonne pour les GCF
    col1_value = row[4] # Colonne de ce que l'on vérifie
    
    # Vérification de la valeur et conversion en chaîne
    if pd.isna(col1_value):
        famille = 'Unknown'
    else:
        famille = ''.join([i for i in str(col1_value) if not i.isdigit()]).strip()
    
    # Vérification si la famille est dans le dictionnaire
    # A modifier si on veut ordre/classe
    if famille in ordres_couleurs_bis:
        # A modifier sir on veut ordre/classe
        couleur = ordres_couleurs_bis[famille]
        print(f"{col0_value},{couleur},{famille}")
    else:
        # Si la famille n'est pas trouvée, on peut gérer cela ici (par exemple, utiliser une couleur par défaut)
        print(f"{col0_value},#FFFFFF,Unknown")
