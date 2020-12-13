from functions import *
from drawing import *
import networky as ny

def prims_algorithm(G, start_vert, show_g, show_c):
    
    A = prims_ini(G, start_vert)
    
    if isinstance(A,str) == True: #to check if the vertex exists in the graph
        print(A)
        return A
        
    while is_span(G,A)==False: # to check functions
        e = min_prims_edge(G,A)
        A.add_edge(e[0],e[1])
        
    if show_g == True: # to display a visual representation of the subtree
        show_weighted_graph(G)
        draw_subtree(G,A)
        
    if show_c == True: # to display the weight of the graph
        total_c = 0
        for y in E(A): #to add up all the weights
            total_c = total_c + c(G,x)
        print("the cost of the spanning tree is: " + str(total_c))
            
    return A
