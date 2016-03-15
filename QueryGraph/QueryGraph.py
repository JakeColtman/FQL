from Nodes.Node import Node
from typing import List

class QueryGraph:
    def __init__(self):
        self.node_lookup = {}

    def add_node(self, node: Node):
        self.node_lookup[node.get_name()] = node

    def get_node_by_name(self, name):
        return self.node_lookup[name]

    def add_nodes(self, nodes : List[Node], replacement = False):
        for node in nodes:
            if replacement or node.get_name() not in self.node_lookup:
                self.add_node(node)
