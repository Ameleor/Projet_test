import sys
import os
import pandas as pd
from Bio import SeqIO

genome = sys.argv[1]

try:
    df_best_solution = pd.read_csv('results/genomes/' + genome + '/PGCfinder/best_solution.tsv', sep='\t', comment='#')
except pd.errors.EmptyDataError:
    sys.exit()

record_dict = SeqIO.to_dict(SeqIO.parse('data/genomes_unzip/' + genome + '/' + genome + '_protein.faa', "fasta"))

# Where we're going to stock our results
results = []

# Iterate on each value from the column
for values in df_best_solution['hit_id']:
    # Marges to take to gather the corresponding fastas. Equivalent to the one used by PGCfinder
    values = int(values.split("_")[-1])
    plage = list(range(values - 5, values + 6))
    results.extend(plage)

# Transformation to have a series with all the number we need
series_results = pd.Series(results)
results_clean = series_results.drop_duplicates().reset_index(drop=True)

# Way to print every fasta and gatherer them later in a bigger file
for num in results_clean:
    fasta_name = genome + "_" + str(num)
    if fasta_name in record_dict:
        fasta = record_dict[fasta_name].format("fasta")
        print(fasta, end='')

