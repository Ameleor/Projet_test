import pandas as pd

data_briant = pd.read_csv('../data/supp_data_from_thiel_et_al_2018/table_3_2col.csv')
data_list = pd.read_csv('../data/list_modif.csv')
full_data_briant = data_briant.copy()
full_data_list = data_list.copy()

# Delete of the last two digit which correspond to the version
data_briant['Assembly'] = data_briant['Assembly'].str[:-2]
data_list['Assembly'] = data_list['Assembly'].str[:-2]

# Merge of our two dataframe using data_list as the main
merged_data = data_list.merge(data_briant, how='left', on='Assembly')

merged_data['Assembly'] = full_data_list['Assembly']

# Creation of the .csv to download the results
merged_data.to_csv('merged_list.csv', index=False)

Phototrophic_group = merged_data.iloc[:, 16]

# Filter to see how many of the bacteria from briant didn't find a match
unmerged_data_briant = full_data_briant[~full_data_briant['Assembly'].isin(merged_data['Assembly'])]

print(unmerged_data_briant)
