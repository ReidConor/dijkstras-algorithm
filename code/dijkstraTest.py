import time
import os
import networkx as nx
from random import *
import priority_queue_dijkstra as pqd
import bidirectional_dijkstra as dbd
import genGraphs as gg

def timeDijkstra(Graph, initalNode):
    start = time.time()
    pqd.dijkstra(Graph, initalNode)
    elapsed = time.time() - start
    return elapsed

def timeBidirectionalDijkstra(Graph, initalNode, targetNode):
    start = time.time()
    dbd.bidirectional_dijkstra(Graph, initalNode, targetNode)
    elapsed = time.time() - start
    return elapsed

def sampleFuction(String):
    print(String)

if __name__ == "__main__":
    os.system('clear')
    print("Starting dijkstraTest")
    testCount=1
    graphsPerTest=2
    print("Running %s tests" % testCount)
    print("Using %s graphs per test" % graphsPerTest)
    print("-----------------------------------------")

    for i in range(1, testCount+1):
        print("Running test number: %s" % i )
        Graphs = gg.gen_random_graphs(graphsPerTest)
        for Graph in Graphs:
             print("Number of nodes:", len(nx.nodes(Graph)))
             print("Number of edges:",len(nx.edges(Graph)))
             initalNode = choice(nx.nodes(Graph))#chose a random node in the graph as the starter node
             timeTaken = timeDijkstra(Graph, initalNode)
             print("Time Taken (Dijkstra):", timeTaken)
             targetNode = choice(nx.nodes(Graph))
             timeTaken = timeBidirectionalDijkstra(Graph, initalNode, targetNode)
             print("Time Taken (BidirectionalDijkstra):", timeTaken)
             print("----------")
