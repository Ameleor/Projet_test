import pandas as pd

# Récupération de l'output de silix possédant tous les différents numéros de gènes
df_silix = pd.read_csv("results/lists_PGC/output_silix_fullname_v1.csv")
df_taxonomy = pd.read_csv("results/lists_PGC/list_organisms_merged_PGC.csv")

# Filtrer les lignes où 'hit_gene' n'est pas NaN
df_silix_clean = df_silix[df_silix["hit_gene"].notna()]

# Sélectionner les colonnes d'intérêt dans df_taxonomy
df_taxonomy_clean = df_taxonomy[["Assembly", "#Organism Name", "class", "order", "family", "genus", "species", "Phototrophic group", "PGC replicon type"]]

# Modifier la colonne pour merge
df_silix_clean['genome'] = df_silix_clean['genome'].str.replace('GCF', 'GCA')

# Fusionner les DataFrames sur les colonnes "genome" et "Assembly"
df_merged = df_silix_clean.merge(df_taxonomy_clean, left_on="genome", right_on="Assembly")

# Obtenir une liste ordonnée de 'prot_id_unique' et 'hit_gene' pour chaque génome
genome_info_dict = {}
for genome, group in df_merged.groupby("genome"):
    sorted_group = group.sort_values("prot_id_unique")
    hit_gene_list = list(sorted_group["hit_gene"])
    genome_info_dict[genome] = hit_gene_list

# Pour chaque génome, afficher la liste ordonnée des 'hit_gene' en paires successives
for genome, hit_gene_list in genome_info_dict.items():
    pairs = [f"{hit_gene_list[i]}-{hit_gene_list[i+1]}" for i in range(len(hit_gene_list) - 1)]
    print(f"Genomes: {genome}, Pairs of hit_gene: {pairs}")
