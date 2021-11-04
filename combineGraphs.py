import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
import scipy as sp

g1=nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

g2=nx.read_edgelist('G2.edgelist',create_using=nx.Graph(),nodetype=int)

#checks if the graphs are the same, returns False
print(nx.is_isomorphic(g1,g2))

#listing edges(pairs) in g1
g1_edges = list(g1.edges)

#listing edges (pairs) in g2
g2_edges = list(g2.edges)


#prints a bunch of nonstop edges 
# for i in g1_edges:
#     for j in g2_edges:
#       if(i not in j):
#           print(g2_edges)  

#prints pairs that are not in each other lists/graphs
# not_in_g1 = list(set(g1_edges).difference(g2_edges))
# print(not_in_g1)

#same thing as the first one dummy lol
not_in_g2 = list(set(g2_edges).difference(g1_edges))
# print(not_in_g2)

#so there is 158543 nodes/edges that are not the same
sum = len(not_in_g2)
# print(sum)
set_g1 = set(g1_edges)
set_g2 = set(g2_edges)
matching_pairs = set_g1.intersection(set_g2)
print(matching_pairs)
convert = list(matching_pairs)
#there are 1259 pairs/edges that are matched in g1 and g2 graph
matches = len(convert)
print(matches)