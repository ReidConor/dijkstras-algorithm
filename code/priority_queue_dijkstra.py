import networkx as nx
import math
from tools.priority_queue import PriorityQueue
import matplotlib.pyplot as plt
import random
import operator
import os

#####
#####
#
# Dijkstra's algorithm, implemented using a priority queue,
# which makes it more efficient and easier to write
#
#####
#####

def dijkstra_predecessors_and_distances(G, r):
    A, p, D = dijkstra(G, r)
    return p, D

def dijkstra(G, r):
    if not G.has_node(r):#if the graph doesnt have this node
        raise ValueError("Source node " + str(r) + " not present")

    for e1, e2, d in G.edges(data=True):#cant handle negitive weights
        if d["weight"] < 0:
            raise ValueError("Negative weight on edge " + str(e1) + "-" + str(e2))

    P = {r} # permanent set
    S = PriorityQueue() # V-P. This is the crucial data structure.
    D = {} # estimates of SPST lengths
    p = {} # parent-pointers
    A = set() # our result, an SPST

    for n in G.nodes():#for all nodes
        if n == r:#if we're at the source node...
            D[n] = 0#...its weight is zero
        else:
            if G.has_edge(r, n):#if we're at a neighbour
                D[n] = G[r][n]["weight"]#path is the weight of the edge
            else:
                D[n] = math.inf

            p[n] = r
            S.add_task(n, D[n])

    while len(S):
        u, Du = S.pop_task()
        if u in P: continue

        P.add(u) # move one item to the permanent set P and to SPST A
        A.add((p[u], u))

        for v, Dv in S:
            if v in P: continue
            if G.has_edge(u, v):
                if D[v] > D[u] + G[u][v]["weight"]:
                    D[v] = D[u] + G[u][v]["weight"]
                    p[v] = u
                    S.add_task(v, D[v]) # add v, or update its prior

    results={}
    results["SPST"]=A #SPST
    results["predecessors"]=p #predecessors
    results["distances"]=D #distances

    sorted_D = sorted(D.items(), key=operator.itemgetter(1))
    results["generator"]=(n for n in sorted_D)

    return results # let's return the SPST, predecessors and distances: user can decide which to use

if __name__ == "__main__":
    os.system('clear')
    # This is the undirected graph on week 4 slide 28. The solution on the
    # following slide is: {('C', 'F'), ('A', 'C'), ('C', 'D'), ('B',
    # 'G'), ('A', 'B'), ('F', 'E')}
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
    nx.draw_spectral(G, with_labels=True)

    initalNode = "A"
    results = dijkstra(G, initalNode)
    print()
    print(results["SPST"])
    print()
    print("Predecessors for each node")
    print(results["predecessors"])
    print()
    print("Shortest path to each node from", initalNode)
    print(results["distances"])
    print("----------------------------")
    this = nx.shortest_path(G, initalNode)
    print(this)
