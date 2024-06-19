from pyvis.network import Network
import csv
import networkx as nx

# Read the CSV file
edges = []

with open('results/fasta/blast/seq.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        cluster, sequence = row
        edges.append((cluster, sequence))

# Create a graph
G = nx.Graph()
G.add_edges_from(edges)

# Create a pyvis network
nt = Network(notebook=True, cdn_resources='remote', width="100%", height="1200px")

for node in G.nodes:
    nt.add_node(node, label=node)

for edge in G.edges:
    nt.add_edge(edge[0], edge[1])

# Generate and show the network
nt.show('network.html')
