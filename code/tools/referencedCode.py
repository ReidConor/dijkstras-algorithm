import os
import networkx as nx
from heapq import heappush, heappop

#the following function is taken (with some modification) from
#"Python Algorithms, Mastering Basic Algorithms in the Python Language" - Hetland, M.L
#it was found that the other implementation of dijkstra returned a generator very slowly, and hampered the
#bi-directional algorithm significantly
def idijkstra(Graph, initalNode):
    shortest_paths = [(0,initalNode)]#list holding the starting node, with cost 0 (since we're there already)
    visited = set()#empty set, to hold the visited nodes (they will not be revisited)
    while len(shortest_paths) > 0:#while there are still nodes to visit
        d, u = heappop(shortest_paths)#pop over the next node:weight pairing
        if u in visited:#if this node has been visited...
            continue#...continue to the nexxt iteration of the loop
        visited.add(u)#add it to the visited list
        yield u, d#yield the node:weight pairing.
        for v in Graph[u]:#iterate through this nodes neighbours
            heappush(shortest_paths, (d+Graph[u][v]["weight"], v))#add the new node:weight pairing to the list
#list of modifications made:
    #Naming convention. Made more verbose and clear
    #Fix made to heappush section. "Graph[u][v]" changed to "Graph[u][v]["weight"]"
        #the actual weight of the path is to be added to the heap, rather than the node:weight pair
    #altered "while shortest_path:" to "while len(shortest_paths) > 0:" to improve comprehension
    #comments applied

if __name__ == "__main__":#test out this function
    os.system('clear')

    G = nx.Graph()
    E = (
        ("A", "B", 2),
        ("A", "C", 6),
        ("A", "D", 8),

        ("B", "G", 10),
        ("B", "C", 8),

        ("C", "D", 1),
        ("C", "E", 5),
        ("C", "G", 9),
        ("C", "F", 3),

        ("D", "F", 9),
        ("G", "E", 4),
        ("E", "F", 1)
        )
    G.add_weighted_edges_from(E)

    startingNode = "A"
    print(list(idijkstra(G, startingNode)))
