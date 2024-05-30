# Read the .fnodes file
fnodes_file = 'results/fasta_PGC/blast/seq.fnodes'
csv_file = 'results/fasta_PGC/blast/seq.csv'

with open(fnodes_file, 'r') as f_in, open(csv_file, 'w') as f_out:
    # Write the header for the CSV file
    f_out.write('Cluster,Sequence\n')
    
    # Process each line in the .fnodes file
    for line in f_in:
        # Strip any leading/trailing whitespace
        line = line.strip()
        
        # Split the line into cluster and sequence parts
        parts = line.split()
        
        # Write the cluster and sequences to the CSV file
        cluster_id = parts[0]
        sequences = parts[1:]
        for seq in sequences:
            f_out.write(f'{cluster_id},{seq}\n')

print(f'Converted {fnodes_file} to {csv_file}')
