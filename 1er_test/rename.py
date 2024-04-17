import os
import sys

def rename_files(input_dir, output_dir):
    # Vérifier si le répertoire de sortie existe, sinon le créer
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Liste des fichiers dans le répertoire d'entrée
    files = os.listdir(input_dir)

    # Parcourir chaque fichier et le renommer
    for file_name in files:
        # Renommer le fichier en ajoutant un préfixe "renamed_"
        new_file_name = "renamed_" + file_name
        # Chemin d'accès complet au fichier d'entrée
        input_file_path = os.path.join(input_dir, file_name)
        # Chemin d'accès complet au nouveau fichier renommé
        output_file_path = os.path.join(output_dir, new_file_name)
        # Renommer le fichier
        os.rename(input_file_path, output_file_path)
        print(f"Renamed {file_name} to {new_file_name}")

if __name__ == "__main__":
    # Vérifier les arguments en ligne de commande
    if len(sys.argv) != 3:
        print("Usage: python rename.py <input_directory> <output_directory>")
        sys.exit(1)

    # Récupérer les répertoires d'entrée et de sortie des arguments en ligne de commande
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    # Appeler la fonction de renommage des fichiers
    rename_files(input_dir, output_dir)
