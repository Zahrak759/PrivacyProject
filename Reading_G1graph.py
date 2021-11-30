
import math
import argparse as ap
import multiprocessing as mp

#this file just reads and plots the nodes and edges from the G1 
#graph, which is the OG graph

import networkx as nx
import matplotlib.pyplot as plt
import scipy as sp

g1 =nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

g2 =nx.read_edgelist('G2.edgelist',create_using=nx.Graph(),nodetype=int)

seed_pairing = nx.read_edgelist('seed_node_pairs.txt',create_using=nx.Graph(),nodetype=int)

#how to list neighbors of a node 
for i in g1.nodes():
        print(i,': ',list(g1.neighbors(i)))

for i in g2.nodes():
        print(i, ': ',len(list(g2.neighbors(i))), list(g2.neighbors(i)))

for i in seed_pairing.nodes():
        print(i, ': ', list(seed_pairing.neighbors(i)))