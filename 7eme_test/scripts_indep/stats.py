import pandas as pd

# Chargement des données depuis le fichier CSV
data = pd.read_csv('../data/list_with_taxonomy.csv')

# Ouverture du fichier stats.txt en mode écriture
with open('../results/stats.txt', 'w') as file:

    # Statistiques générales
    file.write("Statistiques générales :\n")
    file.write(f"Nombre total de lignes : {len(data)}\n")
    file.write(f"Nombre de colonnes : {len(data.columns)}\n\n")

    # Statistiques sur chaque colonne
    file.write("Statistiques sur chaque colonne :\n")
    for column in data.columns:
        file.write(f"Nom de la colonne : {column}\n")
        file.write(f"Type de données : {data[column].dtype}\n")
        file.write(f"Nombre de valeurs uniques : {data[column].nunique()}\n")
        file.write(f"Nombre de valeurs manquantes : {data[column].isnull().sum()}\n\n")

    # Statistiques sur les valeurs numériques
    numeric_data = data.select_dtypes(include=['number'])
    if not numeric_data.empty:
        file.write("Statistiques sur les valeurs numériques :\n")
        file.write(f"Somme :\n{numeric_data.sum()}\n\n")
        file.write(f"Moyenne :\n{numeric_data.mean()}\n\n")
        file.write(f"Écart-type :\n{numeric_data.std()}\n\n")
        file.write(f"Valeur minimale :\n{numeric_data.min()}\n\n")
        file.write(f"Valeur maximale :\n{numeric_data.max()}\n\n")

    # Statistiques sur les valeurs catégoriques
    categorical_data = data.select_dtypes(exclude=['number'])
    if not categorical_data.empty:
        file.write("Statistiques sur les valeurs catégoriques :\n")
        for column in categorical_data.columns:
            file.write(f"Valeurs uniques pour la colonne {column} :\n{categorical_data[column].unique()}\n\n")
            file.write(f"Nombre d'occurrences de chaque valeur pour la colonne {column} :\n{categorical_data[column].value_counts()}\n\n")
