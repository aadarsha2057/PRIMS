import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *


graph_data = open('test-graphs/G1.txt', 'r')

G=nx.read_weighted_edgelist(graph_data, nodetype=int)

T= prims_algorithm(G, 0, show_graph = True, show_cost = True)
