import csv
import shutil
import os

# Chemins des dossiers et du fichier CSV
chemin_fichier_csv = 'results/lists_PGC/list_family_for_species_tree.csv'
dossier_source = 'results/genomes'
dossier_destination = 'results/genome_family_for_species_tree'

# Vérifier si le dossier de destination existe, sinon le créer
if not os.path.exists(dossier_destination):
    os.makedirs(dossier_destination)

# Lire le fichier CSV et copier les fichiers
with open(chemin_fichier_csv, newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Vérifier si la ligne n'est pas vide et a au moins une colonne
        if row and len(row) > 0:
            nom_fichier = row[0].replace("GCA", "GCF")  # Supposant que les noms de fichiers sont dans la première colonne
            chemin_source = os.path.join(dossier_source, nom_fichier)
            chemin_destination = os.path.join(dossier_destination, nom_fichier)
            
            # Vérifier si le fichier source existe
            if os.path.exists(chemin_source):
                shutil.copy2(chemin_source, chemin_destination)
                print(f'Fichier {nom_fichier} copié de {dossier_source} vers {dossier_destination}')
            else:
                print(f'Fichier {nom_fichier} non trouvé dans {dossier_source}')
        else:
            print('Ligne vide ou mal formatée ignorée')

print('Tous les fichiers ont été copiés.')
