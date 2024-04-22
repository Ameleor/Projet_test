import openpyxl
import warnings

# Ignorer les avertissements openpyxl
warnings.simplefilter("ignore")

# Chemin du fichier Excel
xlsx_file = "../data/supp_data_from_thiel_et_al_2018/pp69_bryant_supplemental_table3.xlsx"

# Onglets à parcourir
sheets = [1, 2, 3]

# Nom du fichier de sortie
output_file = "../results/files/data_supp.txt"

# Fonction pour récupérer les données de la troisième colonne
def extract_column(sheet):
    column_data = []
    for row in sheet.iter_rows():
        if row[4].value and str(row[4].value).startswith("GCA"):
            column_data.append(row[4].value)  # La troisième colonne, indexée à partir de 0
    return column_data

# Ouvrir le fichier Excel
workbook = openpyxl.load_workbook(xlsx_file)

# Ouvrir le fichier de sortie
with open(output_file, "w") as output:
    # Parcourir les onglets spécifiés
    for sheet_index in sheets:
        sheet = workbook.worksheets[sheet_index - 1]  # Les index des onglets commencent à 0
        column_data = extract_column(sheet)
        # Écrire les données dans le fichier de sortie
        for data in column_data:
            output.write(str(data) + "\n")

print("Extraction terminée. Les données ont été écrites dans", output_file)
