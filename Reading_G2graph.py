#this file just reads and plots the edges of the G2 graph
#the anonymized graph 

import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

g=nx.read_edgelist('G2.edgelist',create_using=nx.Graph(),nodetype=int)

print (nx.info(g))

nx.draw(g)

plt.show()