## But de ce test

Le but de ce test est d'améliorer ma pipeline snakemake en y ajoutant une partie de récupération de fasta, puis ensuite de permettre l'utilisation successive de blast (all) et SiLiX pour faire des cluster de mes gènes.

## Résultats de ce test

### Déroulé:

Ce test finit nous permet de récupérer un fichier fasta comprenant:
- un blast all vs all de tout nos fastas de PGC ainsi que les gènes proches (+ ou - 5)
- un résultat SiLiX utilisant les options par défaut de ces memes fasta combiné à la sortie blast
- une amélioration de ce fichier fasta nous permettant de récupérer les informations disposé par NCBI sur les gènes (comprenant: taxonomie, nom de gène, description etc) couplé à nos résultats PGCfinder

### Analyse:

#### Récap mélange:

Nous obtenons donc 84 familles de gènes comprenant plus de 100 gènes (sachant que nous avons au préalable 245 PGC trouvés dans 245 souches).
Dans la majorité des cas nous retrouvons nos gènes annotés par PGCfinder dans une meme et seul famille SiLiX. Les seules différences notables sont:
- crtF et bchE: ceux-ci se retrouvent dans une même famille. Les descriptions NCBI sont aussi mélangés entre les deux et nous ne disposons pas de noms de gènes (via NCBI)
- lhaA et pucC2: ceuc-ci se retrouvent aussi dans la même famille et avec des descriptions mélangés.
- bchX et bchL: Ceux-ci sont mélangés tout pareille au niveau de la famille SiLiX mais leur nom de gène via NCBI est respecté (bchX: no_gene_name, bchL: bchL)
- crtD et crtI: Ici nous avons aussi un mélange sauf que les crtD sont annotés crtI par NCBI et les crtI ne sont pas annotés (no_gene_name)
- bchM: une petite partie de ces gènes sont annotés ubiG sur NCBI

#### Autres:

J'ai aussi observés que certains des gènes utilisés par PGCfinder pour annotés n'ont trouvés aucune correspondance avec NCBI:
- bchH, bchN, tspO, bchP, crtE, crtC, crtB, bchO, bchD, crtA

J'ai observé aussi cetaines protéines ayant eux des "ratés", c'est à dire que nous ne les avons pas utilisés pour PGCfinder mais nous observons des gros clusters via SiLiX:
    Partiellement loupé:
- bchO
    Cluster:
- puhC: 236
- pufA: 256
- pufB: 260
- pufC: 160
- crtY: 48
- bchJ: 44
- pufQ: 57
- pufX: 25

L'output SilIx possèdant toute ces informations se trouvent à: Documents/data/fasta_PGC/blast/output_silix_fullname_v1.csv



