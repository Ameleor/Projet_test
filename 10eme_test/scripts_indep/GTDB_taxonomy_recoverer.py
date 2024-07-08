import pandas as pd

# Lire les fichiers CSV
taxonomy_GTDB = pd.read_csv("data/GTDB/bac120_taxonomy_r220.tsv", sep="\t", header=None)
list_genomes = pd.read_csv("results/lists_PGC/list_family_for_species_tree.csv")

# Renommer les colonnes
taxonomy_GTDB = taxonomy_GTDB.rename(columns={taxonomy_GTDB.columns[0]: 'Assembly', taxonomy_GTDB.columns[1]: 'Taxonomy'})

# Enlever les trois premiers caractères de la colonne "Assembly"
taxonomy_GTDB['Assembly'] = taxonomy_GTDB['Assembly'].str[3:]

# Séparer la colonne "Taxonomy" en plusieurs colonnes
taxonomy = taxonomy_GTDB["Taxonomy"].str.split(";", expand=True)
taxonomy.columns = ["Superkingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]

# Joindre les nouvelles colonnes au DataFrame original
taxonomy_GTDB = taxonomy_GTDB.drop(columns=['Taxonomy']).join(taxonomy)

# Enlever les trois premiers caractères des nouvelles colonnes
for col in ["Superkingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species"]:
    taxonomy_GTDB[col] = taxonomy_GTDB[col].str[3:]

# Remplacer les 
taxonomy_GTDB['Assembly'] = taxonomy_GTDB['Assembly'].str.replace('GCF', 'GCA')

list_genomes = pd.DataFrame(list_genomes.iloc[:,0])
list_genomes = list_genomes.rename(columns={list_genomes.columns[0]: "Assembly"})

# Séparer les valeurs de list_genomes par "_" et récupérer les deux premières parties
split_genomes = list_genomes["Assembly"].str.split("_", n=2, expand=True)
list_genomes_parse = split_genomes[0] + "_" + split_genomes[1]
list_genomes_parse.name = "Parsed Assembly"

list_genomes = list_genomes.rename(columns={list_genomes.columns[0]: "Assembly"}).join(list_genomes_parse)

merged_df = pd.merge(list_genomes, taxonomy_GTDB, left_on='Parsed Assembly', right_on='Assembly', how="left")

merged_df = merged_df.drop(columns=['Assembly_y', 'Parsed Assembly']).rename(columns={'Assembly_x': 'Assembly'})

merged_df.to_csv('results/lists_PGC/merged_with_taxonomy_GTDB.csv', index=False)