import pandas as pd

# Read data from first CSV
data_briant = pd.read_csv('data/supp_data_from_thiel_et_al_2018/table_3_2col.csv')
data_list = pd.read_csv('data/lists/list_Pseudomonadota_modif.csv')
# Read files for list part
df_organisms = pd.read_csv('results/lists/list_organisms.csv', header=None)
df_infos_PGC = pd.read_csv('results/lists/list_PGC_infos.csv', header=None)

# Copy data frames
full_data_briant = data_briant.copy()
full_data_list = data_list.copy()

# Delete the last two digits which correspond to the version
data_briant['Assembly'] = data_briant['Assembly'].str[:-2]
data_list['Assembly'] = data_list['Assembly'].str[:-2]

# Merge data frames using data_list as the main
merged_data_csv = data_list.merge(data_briant, how='left', on='Assembly')

# Update Assembly column with values from full_data_list
#merged_data_csv['Assembly'] = full_data_list['Assembly']

df_merged=merged_data_csv

# Extract important part from df_organisms
infos_version = df_organisms[0].str.rsplit('.', n=1).str[1]
df_organisms[0] = df_organisms[0].str.rsplit('.', n=1).str[0]

# Changing the column name to merge
df_organisms.columns = ['Assembly']
df_infos_PGC = df_infos_PGC.rename(columns={0: 'Assembly', 1: 'number of PGC', 2: 'number of genes', 3:'PGC replicon type'})
df_infos_PGC['Assembly']=df_infos_PGC['Assembly'].str.rsplit('.', n=1).str[0]

# Replace 'GCF' with 'GCA' in Assembly column
df_organisms['Assembly'] = df_organisms['Assembly'].str.replace('GCF', 'GCA')
df_infos_PGC['Assembly'] = df_infos_PGC['Assembly'].str.replace('GCF', 'GCA')

# Merge to have a single file with the right information using the "Assembly" column
merged_data_list = df_organisms.merge(df_merged, how='left', on='Assembly')
merged_data_list = merged_data_list.merge(df_infos_PGC, how='left', on='Assembly')
print(infos_version)
merged_data_list['Assembly'] = merged_data_list['Assembly'].str.cat(infos_version, sep='.')

# Save CSV
merged_data_list.to_csv('results/lists/list_organisms_merged.csv', index=False)


#Phototrophic_group = merged_data_csv.iloc[:, 16]

# Filter to see how many of the bacteria from briant didn't find a match
#unmerged_data_briant = full_data_briant[~full_data_briant['Assembly'].isin(merged_data_csv['Assembly'])]

#print(unmerged_data_briant)
