from Nodes.Node import Node


class QueryGraph:
    def __init__(self):
        self.node_lookup = {}

    def add_node(self, node: Node):
        self.node_lookup[node.get_name()] = node

    def get_node_by_name(self, name):
        return self.node_lookup[name]
