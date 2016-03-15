from QueryGraph.QueryGraph import QueryGraph
import matplotlib.pyplot as plt
import networkx as nx

class QueryGraphVisualizer:

    def __init__(self, query_graph: QueryGraph):
        self.query_graph = query_graph

    def visualize(self):
        G = nx.DiGraph()
        nodeNameList = [x for x in self.query_graph.node_lookup]
        G.add_nodes_from(nodeNameList)


        edges = []
        for name in nodeNameList:
            node = self.query_graph.node_lookup[name]
            dependencies = [x.get_name() for x in node.get_dependencies()]
            edges += [(x, name) for x in dependencies]
        G.add_edges_from(edges)
        nx.draw(G, with_labels=True)
        plt.show()