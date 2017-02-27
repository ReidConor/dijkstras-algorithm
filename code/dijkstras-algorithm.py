class Graph:
    def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distance = {}
    # self.initial

    def dijsktraAlgorithm(theGraph, initialNode):
        print("In dijsktra algo ")
