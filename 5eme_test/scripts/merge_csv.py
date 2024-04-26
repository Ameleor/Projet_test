import pandas as pd

# Read data from first CSV
data_briant = pd.read_csv('data/supp_data_from_thiel_et_al_2018/table_3_2col.csv')
data_list = pd.read_csv('data/lists/list_Pseudomonadota_modif.csv')

# Copy data frames
full_data_briant = data_briant.copy()
full_data_list = data_list.copy()

# Delete the last two digits which correspond to the version
data_briant['Assembly'] = data_briant['Assembly'].str[:-2]
data_list['Assembly'] = data_list['Assembly'].str[:-2]

# Merge data frames using data_list as the main
merged_data = data_list.merge(data_briant, how='left', on='Assembly')

# Update Assembly column with values from full_data_list
merged_data['Assembly'] = full_data_list['Assembly']

# Save merged data to CSV
merged_data.to_csv('data/lists/merged_list.csv', index=False)

### PGCfinder part ###
# Uncomment and adapt below code for PGCfinder part
# import sys 
# genome = sys.argv[1]
# all_best_solutions = pd.read_csv(genome+'/hmmer_results/all_best_solutions.tsv', sep='\t')
# best_solution_summary = pd.read_csv(genome+'/hmmer_results/best_solution_summary.tsv', sep='\t')

# Read files for list part
df_organisms = pd.read_csv('results/lists/list_organisms.csv', header=None)
df_merged = pd.read_csv('data/lists/merged_list.csv', low_memory=False)

# Extract important part from df_organisms
df_organisms[0] = df_organisms[0].str.rsplit('_', n=1).str[0]
df_organisms.columns = ['Assembly']

# Replace 'GCF' with 'GCA' in Assembly column
df_organisms['Assembly'] = df_organisms['Assembly'].str.replace('GCF', 'GCA')

# Merge to have a single file with the right information using the "Assembly" column
merged_data = df_organisms.merge(df_merged, how='left', on='Assembly')

# Save CSV
merged_data.to_csv('results/lists/list_organisms_merged.csv', index=False)


#Phototrophic_group = merged_data.iloc[:, 16]

# Filter to see how many of the bacteria from briant didn't find a match
#unmerged_data_briant = full_data_briant[~full_data_briant['Assembly'].isin(merged_data['Assembly'])]

#print(unmerged_data_briant)
