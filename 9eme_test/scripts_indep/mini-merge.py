# Le but de ce script est de rajouter à merged_csv les informations de taxonomies nécessaires
import pandas as pd

df_merged = pd.read_csv("data/lists/merged_list.csv")
df_taxonomy = pd.read_csv("data/lists/list_with_taxonomy.csv", low_memory=False)

df_taxonomy_trim = df_taxonomy[["Assembly","class","genus","order","family"]]

df_merged_merge = df_merged.merge(df_taxonomy_trim, how="left", on="Assembly")

df_merged_merge.to_csv("data/lists/merged_list_with_taxonomy.csv")