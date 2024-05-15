#!/usr/bin/bash

# Ce script à pour but de récupérer les noms de dossiers pour les génomes ayant eu au moins un hit via PGCfinder
awk -F ',' '{
    # Vérifie si la colonne 20 contient des caractères
    if ($20 != "") {
        # Divise la colonne 15 par "/" et extrait la partie après le "/"
        n = split($15, parts, "/")
        if (n > 1) {
            print parts[2]  # Affiche la partie après le "/"
        }
    }
}' results/list_organisms_merged.csv | while read -r line; do
    # Pour chaque résultat de grep, copier le dossier correspondant dans ../results/genomes/
    cp -r "results/genomes/$line" "results/genomes_PGC/"
done
