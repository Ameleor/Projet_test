# 3eme test en relation avec l'utilisation de snakemake

## Objectif:

Le but ici est de continuer notre pipeline en y rajoutant les méthodes de création d'arbre en utilisant successivement: la pipeline du 4eme essais + mafft-linsi + BMGE + iqtree2

### Mafft-linsi:
C'est un programme d'alignement multiple de sequence (MSA) qui nous permet de ranger convenablement tout nos fastas entre eux.

### BGME:
C'est un programme de "trim", c'est à dire qu'il permet de nettoyer les différentes séquences qu'il utilise afin d'avoir un alignement de séquence plus représentatif et plus court.

### IQtree2:
C'est le logiciel nous permettant d'utiliser les sorties précédentes afin d'afficher un arbre phylogénétique.


