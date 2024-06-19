#Explication des différentes listes présentes:

###list_modif.csv:
Réduction de list_with_taxonomy.csv avec uniquement les colonnes qui nous intéressent.

###list_organisms_merged.csv:
Fichier nous permettant d'observer si la fusion entre les différentes listes s'était bien passé (obsolète).

###list_Pseudomonadota_modif.csv:
Réduction de la list_Pseudomonadota_with_taxonomy afin de ne garder que les colonnes qui nous intéressent

###list_Pseudomonadota_with_taxonomy.csv:
list_with_taxonomy.csv modifié afin de n'y garder que les pseudomonadotas.

###list_with_taxonomy.csv:
Liste originel possèdant la taxonomie de chaque bactéries présentent dans la base de données.

###merged_list.csv:
Fusion de la liste des organismes ainsi que celle tiré de la table de Bryant 2018. On y rajoute donc si chaque bactéries sont (p)AAPB/(p)PN(S)B

###pre-list_check.csv:
Petit échantillon d'informations représentatives de "list_Pseudomonadota_with_taxonomy.csv" afin de vérifier via un script si j'ai la bonne méthode pour récupérer les informations.
J'ai utilisé ce script pour récupérer le nom afin d'y lier les dossiers et copier ceux-ci à un autre endroit.
