import pandas as pd
import sys 

###PGCfinder part
#genome = sys.argv[1]
#all_best_solutions = pd.read_csv(genome+'/hmmer_results/all_best_solutions.tsv', sep='\t')
#best_solution_summary = pd.read_csv(genome+'/hmmer_results/best_solution_summary.tsv', sep='\t')

###List part
# Read of our files
df_organisms = pd.read_csv('results/lists/list_organisms.csv', header=None)
df_merged = pd.read_csv('data/lists/merged_list.csv', low_memory=False)

# recovery of the important part 
df_organisms[0] = df_organisms[0].str.rsplit('_', n=1).str[0]
df_organisms.columns = ['Assembly']

# Way to find the right assembly
df_organisms['Assembly'] = df_organisms['Assembly'].str.replace('GCF', 'GCA')

###Merge part
# Merging to have a single file with the right informations using the "Assembly" column
merged_data = df_organisms.merge(df_merged, how='left', on='Assembly')

#print(merged_data)

# saving of our csv
merged_data.to_csv('results/lists/list_organisms_merged.csv', index=False)