import networkx as nx
import matplotlib.pyplot as plt
from networkx.classes.function import neighbors
import scipy as sp

g1=nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

g2=nx.read_edgelist('G2.edgelist',create_using=nx.Graph(),nodetype=int)

seed_pairing = nx.read_edgelist('seed_node_pairs.txt',create_using=nx.Graph(),nodetype=int)

#checks if the graphs are the same, returns False
print(nx.is_isomorphic(g1,g2))

#listing edges(pairs) in g1
g1_edges = list(g1.edges)

#listing edges (pairs) in g2
g2_edges = list(g2.edges)

#list the seed pairing from both graphs;i.e. column one is g1 first col and column 2 is g2 second col
seed_pairs = list(seed_pairing.edges)

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
matching_pairs = set_g1.intersection(set_g2)    #prints matching pairs in g1 and g2
#print(matching_pairs)


convert = list(matching_pairs)
#there are 1259 pairs/edges that are matched in g1 and g2 graph
matches = len(convert)
#print(matches)

#gets first index in g1
first_col_g1 = []
for list in g1_edges:
    first_col_g1.append(list[0])
#print(first_col_g1)
print(len(first_col_g1)) #159748 nodes

#gets second index in g2
second_col_g2 = []
for list in g2_edges:
    second_col_g2.append(list[1])
#print(second_col_g2)
print(len(second_col_g2)) #159802 nodes

#need to figure out how to connect g1 column to g2 column and/or compare them to the seed pairing file
def merge(g1, g2):
    merged = tuple(zip(g1, g2))
    return merged
#print(merge(first_col_g1, second_col_g2))

def matches ():
    set_g3seed = set(seed_pairs)
    g3 = merge(first_col_g1,second_col_g2)
    combined_g3 = set(g3)
    matching_pairs = set_g3seed.intersection(combined_g3)
    return matching_pairs
print(matches())

#find neighbors for each node in each graph and implement an algorithm that calculates the similiarities of the nodes.