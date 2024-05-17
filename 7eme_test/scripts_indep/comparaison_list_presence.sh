# Comparaison de sortie dans une liste, ici comparaison si les lignes incomplètes sont communes entre les deux recherches
cat list_with_taxonomy.csv | grep Pseudomonadota | awk -F ',' '{
    if ($2 !~ /proteobacteria/ && $25 !~ /proteobacteria/) {
        array1[$1] = 1
    }
    if ($2 !~ /Pseudomonadota/ && $23 !~ /Pseudomonadota/) {
        array2[$1] = 1
    }
}
END {
    common_count = 0
    for (id in array1) {
        if (id in array2) {
            common_count++
        }
    }
    print "Nombre de génomes communs entre les deux sorties :", common_count
}'  
