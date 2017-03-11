import networkx as nx
import matplotlib.pyplot as plt
from random import randint, uniform
import math
import string
import matplotlib.pyplot as plt
import os

def plot_graph(Graph):
    nx.draw_spectral(Graph, with_labels=True)
    plt.draw()
    plt.savefig('../notes/graph.png')

def gen_graph():
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
    return G


#below function returns a graph of random lenght, between 0 and 676 nodes.
def gen_random_graph():
    upperLetters = list(string.ascii_uppercase)#list of uppercase letters (26)
    lowerLetters = list(string.ascii_lowercase)#list of lowercase letters (26)
    numbers = [1,2]
    combo = []#to fill with pairs of the above, totalling 26*26 = 676. This forms the max amount of nodes in this graph
    print("Generating combo list")
    for upperLetter in upperLetters:
        for lowerLetter in lowerLetters:
            for number in numbers:
                combo.append(upperLetter + lowerLetter + str(number))

    number = randint(0,len(combo))#get a random number between 0 and the amount of nodes we can have (676)
    nodes = combo[:number]#slice the total nodes to get the above amount of nodes
    mapping = {}
    for i in range(len(combo)):
        mapping[i]=combo.pop()#mapping dict contains each nodes name (soem from of Aa, Bx etc)

    Graph = nx.complete_graph(len(nodes))#create a complete graph with randomly generated lenght
    Graph = nx.relabel_nodes(Graph,mapping)#add in the mappings

    for (u, v) in Graph.edges():#add in weights for each edge, randomly generated with values between 1 and 10
        Graph.edge[u][v]['weight'] = randint(1,10)

    return Graph#return the graph


#below function returns x amount of graphs of random lengths, between 0 and 1352 nodes.
def gen_random_graphs(GraphCount):
    print("Generating %s graphs" % GraphCount)
    upperLetters = list(string.ascii_uppercase)#list of uppercase letters (26)
    lowerLetters = list(string.ascii_lowercase)#list of lowercase letters (26)
    numbers = [1,2]
    combo = []#to fill with pairs of the above, totalling 26*26*2 = 1352. This forms the max amount of nodes in this graph
    for upperLetter in upperLetters:
        for lowerLetter in lowerLetters:
            for number in numbers:
                combo.append(upperLetter + lowerLetter + str(number))

    graphs = []
    for i in range(GraphCount):
        number = randint(0,len(combo))#get a random number between 0 and the amount of nodes we can have (1352)
        nodes = combo[:number]#slice the total nodes to get the above amount of nodes
        mapping = {}
        thisCombo = combo[:]#apprently without the [:] I dont actaully have two lists....need to slice
        for i in range(len(thisCombo)):
            mapping[i]=thisCombo.pop()#mapping dict contains each nodes name (soem from of Aa, Bx etc)

        Graph = nx.complete_graph(len(nodes))#create a complete graph with randomly generated lenght
        Graph = nx.relabel_nodes(Graph,mapping)#add in the mappings

        for (u, v) in Graph.edges():#add in weights for each edge, randomly generated with values between 1 and 10
            Graph.edge[u][v]['weight'] = randint(1,10)

        graphs.append(Graph)
    print("%s graphs generated." % GraphCount)
    return graphs


if __name__ == "__main__":
    os.system('clear')
    Graphs = gen_random_graphs(2)
    # print(len(Graphs))

    for Graph in Graphs:
        print(nx.number_of_nodes(Graph))
        print(nx.number_of_edges(Graph))
        print()
    # print(Graph.nodes())
    # print(Graph.edges(data=True))
    # nx.draw_spectral(Graph, with_labels=True)
    # plt.show()
