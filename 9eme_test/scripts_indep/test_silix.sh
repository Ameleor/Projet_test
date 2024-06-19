#!/bin/bash

# Ce code à pour but de tester Silix avec des paramètres se modifiant petit à petit pour comparer le nombre de familles qu'il propose
input_file="results/fasta/all_fasta_gathered.faa"
blast_file="results/fasta/blast/blastall.out"
output_nodes="results/fasta/blast/seqv2.fnodes"

i_value=0.1
r_value=0.1

while (( $(echo "$i_value <= 1.0" | bc -l) )); do
    while (( $(echo "$r_value <= 1.0" | bc -l) )); do
        echo "Running silix with -i $r_value and -r $i_value"
        silix "$input_file" "$blast_file" -f FAM -i "$r_value" -r "$i_value" > "$output_nodes"
        r_value=$(echo "$r_value + 0.1" | bc)
    done
    r_value=0.1
    i_value=$(echo "$i_value + 0.1" | bc)
done
