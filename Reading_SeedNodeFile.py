#this file just reads the nodes and the edges and plots it

import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

g=nx.read_edgelist('seed_node_pairs.txt',create_using=nx.Graph(),nodetype=int)

print (nx.info(g))

nx.draw(g)

plt.show()