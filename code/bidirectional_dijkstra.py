from itertools import cycle
import networkx as nx
import matplotlib.pyplot as plt
import os
import priority_queue_dijkstra as pqd
import genGraphs as gg


def bidirectional_dijkstra(Graph, startingNode, targetNode):
    shortest_path = float('inf')#http://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
    visited = {}
    visitedOther = {}
    forwardPath = pqd.dijkstra(Graph,startingNode)["generator"] #get the generators from the orginal dijkstra algo
    backwardPath = pqd.dijkstra(Graph,targetNode)["generator"]

    directions = ((visited, visitedOther, forwardPath), (visitedOther, visited, backwardPath)) #create a tuple to hold the directions
    try:
        for visited, visitedOther, path in cycle(directions): #cycle between directions (ie step from the startingNode, then targetNode, then startingNode again etc.)
            node, distance = next(path)#get the next in path
            visited[node] = distance #add to the visited dict
            if node in visitedOther: break #if we have already meet that node in the other direction, we're done
    except StopIteration: return shortest_path #if this exception is thrown, one of the directions ran out of nodes before meeting the other
    for u in visited: #if we get here, they meet at some stage. Iterate through the visited dict (forward direction) to find where
        for v in Graph[u]: #iterate through this nodes neighbours
            if not v in visitedOther: continue #if its not visited in the backwards direction, continue to the next iteration
            shortest_path = min(shortest_path, visited[u] + Graph[u][v]["weight"] + visitedOther[v]) #if it was, check if this path is better than what we already have
    return shortest_path


if __name__ == "__main__":
    os.system('clear')

    #generate the graph
    Graph = gg.gen_graph()

    #plot the graph with labels
    gg.plot_graph(Graph)

    #give the arguments names so the logic behind the calling of bidirectional_dijkstra is more clear
    startingNode = "A"
    targetNode = "E"
    shortest_path = bidirectional_dijkstra(Graph,startingNode,targetNode)
    print("The shortest path between %s and %s is: %s" % (startingNode, targetNode, shortest_path)) #print out the
