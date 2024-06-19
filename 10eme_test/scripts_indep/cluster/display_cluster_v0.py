import networkx as nx
import matplotlib.pyplot as plt
import csv

# Read the CSV file
edges = []

with open('results/fasta_PGC/blast/seq.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        cluster, sequence = row
        edges.append((cluster, sequence))

# Create a graph
G = nx.Graph()
G.add_edges_from(edges)

# Filter clusters with at least three sequences attached
clusters_with_three_or_more_sequences = [cluster for cluster in G.nodes() if sum(1 for edge in G.edges() if edge[0] == cluster or edge[1] == cluster) >= 3]
filtered_edges = [(cluster, sequence) for cluster, sequence in G.edges() if cluster in clusters_with_three_or_more_sequences]

# Create a new graph with filtered edges
G_filtered = nx.Graph()
G_filtered.add_edges_from(filtered_edges)

# Draw the graph
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G_filtered, k=0.1)
nx.draw(G_filtered, pos, with_labels=False, node_size=50, font_size=5)
plt.title('Sequence Clusters with at least Three Sequences')
plt.show()
