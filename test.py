import networky as ny
from functions import *
from algorithms import prims_alg
from drawing import *


graph_data = open('Graphs/graph01.txt', 'r')

G=ny.read_weighted_edgelist(graph_data, nodetype=int)

A= prims_alg(G, 0, show_graph = True, show_cost = True)
