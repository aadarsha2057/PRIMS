import networkx as ny

def V(graph):
    return set(graph.nodes()) #list of the vertices

def E(graph):
    return set(graph.edges()) #list of the edges

def prims_ini(graph, v ): #to check if the starting vertices exist
    if(v not in V(graph)):
        return 'Error: Vertex NOT Found' #if there's an error
    else: #to initialize the subtree
        A=nx.Graph()
        A.add_node(v)
        return A

def is_span(graph, subgraph): #to make sure that the subtree does not include cycles or all the edges of G
    return V(graph)==V(subgraph)

def cost(G, e): #to return the weight of the edge
    return G[e[0]][e[1]]['weight']

def possible_edges(G,A): #to check to see what edges do not create a cycle
    return [e for e in list(G.edges(V(A))) if e[0] not in V(A) or e[1] not in V(A)]

def min_prims_edge(G,A):
    possible = possible_edges(G, A)
    minimum = 9999999999 #to check for minimum default set to a really high number
    next_edge = list() #to hold the edge that has the minimum weight
    for y in range(0,len(possible),1): #to run through the list of edges
        weight = cost(G,possible[y]) #to keeps track of the weight
        if weight < minimum: #to compare the weight of the edge to current min
            minimum = cost(G,possible[y]) #to set the min to the smallest weight
            next_edge = possible[y] #to save the edge with small weight
    return next_edge #to return the smallest edge
