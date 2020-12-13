import networkx as ny

def V(graph):
    return set(graph.nodes()) #list of vertices

def E(graph):
    return set(graph.edges()) #list of edges

def prims_ini(graph, v ): #checks if the starting verticy exists
    if(v not in V(graph)):
        return 'Error: Vertex NOT Found' #error message
    else: #initializes the subtree
        A=nx.Graph()
        A.add_node(v)
        return A

def is_span(graph, subgraph): # makes sure the subtree doesn't include cycles or all edges of G
    return V(graph)==V(subgraph)

def cost(G, e): #return the weight of the edge
    return G[e[0]][e[1]]['weight']

def possible_edges(G,A): #checks to see what edges don't create a cycle
    return [e for e in list(G.edges(V(A))) if e[0] not in V(A) or e[1] not in V(A)]

def min_prims_edge(G,A):
    possible = possible_edges(G, A)
    minimum = 9999999999 #used to check for minimum default set to a really high num
    next_edge = list() #used to hold the edge that has the minimum weight
    for y in range(0,len(possible),1): #runs through the list of edges
        weight = cost(G,possible[y]) #keeps track of the weight
        if weight < minimum: #compare the weight of the edge to current min
            minimum = cost(G,possible[y]) #set the min to the smallest weight
            next_edge = possible[y] #save the edge with small weight
    return next_edge #return the smallest edge
