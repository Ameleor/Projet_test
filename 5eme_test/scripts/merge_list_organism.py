import pandas as pd

df_organisms = pd.read_csv('../results/genomes/list_organisms.tsv', header=None)
df_merged = pd.read_csv('../data/merged_list.csv', low_memory=False)

df_organisms[0] = df_organisms[0].str.rsplit('_', n=1).str[0]
df_organisms.columns = ['Assembly']
df_organisms['Assembly'] = df_organisms['Assembly'].str.replace('GCF', 'GCA')

merged_data = df_organisms.merge(df_merged, how='left', on='Assembly')

print(merged_data)

merged_data.to_csv('../results/list_organisms_merged.csv', index=False)