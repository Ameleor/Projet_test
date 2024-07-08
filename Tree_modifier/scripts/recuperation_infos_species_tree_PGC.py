# The goal of this scripts is to retrive the gene from the genome corresponding to the PGC gene hit
import pandas as pd
import sys
from Bio import SeqIO

list_genome_PGC = [
"    GCA_019285715.1_ASM1928571v1",
    "GCF_001483865.1_ASM148386v1",
    "GCF_011044255.1_ASM1104425v1",
    "GCF_000014045.1_ASM1404v1",
    "GCF_001548015.1_ASM154801v1",
    "GCF_011290485.1_ASM1129048v1",
    "GCF_000015165.1_ASM1516v1",
    "GCF_001632845.1_ASM163284v1",
    "GCF_011388215.1_ASM1138821v1",
    "GCF_000015585.1_ASM1558v1",
    "GCF_001713355.1_ASM171335v1",
    "GCF_013170845.1_ASM1317084v1",
    "GCF_000016185.1_ASM1618v1",
    "GCF_001713375.1_ASM171337v1",
    "GCF_014495845.1_ASM1449584v1",
    "GCF_000018145.1_ASM1814v1",
    "GCF_001713455.1_ASM171345v1",
    "GCF_019134555.1_ASM1913455v1",
    "GCF_000019725.1_ASM1972v1",
    "GCF_001713475.1_ASM171347v1",
    "GCF_019203965.1_ASM1920396v1",
    "GCF_000021005.1_ASM2100v1",
    "GCF_001719165.1_ASM171916v1",
    "GCF_021088345.1_ASM2108834v1",
    "GCF_000021745.1_ASM2174v1",
    "GCF_001720465.1_ASM172046v1",
    "GCF_021228015.1_ASM2122801v1",
    "GCF_000166055.1_ASM16605v1",
    "GCF_002002865.1_ASM200286v1",
    "GCF_021391535.1_ASM2139153v1",
    "GCF_000202835.1_ASM20283v1",
    "GCF_002073975.1_ASM207397v1",
    "GCF_022227035.1_ASM2222703v1",
    "GCF_000225955.1_ASM22595v1",
    "GCF_002813775.1_ASM281377v1",
    "GCF_022370455.1_ASM2237045v1",
    "GCF_000227745.2_ASM22774v3",
    "GCF_002868735.1_ASM286873v1",
    "GCF_023573145.1_ASM2357314v1",
    "GCF_000284255.1_ASM28425v1",
    "GCF_003288315.1_ASM328831v1",
    "GCF_026898155.1_ASM2689815v1",
    "GCF_000284415.1_ASM28441v2",
    "GCF_003855495.1_ASM385549v1",
    "GCF_027271155.1_ASM2727115v1",
    "GCF_000512205.2_ASM51220v2",
    "GCF_003966715.1_ASM396671v1",
    "GCF_027886585.1_ASM2788658v1",
    "GCF_000935025.1_ASM93502v1",
    "GCF_004331955.1_ASM433195v1",
    "GCF_030297575.1_ASM3029757v1",
    "GCF_001402875.1_ASM140287v1",
    "GCF_006542605.1_ASM654260v1",
    "GCF_030297595.1_ASM3029759v1",
    "GCF_001459775.1_Blastochloris_viridis_genome",
    "GCF_008843145.1_ASM884314v1",
    "GCF_937425535.1_Rhodovastum_atsumiense_G2-11"
]


# Try to filter all the non-PGC genomes (thanks to PGCfinder)
try:
    for genome in list_genome_PGC:
        # Use two argument to be launch: {genome} {gene}
        gene_path = "PGC_pufL"

        # Extracting the gene name from the gene path
        gene = gene_path.split('/')[2].split('.')[0]

        # Read files with pandas
        hit_PGC = pd.read_csv('results/genomes_PGC/'+genome+'/PGCfinder/best_solution.tsv', sep='\t', comment='#')
        record_dict = SeqIO.to_dict(SeqIO.parse('data/genomes_unzip_PGC/'+genome+'/'+genome+'_protein.faa', "fasta"))

        # Get the the name of the gene hit from the genome
        column_git_gene = hit_PGC.iloc[:, 1:3]
        hit_PGC_gene = column_git_gene[column_git_gene["gene_name"].str.contains(gene)]
        if not hit_PGC_gene.empty:
            hit_gene = hit_PGC_gene.iloc[0,0]

            # Retrieve the fasta corresponding to the hit
            record_hit = record_dict[hit_gene].format("fasta")

            # Sépare le nom de fasta en une liste de sous-chaînes en fonction des espaces
            fasta_name_parts = record_hit.split(" ")

            # Modify to only keep the right amount of name to concatenate after
            record_hit = "_".join(fasta_name_parts[0].split("_")[:-1]) + "\n" + record_dict[hit_gene].seq
            print(record_hit)

except pd.errors.EmptyDataError:
    pass