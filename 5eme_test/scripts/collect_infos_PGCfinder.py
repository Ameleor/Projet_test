import os
import pandas as pd
import sys

genome = sys.argv[1]

data_genome = "data/genomes_unzip/" + genome + "/"
results_genome = 'results/genomes/' + genome + '/PGCfinder/'

try:
    best_solution = pd.read_csv(results_genome + 'best_solution.tsv', sep='\t', comment='#')
    best_solution_summary = pd.read_csv(results_genome + 'best_solution_summary.tsv', sep='\t', comment='#', index_col=0)
    genome_gff = pd.read_csv(data_genome + genome + "_protein_gff.tsv", sep='\t')

    nbr_genes_hit = best_solution.shape[0]

    nbr_PGC = best_solution_summary.iloc[0, 0]

    genes_place = pd.DataFrame(best_solution.iloc[:, 1])
    genes_place.columns = ['prot_id_unique']

    # Merge the DataFrames and add suffixes to the overlapping columns
    replicon_type = genes_place.merge(genome_gff[['prot_id_unique', 'replicon_type']], how='left', on='prot_id_unique')
    replicons_unique = replicon_type['replicon_type'].unique()

    replicons_diff = ""
    for replicon in replicons_unique:
        if replicons_diff:
            replicons_diff += "/" + replicon
        else:
            replicons_diff = replicon

    # We're getting back the name of the genome to merge with the list
    genome_split = genome.split('_')
    genome_name = "_".join(genome_split[:2])

    to_merge_data = (genome_name + ',' + str(nbr_PGC) + ',' + str(nbr_genes_hit) + ',' + replicons_diff)

    print(to_merge_data)

except pd.errors.EmptyDataError:
    pass
