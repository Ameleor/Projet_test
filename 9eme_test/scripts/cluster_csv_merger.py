import pandas as pd
import sys

# Input file path provided via command line arguments
output_silix = sys.argv[1]

# Read the silix output file
df_silix = pd.read_csv(output_silix, sep='\t', header=None)
df_silix.columns = ["Family", "prot_id_unique"]

# Dictionary to store genome information
genome_dict = {}

# Populate the genome_dict with genome as keys and list of gene numbers as values
for i in df_silix.iloc[:, 1]:
    genome = i.rsplit('_', 1)
    key, value = genome
    # Condition to have a list and not just one itteration for each key
    if key in genome_dict:
        genome_dict[key].append(value)
    else:
        genome_dict[key] = [value]

# Initialize an empty DataFrame for collecting all merged information
all_infos = pd.DataFrame(columns=["genome", "seq", "prot_id", "prot_id_unique", "beginning", "end", "strand", "gene", "product", "refseq_id", "replicon_type", "hit_gene"])

# Loop through each genome and its associated gene numbers
for genome, values in genome_dict.items():
    # File paths for GFF and HIT files
    dir_gff = f"data/genomes_unzip_PGC/{genome}/{genome}_protein_gff.tsv"
    dir_hit = f"results/genomes_PGC/{genome}/PGCfinder/best_solution.tsv"
    dir_tax = f"results/genomes_PGC"
    
    # Read the GFF and HIT files
    df_gff = pd.read_csv(dir_gff, sep='\t')
    df_hit = pd.read_csv(dir_hit, sep='\t', comment='#')
    
    # Loop through each gene number for the current genome
    for value in values:
        gene = f"{genome}_{value}"
        
        # Filter the information for the current gene
        gff_infos = df_gff[df_gff["prot_id_unique"] == gene]
        hit_infos = df_hit[df_hit["hit_id"] == gene][["hit_id", "gene_name"]]
        
        # Rename columns for consistency
        hit_infos = hit_infos.rename(columns={"hit_id": "prot_id_unique", "gene_name": "hit_gene"})
        
        # Merge GFF and HIT information based on prot_id_unique
        merge_infos = gff_infos.merge(hit_infos, how="left", on="prot_id_unique")
        
        # Append the merged information to the all_infos DataFrame
        all_infos = pd.concat([all_infos, merge_infos])


# Merge using the column "prot_id_unique" that I have previously named for the silix output
df_silix_full = df_silix.merge(all_infos, how="left", on="prot_id_unique")

df_silix_full.to_csv("results/fasta_PGC/blast/output_silix_fullname_v1.csv", index=False)
