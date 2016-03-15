from QueryGraph.QueryGraph import QueryGraph
from typing import List
from Nodes.Node import Node

class QueryGraphFactory:
    def create_complete_graph_from_node(self, node):
        graph = QueryGraph()
        graph.add_node(node)
        depList = node.get_dependencies()
        while len(depList) != 0:
            [graph.add_node(x) for x in depList]
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        return graph

    def create_quickest_graph_from_node(self, node):
        graph = QueryGraph()
        graph.add_node(node)
        depList = node.get_dependencies()
        while len(depList) != 0:
            [graph.add_node(x) for x in depList]
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        return graph

    def create_graph_from_node_list(self, node_list: List[Node]):
        graph = QueryGraph()
        for node in node_list:
            graph.add_node(node)
