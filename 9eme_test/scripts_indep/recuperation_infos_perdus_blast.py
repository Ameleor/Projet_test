import pandas as pd
from Bio import SeqIO

# This script is useless because the way to do things is wrong
# To have information that is missing I used to think that i had to change BEFORE the blast but i just have to modify the output with Silix
# By modifying the silix output it's easier and it's working perfectly

# Read in the data
df_blast_all = pd.read_csv("results/fasta_PGC/blast/blastall.out", sep="\t", header=None)
record_dict = SeqIO.to_dict(SeqIO.parse('results/fasta_PGC/all_fasta_gathered.faa', "fasta"))

# Create a list of full names
list_full_names = [record_dict[record].description for record in record_dict]

# Create a DataFrame from the list of full names
record_df = pd.DataFrame(list_full_names, columns=["Name"])

# Create a mapping dictionary from partial names to full names
# Assuming the partial name is the first part of the full name split by space
mapping_dict = {name.split()[0]: name for name in record_df['Name']}

# Function to replace partial name with full name using the mapping dictionary
def replace_partial_name(partial_name):
    return mapping_dict.get(partial_name, partial_name)

# Replace partial names in columns 0 and 1
df_blast_all[0] = df_blast_all[0].apply(replace_partial_name)
df_blast_all[1] = df_blast_all[1].apply(replace_partial_name)

df_blast_all[0] = df_blast_all[0].str.replace(' ', '_')
df_blast_all[1] = df_blast_all[1].str.replace(' ', '_')

# Save CSV
df_blast_all.to_csv('results/fasta_PGC/blast/blast_all_fullname.out', sep="\t", header=None)

