#!/bin/bash

# Chemin vers le fichier PGC_hit.txt
pgc_hit_file="../results/files_txt/PGC_hit.txt"

# Chemin vers le fichier CSV
csv_file="../data/list_with_taxonomy.csv"

# Cette commande recherche tous les fichiers contenant "Systems found:" et extrait uniquement les noms de fichier souhaités
find ../results/ -type f -exec grep -l "Systems found:" {} + | grep '\all_systems.txt$' | awk -F/ '{print $3}' | cut -c -15 > "$pgc_hit_file"

# Vérifie si PGC_hit.txt existe
if [ ! -f "$pgc_hit_file" ]; then
    echo "Le fichier PGC_hit.txt n'existe pas."
    exit 1
fi

# Vérifie si le fichier CSV existe
if [ ! -f "$csv_file" ]; then
    echo "Le fichier list_with_taxonomy.csv n'existe pas."
    exit 1
fi

# Boucle à travers chaque ligne du fichier PGC_hit.txt
while IFS= read -r line; do
    # Exécute la commande grep avec le nom de fichier actuel comme argument dans list_with_taxonomy.csv
    grep "$line" "$csv_file" | awk -F',' '{print $1,$3,$2}' | sort -k2
done < "$pgc_hit_file"
