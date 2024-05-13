import sys 
import os 
import pandas as pd

# The goal of this scirpt is to make some stats with all the results from PGCfinder to decipher patterns that can later be exploit

dir_aln = sys.argv[1]
dir_trim = sys.argv[2]

list_Pseudomonadota = pd.read_csv("results/lists/list_organisms_merged.csv")

print (list_Pseudomonadota.describe())