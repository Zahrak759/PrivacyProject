
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


#another method that we tried to apply but on our dummy data 

"""
import math
import argparse as ap
import multiprocessing as mp

#this file just reads and plots the nodes and edges from the G1 
#graph, which is the OG graph

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.operators.binary import difference
from networkx.classes.function import neighbors
import scipy as sp
import random

g1 =nx.read_edgelist('G1.edgelist',create_using=nx.Graph(),nodetype=int)

g2 =nx.read_edgelist('G2.edgelist',create_using=nx.Graph(),nodetype=int)

seed_pairing = nx.read_edgelist('seed_node_pairs.txt',create_using=nx.Graph(),nodetype=int)

#dummy data to help the equation out
dummy_data = [0, 1, 2, 3]
random_num = random.choice(dummy_data)


# lines 26-34 basically creates a new list to store how many neighbors each node has in g1 and g2
list_g1 = []
for n, neighdict in g1.adjacency():
    g1_neighbors = len(neighdict)
    list_g1.append(g1_neighbors)

list_g2 = []
for n, neighdict in g2.adjacency():
    g2_neighbors = len(neighdict)
    list_g2.append(g2_neighbors)


# multiplies the number of neigbors together and stores it into a new list
# i already calucated both ways for the square root to make sure they output the same results and they do
results = []
for i in range(0, len(list_g2)):
    results.append(list_g1[i]*list_g2[i])
#print(results)

#calculates by score(1,1) -> score(2,2) and so on
score_list = []
for i in results:
    #print(i)
    if(random_num == 0):
        pass
    elif(random_num != 0):
        score = 0
        score = float(random_num) / math.sqrt(i)
        score_list.append(score)
        #prints the score between g1 and g2
        #print(score)
#prints the score between g1 and g2, just in a list
#print(score_list)

#standard deviation: the calculation story
count = len(score_list)
#print(count)

sum_of_list = sum(score_list)
#print(sum_of_list)

mean = sum_of_list / count
#print(mean)

differences = []
for i in range(0, len(score_list)):
    differences.append(score_list[i] - mean)
#print(differences)

differences_squared =[]
for i in range(0, len(differences)):
    differences_squared.append(differences[i] * differences[i])
#print(differences_squared)

sum_squared_differences = sum(differences_squared)
#print(sum_squared_differences)

variance = sum_squared_differences / (count - 1)
#print(variance)

#standard deviation 
std = math.sqrt(variance)
print(std)


# the story of finding the eccentricity or whatever it is
#first thing first, we need to find the max and second max in the list of the scores

first_max = max(score_list)
print(first_max)

sec_max = set(score_list)
sec_max.remove(max(sec_max))
second_max = max(sec_max)
print(second_max)

#now we calculate the ecc
ecc = (first_max - second_max) / std
print("eccentricity: ", ecc)
combine.txt
3 KB

"""