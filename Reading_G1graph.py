#this file just reads and plots the nodes and edges from the G1 
#graph, which is the OG graph

import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
import scipy as sp

g=nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

print (nx.info(g))

# nx.draw(g)

# plt.show()
# plt.savefig("g1graph.png")

#listing edges(pairs)
#print(list(g.edges))

#listing the neighbors of node 3506
print(list(g.adj[3506]))

#listing the degree of node 3506 (the number of edges incident to 1)
#print(g.degree[3506])

#finds the shortest path from node 0 to node 3506
print([p for p in nx.all_shortest_paths(g, source=0, target=3506)])