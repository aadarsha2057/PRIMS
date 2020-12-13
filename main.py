import networkx as ny
from functions import * 
from drawing import *
from algorithms import *

graph_data = open('Graphs/graph4.txt','r') #read in the graph you want to test graph1 - graph4

G = ny.read_weighted_edgelist(graph_data, nodetype = int) #create initial graph 

A = prims_alg(G, int(input("Type starting vertex: ")), True, True) #ask the user what verticy they want to start on
