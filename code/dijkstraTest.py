import time
import os
import networkx as nx
from random import *
import priority_queue_dijkstra as pqd
import bidirectional_dijkstra as dbd
import genGraphs as gg


def timed(function):
  start = time.time()
  function
  elapsed = time.time() - start
  return elapsed



def smallGraph():
    Graph = gg.gen_graph()
    print ("Details: %s nodes and %s edges." % (nx.number_of_nodes(Graph), nx.number_of_edges(Graph)))

    print("------------------------------------------")
    print ("dijkstra")
    start = time.time()
    pqd.dijkstra(Graph, "A")
    end = time.time()
    print(end - start)
    print("------------------------------------------")
    print ("bidirectional_dijkstra")
    start = time.time()
    dbd.bidirectional_dijkstra(Graph, "A", "E")
    end = time.time()
    print(end - start)
    print("------------------------------------------")


def sampleFuction(String):
    print(String)

if __name__ == "__main__":
    os.system('clear')

    for i in range(1):
        Graph = gg.gen_random_graph()
        # print(nx.nodes(Graph))
        # print(nx.edges(Graph))
        initalNode = choice(nx.nodes(Graph))
        print(initalNode)

        results = pqd.dijkstra(Graph, initalNode)
        print(results["distances"])
        # print(timed(pqd.dijkstra(Graph, choice(nx.nodes(Graph)))))
