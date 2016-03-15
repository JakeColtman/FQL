from Nodes.Node import Node


class Query:
    def __init__(self):
        self.query_lookup = {}

    def add_node(self, node: Node):
        self.query_lookup[node.get_name()] = node

    def get_node_by_name(self, name):
        return self.query_lookup[name]
