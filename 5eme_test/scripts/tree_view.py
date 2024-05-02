from ete3 import Tree

tree_bionj = Tree("results/tree/pufM.bionj")
# tree_iqtree = Tree("results/tree/pufM.iqtree") -> You may want to check other newick loading flags like 'format' or 'quoted_node_names'.
# tree_treefile = Tree("results/tree/pufM.treefile")

tree_bionj.show()