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
        for node in query_graph.node_lookup:
            if type(node) != PlaceholderNode:
                self.node_lookup[node.node.get_name()].set_docstring(node.get_docstring())
                self.node_lookup[node.node.get_name()].set_text(node.get_text())

        return self

    def full_replace(self, query_graph: 'QueryGraph'):
        for node in query_graph.node_lookup:
            if type(node) != PlaceholderNode:
                self.node_lookup[node.node.get_name()] = node
