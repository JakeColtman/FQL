from Nodes.Node import Node
from Nodes.PlaceholderNode import PlaceholderNode
from typing import List


class QueryGraph:
    def __init__(self):
        self.node_lookup = {}

    def add_node(self, node: Node):
        self.node_lookup[node.get_name()] = node

    def get_node_by_name(self, name):
        return self.node_lookup[name]

    def value_replace(self, query_graph: 'QueryGraph'):
        for node_name in query_graph.node_lookup:
            node = query_graph.node_lookup[node_name]
            if type(node) != PlaceholderNode:
                self.node_lookup[node.get_name()].set_docstring(node.get_docstring())
                self.node_lookup[node.get_name()].set_text(node.get_text())

        return self

    def full_replace(self, query_graph: 'QueryGraph'):
        for node in query_graph.node_lookup:
            if type(node) != PlaceholderNode:
                self.node_lookup[node.node.get_name()] = node

    def get_ordered_node_list_from_node(self, node: Node):
        output = [node]
        depList = node.get_dependencies()
        while len(depList) != 0:
            [output.append(x) for x in depList]
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        output.reverse()
        return output