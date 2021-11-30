# PrivacyProject
In this project, you will utilize seed based de-anonymization to solve real problems.

In the seed based de-anonymization part, you have two graphs and a seed node pairs file. The graphs are given in edgelist filetype.
seed_G1.edgelist is the original graph and seed_G2.edgelist is the anonymized graph. The file seed_node_pairs.txt gives some matched node seed pairs.  In the file seed_node_pairs.txt the first column refers the node number in graph G1 and the second column refers the node number in graph G2.

As the answer of this problem, you need to give a file shows full mapping of seed nodes in G1 and G2 and follows the format shown in the file seed_node_pairs.txt.

So for G1, if the source is 1 and target is 3 then that means node 1 of of G1 is connected to node 3 of G2

# How We Approached The Problem
In the given amount of time and resources, we weren’t able to have a working solution. 
We tried working with smaller dummy data that provided us good results but that is as far we could get. We also tried several techniques to implement this project which included Reverse Matching, Choosing the node based on the eccentricity ratio and more. 

We create files that calculates the similarity between the two nodes in G1 and G2. We also calculated the eccentricity and the standard deviation. We could not figure out the mapping, but we created dummy data, to get results, since we need the mapping for the similarity.

To run the program, you can simply run the program in your terminal or any IDE that you use. In addition, in some of the files that we have attempted, you can call the methods out, which is already done for you.
 
# Source Target

Hint:

Example edgelist file format:

a b

a c

d e


You can use package networkx in python to read the edgelist file.

<<<<<<< HEAD

We weren't able to make our project run successfully provided the time and resources.

I have mentioned more details about our effort in the project report

"""

=======
>>>>>>> 0677b12c5cec6bca0d87b2652c8165be1bf4e71c
