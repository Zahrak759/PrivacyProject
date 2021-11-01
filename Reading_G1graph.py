#this file just reads and plots the nodes and edges from the G1 
#graph, which is the OG graph

import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

g=nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

print (nx.info(g))

nx.draw(g)

plt.show()
plt.savefig("g1graph.png")