from ete3 import Tree, TreeStyle, TextFace

def layout(node) :
    if node.is_leaf() :
        parts = node.name.split('_')
        modified_name = ' '.join(parts[-3:])
        #modified_name = '_'.join(parts[:2]) + " " + ' '.join(parts[-3:])
        node.name = modified_name
        #seq = sector[name]
        #seqFace = SeqMotifFace(seq, motifs = [[0, 20, "seq", 10, 10, None, None, None]], scale_factor = 1)
        #add_face_to_node(seqFace, node, 2, position = "aligned")
        #nstyle = NodeStyle()
        #nstyle["fgcolor"] = gene_colors[name]
        #nstyle["size"] = 10
        #node.set_style(nstyle)
        #square = RectFace(10, 10, fgcolor = gene_colors[name], bgcolor = gene_colors[name])
        #blank_square = RectFace(10, 10, fgcolor = "white", bgcolor = "white")
        #add_face_to_node(square, node, 0, position = "aligned")
        #add_face_to_node(blank_square, node, 1, position = "aligned")


t1= Tree("results/tree/PGC_pufM/PGC_pufM.bionj")
t2= Tree("results/tree/PGC_pufL/PGC_pufL.bionj")
t3= Tree("results/tree/PGC_crtB/PGC_crtB.bionj")

# tree_iqtree = Tree("results/tree/pufM.iqtree") -> You may want to check other newick loading flags like 'format' or 'quoted_node_names'.
# tree_treefile = Tree("results/tree/pufM.treefile")

ts= TreeStyle()

tree = [t1, t2, t3]
#tree_bionj.show()
for t in tree:
    for leaf in t: 
        layout(leaf)

#ts.layout_fn = layout
#t.render("%%inline", tree_style = ts)

for i in tree:
    print(i)

ts.show_leaf_name = True
ts.mode = "c"
ts.arc_start = -180 # 0 degrees = 3 o'clock
ts.arc_span = 180
ts.title.add_face(TextFace("Phylogenetic Tree of a gene from the PGC", fsize=20), column=0)
t.show(tree_style=ts)
