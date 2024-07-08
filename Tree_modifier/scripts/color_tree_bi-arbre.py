# Ouvrir le fichier en mode lecture
with open('data/unique_gene/bchE_crtF/bchE_crtF.phy', 'r') as file:
    # Lire chaque ligne du fichier
    for line in file:
        # Récupérer le premier mot de la ligne
        first_word = line.split()[0]
        
        # Vérifier si le premier mot contient "crtI" ou "crtD" et afficher le message correspondant
        if "bchE" in first_word:
            print(f"{first_word},#FF0000,bchE")
        elif "crtF" in first_word:
            print(f"{first_word},#0000FF,crtF")
