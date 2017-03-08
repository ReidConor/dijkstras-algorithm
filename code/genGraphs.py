import networkx as nx
import matplotlib.pyplot as plt
from random import randint, uniform
import math
import string
import matplotlib.pyplot as plt

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

def gen_random_graph():
    letters = list(string.ascii_uppercase)
    number = randint(0,len(letters))
    nodes = letters[:number]
    # print(nodes)
    mapping = {}
    for i in range(26):
        mapping[i]=letters.pop()
    # print(mapping)
    Graph = nx.complete_graph(len(nodes))
    Graph = nx.relabel_nodes(Graph,mapping)

    for (u, v) in Graph.edges():
        Graph.edge[u][v]['weight'] = randint(0,10)

    return Graph

if __name__ == "__main__":
    Graph = gen_random_graph()
    print(nx.number_of_nodes(Graph))
    print(nx.number_of_edges(Graph))
    print(Graph.nodes())
    # nx.draw_spectral(Graph, with_labels=True)
    # plt.show()
