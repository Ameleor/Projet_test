import pandas as pd

# Read of our files
df_organisms = pd.read_csv('../results/genomes/list_organisms.tsv', header=None)
df_merged = pd.read_csv('../data/merged_list.csv', low_memory=False)

# recovery of the important part 
df_organisms[0] = df_organisms[0].str.rsplit('_', n=1).str[0]
df_organisms.columns = ['Assembly']

# Way to find the right assembly
df_organisms['Assembly'] = df_organisms['Assembly'].str.replace('GCF', 'GCA')

# Merging to have a single file with the right informations
merged_data = df_organisms.merge(df_merged, how='left', on='Assembly')

print(merged_data)

# saving of our csv
merged_data.to_csv('../results/list_organisms_merged.csv', index=False)