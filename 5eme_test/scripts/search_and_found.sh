#!/bin/bash

pgc_hit_file="../results/files_txt/PGC_hit.txt"

csv_file="../data/list_with_taxonomy.csv"

# searching if 
find ../results/ -type f -exec grep -l "Systems found:" {} + | grep '\all_systems.txt$' | awk -F/ '{print $3}' | cut -c -15 > "$pgc_hit_file"

# Verification of the file existence
if [ ! -f "$pgc_hit_file" ]; then
    echo "Le fichier PGC_hit.txt n'existe pas."
    exit 1
fi

# Verification of the file existence
if [ ! -f "$csv_file" ]; then
    echo "Le fichier list_with_taxonomy.csv n'existe pas."
    exit 1
fi

# Loop to see every line of the file
while IFS= read -r line; do
    # Creation of the line that will be ln the output files with the important informations 
    grep "$line" "$csv_file" | awk -F',' '{print $1,$3,$2}' | sort -k2
done < "$pgc_hit_file"
