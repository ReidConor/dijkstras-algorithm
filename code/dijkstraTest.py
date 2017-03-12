import time
import os
import networkx as nx
from random import *
import priority_queue_dijkstra as pqd
import bidirectional_dijkstra as dbd
import genGraphs as gg
import tools.referencedCode as rc

def timeMyDijkstra(Graph, initalNode):#timing function for this dijkstra implementation
    start = time.time()
    pqd.dijkstra(Graph, initalNode)
    # rc.idijkstra(Graph, initalNode)#comment in for third party implementation of dijkstra
    elapsed = time.time() - start
    return elapsed

def timeDijkstra(Graph, initalNode):#timing function for networkx's dijkstra (or single_source_shortest_path)
    start = time.time()
    nx.single_source_shortest_path(Graph, initalNode)
    elapsed = time.time() - start
    return elapsed

def timeMyBidirectionalDijkstra(Graph, initalNode, targetNode):#timing function for my implementation of bi-directional dijkstra
    start = time.time()
    dbd.bidirectional_dijkstra(Graph, initalNode, targetNode)
    elapsed = time.time() - start
    return elapsed

def timeBidirectionalDijkstra(Graph, initalNode, targetNode):#timing function for the nx implementation of bi-directional dijkstra
    start = time.time()
    nx.bidirectional_dijkstra(Graph, initalNode, targetNode)
    elapsed = time.time() - start
    return elapsed


if __name__ == "__main__":
    # os.system('clear')
    print("Starting dijkstraTest")
    testCount=1
    graphsPerTest=10
    print("Running %s tests" % testCount)
    print("Using %s graphs per test" % graphsPerTest)
    print("-----------------------------------------")

    for i in range(1, testCount+1):
        print("Running test number: %s" % i )
        Graphs = gg.gen_random_graphs(graphsPerTest)
        for Graph in Graphs:
            print("----------")
            print("Number of nodes:", len(nx.nodes(Graph)))
            print("Number of edges:",len(nx.edges(Graph)))
            initalNode = choice(nx.nodes(Graph))#chose a random node in the graph as the starter node
            targetNode = choice(nx.nodes(Graph))#chose a random node in the graph as the target node

            #-------------------Dijkstra
            timeTaken = round(timeMyDijkstra(Graph, initalNode),6)
            print("Time Taken (Dijkstra):", timeTaken)
            timeTaken = round(timeDijkstra(Graph, initalNode),6)
            print("Time Taken (nx.Dijkstra):", timeTaken)

            #-------------------Bi-Directional Dijkstra
            timeTaken = round(timeMyBidirectionalDijkstra(Graph, initalNode, targetNode),6)
            print("Time Taken (BidirectionalDijkstra):", timeTaken)
            timeTaken = round(timeBidirectionalDijkstra(Graph, initalNode, targetNode),6)
            print("Time Taken (nx.BidirectionalDijkstra):", timeTaken)
