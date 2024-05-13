# The goal of this scripts is to retrive the gene from the genome corresponding to the PGC gene hit
import pandas as pd
import sys
from Bio import SeqIO

try:
    # Use two argument to be launch: {genome} {gene}
    genome = sys.argv[1]
    gene_path = sys.argv[2]

    # Extracting the gene name from the gene path
    gene = gene_path.split('/')[2].split('.')[0]

    # Read files with pandas
    hit_PGC = pd.read_csv('results/genomes/'+genome+'/PGCfinder/best_solution.tsv', sep='\t', comment='#')
    record_dict = SeqIO.to_dict(SeqIO.parse('data/genomes_unzip/'+genome+'/'+genome+'_protein.faa', "fasta"))

    # Get the the name of the gene hit from the genome
    column_git_gene = hit_PGC.iloc[:, 1:3]
    hit_PGC_gene = column_git_gene[column_git_gene["gene_name"].str.contains(gene)]
    if not hit_PGC_gene.empty:
        hit_gene = hit_PGC_gene.iloc[0,0]

        # Retrieve the fasta corresponding to the hit
        record_hit = record_dict[hit_gene].format("fasta")

        print(record_hit)

        # Write the result to a file
        #with open('results/fasta/' + gene + '.faa', 'a') as f:
        #    f.write(record_hit)

except pd.errors.EmptyDataError:
    pass