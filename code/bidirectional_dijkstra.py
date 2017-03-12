from itertools import cycle
import networkx as nx
import matplotlib.pyplot as plt
import os
import priority_queue_dijkstra as pqd
import genGraphs as gg
import tools.referencedCode as rc


def bidirectional_dijkstra(Graph, startingNode, targetNode):
    shortest_path = float('inf')#http://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
    visitedForwards = {}
    visitedBackwards = {}
    # forwardPath=rc.idijkstra(Graph, startingNode)#use the third party dijkstra algorithm fsrom the book
    # backwardPath=rc.idijkstra(Graph, targetNode)#use the third party dijkstra algorithm from the book
    forwardPath = pqd.dijkstra(Graph,startingNode)["generator"]#get the generators from the orginal dijkstra algorithm
    backwardPath = pqd.dijkstra(Graph,targetNode)["generator"]#get the generators from the orginal dijkstra algorithm

    directions = ((visitedForwards, visitedBackwards, forwardPath), (visitedBackwards, visitedForwards, backwardPath)) #create a tuple to hold the directions
    for visited, visitedOther, path in cycle(directions): #cycle between directions (ie step from the startingNode, then targetNode, then startingNode again etc.)
        node, distance = next(path)#get the next in path
        visited[node] = distance #add to the visited dict
        if node in visitedOther: break #if we have already meet that node in the other direction, we're done
    for u in visitedForwards: #if we get here, they meet at some stage. Iterate through the visited dict (forward direction) to find where
        for v in Graph[u]: #iterate through this nodes neighbours
            if not v in visitedBackwards: continue #if its not visited in the backwards direction, continue to the next iteration
            shortest_path = min(shortest_path, visitedForwards[u] + Graph[u][v]["weight"] + visitedBackwards[v]) #if it was, check if this path is better than what we already have
    return shortest_path#return the shortest_path


def check_answer(my_shortest_path):
    print("Comparing answer to nx implementation.")
    nx_shortest_path = nx.bidirectional_dijkstra(Graph,startingNode,targetNode)[0]
    if nx_shortest_path == my_shortest_path:
        print("Answer is correct.")
    else:
        print("Answer is not correct.")
        print("The shortest path according to me: " , my_shortest_path)
        print("The shortest path according to nx: ", nx_shortest_path)

if __name__ == "__main__":
    os.system('clear')

    #generate the graph
    Graph = gg.gen_graph()

    #plot the graph with labels
    # gg.plot_graph(Graph)

    #give the arguments names so the logic behind the calling of bidirectional_dijkstra is more clear
    startingNode = "A"
    targetNode = "E"
    shortest_path = bidirectional_dijkstra(Graph,startingNode,targetNode)
    print("The shortest path (as per my solution) between %s and %s is: %s" % (startingNode, targetNode, shortest_path)) #print out the
    check_answer(shortest_path)
