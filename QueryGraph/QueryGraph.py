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
            if node_name not in self.node_lookup:
                continue

            node = query_graph.node_lookup[node_name]
            if type(node) != PlaceholderNode:
                self.node_lookup[node.get_name()].set_docstring(node.get_docstring())
                self.node_lookup[node.get_name()].set_text(node.get_text())

        return self

    def add_query(self, query_graph: 'QueryGraph', replace = False):
        '''
            Use to combind queries together.  By default does a structural add, i.e. will only update the deps on
            existing nodes and add new nodes to the graph

            If replace = True then will wipe out existing nodes if there is a conflict.  Use carefully!
        '''
        for node_name in query_graph.node_lookup:
            node = query_graph.node_lookup[node_name]
            if type(node) != PlaceholderNode and (replace or node_name not in self.node_lookup):
                self.node_lookup[node.get_name()] = node
            else:
                old_node = self.node_lookup[node.get_name()]
                old_node.dependencies = [x for x in old_node.get_dependencies() if x.get_name() not in query_graph.node_lookup]
                for dependency in node.get_dependencies():
                    old_node.add_dependency_node(dependency)



    def list_of_nodes_on_which_nothing_depends(self):
        output = []
        all_nodes = [self.node_lookup[x] for x in self.node_lookup]
        for node in all_nodes:
            is_depended_on = any([node in x.get_dependencies() for x in all_nodes])
            if not is_depended_on:
                output.append(node)

        return output

    def get_ordered_node_list_from_node(self, node: Node):
        output = [node]
        depList = node.get_dependencies()
        while len(depList) != 0:
            [output.append(x) for x in depList]
            dependentNodes = [x.get_dependencies() for x in depList]
            depList = [item for sublist in dependentNodes for item in sublist]
        output.reverse()
        return output
